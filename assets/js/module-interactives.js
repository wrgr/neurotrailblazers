(function () {
  function toInt(value, fallback) {
    var n = parseInt(value, 10);
    return Number.isFinite(n) ? n : fallback;
  }

  function updateProgress(root) {
    var checks = Array.from(root.querySelectorAll('.nt-progress-step'));
    if (!checks.length) return;

    var done = checks.filter(function (el) { return el.checked; }).length;
    var pct = Math.round((done / checks.length) * 100);

    var fill = root.querySelector('.nt-progress-fill');
    var bar = root.querySelector('.nt-progress-bar');
    var text = root.querySelector('.nt-progress-text');
    if (fill) fill.style.width = pct + '%';
    if (bar) bar.setAttribute('aria-valuenow', String(pct));
    if (text) text.textContent = pct + '% complete';
  }

  function storageKey(root) {
    var slug = root.getAttribute('data-module-slug') || 'module';
    return 'nt-progress-' + slug;
  }

  function saveState(root) {
    var key = storageKey(root);
    var steps = Array.from(root.querySelectorAll('.nt-progress-step')).map(function (el) {
      return !!el.checked;
    });
    var data = {
      steps: steps,
      quizPassed: root.getAttribute('data-quiz-passed') === 'true',
      taskPassed: root.getAttribute('data-task-passed') === 'true'
    };
    try {
      localStorage.setItem(key, JSON.stringify(data));
    } catch (err) {
      return;
    }
  }

  function loadState(root) {
    var key = storageKey(root);
    var raw;
    try {
      raw = localStorage.getItem(key);
    } catch (err) {
      raw = null;
    }
    if (!raw) return;

    try {
      var data = JSON.parse(raw);
      var checks = Array.from(root.querySelectorAll('.nt-progress-step'));
      checks.forEach(function (el, i) {
        el.checked = !!(data.steps && data.steps[i]);
      });
      root.setAttribute('data-quiz-passed', data.quizPassed ? 'true' : 'false');
      root.setAttribute('data-task-passed', data.taskPassed ? 'true' : 'false');
    } catch (err2) {
      return;
    }
  }

  function initQuiz(root) {
    var submit = root.querySelector('.nt-quiz-submit');
    var scoreNode = root.querySelector('.nt-score');
    var passScore = toInt(root.getAttribute('data-quiz-pass'), 2);
    if (!submit) return;

    submit.addEventListener('click', function () {
      var questions = Array.from(root.querySelectorAll('.nt-quiz-question'));
      var score = 0;

      questions.forEach(function (q, idx) {
        var expected = toInt(q.getAttribute('data-correct-index'), -1);
        var selected = q.querySelector('input[type="radio"]:checked');
        var feedback = q.querySelector('.nt-feedback');
        var explanation = q.querySelector('.nt-explanation');
        var selectedVal = selected ? toInt(selected.value, -2) : -2;
        var ok = selectedVal === expected;

        if (ok) score += 1;

        if (feedback) {
          if (!selected) {
            feedback.textContent = 'Select an answer.';
            feedback.className = 'nt-feedback nt-feedback-warn';
          } else if (ok) {
            feedback.textContent = 'Correct';
            feedback.className = 'nt-feedback nt-feedback-ok';
          } else {
            feedback.textContent = 'Not yet';
            feedback.className = 'nt-feedback nt-feedback-bad';
          }
        }

        if (explanation) {
          explanation.style.display = 'block';
        }
      });

      var passed = score >= passScore;
      root.setAttribute('data-quiz-passed', passed ? 'true' : 'false');

      if (scoreNode) {
        scoreNode.textContent = 'Score: ' + score + '/' + questions.length + (passed ? ' (passed)' : ' (review and retry)');
      }

      var checks = root.querySelectorAll('.nt-progress-step');
      if (checks[3]) checks[3].checked = passed;

      updateProgress(root);
      saveState(root);
    });
  }

  function initTask(root) {
    var submit = root.querySelector('.nt-task-submit');
    var node = root.querySelector('.nt-task-feedback');
    var block = root.querySelector('.nt-task-options');
    if (!submit || !node || !block) return;

    submit.addEventListener('click', function () {
      var expected = toInt(block.getAttribute('data-task-correct'), -1);
      var selected = block.querySelector('input[type="radio"]:checked');
      if (!selected) {
        node.textContent = 'Select one option.';
        node.className = 'nt-task-feedback nt-feedback-warn';
        return;
      }

      var ok = toInt(selected.value, -2) === expected;
      node.textContent = ok ? node.getAttribute('data-correct-feedback') : node.getAttribute('data-incorrect-feedback');
      node.className = ok ? 'nt-task-feedback nt-feedback-ok' : 'nt-task-feedback nt-feedback-bad';

      root.setAttribute('data-task-passed', ok ? 'true' : 'false');
      var checks = root.querySelectorAll('.nt-progress-step');
      if (checks[4]) checks[4].checked = ok;
      updateProgress(root);
      saveState(root);
    });
  }

  function initProgress(root) {
    var checks = Array.from(root.querySelectorAll('.nt-progress-step'));
    checks.forEach(function (el) {
      el.addEventListener('change', function () {
        updateProgress(root);
        saveState(root);
      });
    });

    var reset = root.querySelector('.nt-progress-reset');
    if (reset) {
      reset.addEventListener('click', function () {
        checks.forEach(function (el) { el.checked = false; });
        root.setAttribute('data-quiz-passed', 'false');
        root.setAttribute('data-task-passed', 'false');
        var key = storageKey(root);
        try { localStorage.removeItem(key); } catch (err) { }
        var scoreNode = root.querySelector('.nt-score');
        var taskNode = root.querySelector('.nt-task-feedback');
        if (scoreNode) scoreNode.textContent = '';
        if (taskNode) {
          taskNode.textContent = '';
          taskNode.className = 'nt-task-feedback';
        }
        root.querySelectorAll('.nt-feedback').forEach(function (n) {
          n.textContent = '';
          n.className = 'nt-feedback';
        });
        root.querySelectorAll('.nt-explanation').forEach(function (n) {
          n.style.display = 'none';
        });
        updateProgress(root);
      });
    }

    updateProgress(root);
  }

  function init(root) {
    root.setAttribute('data-quiz-passed', 'false');
    root.setAttribute('data-task-passed', 'false');
    loadState(root);
    initQuiz(root);
    initTask(root);
    initProgress(root);
    updateProgress(root);
  }

  document.addEventListener('DOMContentLoaded', function () {
    var roots = document.querySelectorAll('.nt-interactive-lab');
    roots.forEach(init);
  });
})();

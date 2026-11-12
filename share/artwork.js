export function drawNetwork(canvas) {
  const ctx = canvas.getContext('2d');
  const points = Array.from({length: 38}, (_, i) => {
    const angle = i * 2.399963;
    const radius = 21 + 29 * Math.sqrt(i);
    return [330 + Math.cos(angle) * radius * 1.32, 205 + Math.sin(angle) * radius * .84];
  });
  points.forEach(([x,y], i) => {
    points.slice(i+1).forEach(([xx,yy]) => {
      const distance = Math.hypot(x-xx,y-yy);
      if (distance < 94) {
        ctx.beginPath();
        ctx.moveTo(x,y);
        ctx.quadraticCurveTo((x+xx)/2 + 16,(y+yy)/2 - 17,xx,yy);
        ctx.strokeStyle = 'rgba(164,223,162,' + ((1-distance/120)*.58) + ')';
        ctx.stroke();
      }
    });
    ctx.beginPath();
    ctx.arc(x,y,i%7===0?6:2.8,0,Math.PI*2);
    ctx.shadowBlur = 13;
    ctx.shadowColor = '#c7f28a';
    ctx.fillStyle = i%4===0?'#e2fa9e':'#81cbac';
    ctx.fill();
    ctx.shadowBlur = 0;
  });
}
function wrap(ctx, text, width) {
  return text.split('\n').flatMap(paragraph => {
    const lines = [];
    let line = '';
    for (const word of paragraph.trim().split(/\s+/u)) {
      const candidate = line ? line + ' ' + word : word;
      if (ctx.measureText(candidate).width <= width) {
        line = candidate;
        continue;
      }
      if (line) lines.push(line);
      line = '';
      for (const char of word) {
        if (ctx.measureText(line + char).width > width) {
          lines.push(line);
          line = '';
        }
        line += char;
      }
    }
    if (line) lines.push(line);
    return lines;
  });
}
export function drawPoster(canvas, content) {
  const ctx = canvas.getContext('2d');
  const palette = content.template === 'atlas'
    ? {top:'#123c31', ink:'#153d32', accent:'#ceee9a', bg:'#f0f6e9', line:'#9bb6a0'}
    : {top:'#262650', ink:'#262650', accent:'#d9d2ff', bg:'#f1eff9', line:'#a9a2c6'};
  const {top,ink,accent,bg,line} = palette;
  const left = 74;
  const full = 1052;
  let fits = true;
  function text(value,x,y,width,font,leading,color) {
    ctx.font = font;
    ctx.fillStyle = color;
    const lines = wrap(ctx,value,width);
    lines.forEach((item,i) => ctx.fillText(item,x,y+leading*i));
    return y+leading*lines.length;
  }
  ctx.fillStyle = bg;
  ctx.fillRect(0,0,1200,1600);
  ctx.fillStyle = top;
  ctx.fillRect(0,0,1200,390);
  text('RESEARCH IN ONE MINUTE',left,72,full,'bold 24px system-ui',32,accent);
  text(content.scope.toUpperCase(),left,118,full,'bold 23px system-ui',30,'#fff');
  if (text(content.values.headline || 'Your poster headline',left,207,full,'76px Georgia',78,'#fff') > 440) fits = false;
  ctx.fillStyle = accent;
  ctx.fillRect(left,352,130,8);
  const blocks = content.sections.slice(1);
  let y = 459;
  for (const [key,label] of blocks) {
    y = text(label.toUpperCase(),left,y,full,'bold 24px system-ui',31,ink);
    y = text(content.values[key],left,y+8,full,'34px system-ui',43,ink);
    ctx.fillStyle = line;
    ctx.fillRect(left,y-12,full,1);
    y += 36;
  }
  const footerTop = 1304;
  if (y > footerTop + 15) fits = false;
  ctx.fillStyle = top;
  ctx.fillRect(0,footerTop,1200,296);
  let fy = 1346;
  for (const item of content.footer) {
    fy = text(item,left,fy,full,'23px system-ui',29,'#fff');
  }
  return fits && fy <= 1604;
}

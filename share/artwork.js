import qrcode from './qrcode.js';

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
function drawDiagram(ctx, style, palette) {
  const centers = [334, 866];
  ctx.strokeStyle = palette.ink;
  ctx.lineWidth = 5;
  ctx.beginPath();
  ctx.moveTo(455, 544);
  ctx.lineTo(745, 544);
  if (style === 'process') {
    ctx.moveTo(720, 525);
    ctx.lineTo(745, 544);
    ctx.lineTo(720, 563);
  } else if (style === 'comparison') {
    ctx.moveTo(480, 525);
    ctx.lineTo(455, 544);
    ctx.lineTo(480, 563);
    ctx.moveTo(720, 525);
    ctx.lineTo(745, 544);
    ctx.lineTo(720, 563);
  }
  ctx.stroke();
  for (const [index,x] of centers.entries()) {
    ctx.fillStyle = palette.paper;
    ctx.beginPath();
    ctx.roundRect(x-112,462,224,164,20);
    ctx.fill();
    const points = [[-61,-40],[46,-44],[-10,0],[-48,39],[57,42]];
    if (style === 'relationship' && index === 1) {
      ctx.strokeStyle = palette.ink;
      ctx.lineWidth = 4;
      for (const [a,b] of [[0,2],[1,2],[2,3],[2,4],[1,4]]) {
        ctx.beginPath();
        ctx.moveTo(x+points[a][0],544+points[a][1]);
        ctx.lineTo(x+points[b][0],544+points[b][1]);
        ctx.stroke();
      }
    }
    if (style === 'relationship') {
      points.forEach(([dx,dy],i) => {
        ctx.fillStyle = i%2 ? palette.line : palette.top;
        ctx.beginPath();
        ctx.arc(x+dx,544+dy,12,0,Math.PI*2);
        ctx.fill();
      });
    } else {
      ctx.fillStyle = index ? palette.line : palette.top;
      ctx.beginPath();
      if (index) ctx.roundRect(x-34,510,68,68,12);
      else ctx.arc(x,544,34,0,Math.PI*2);
      ctx.fill();
    }
  }
}
function drawQR(ctx, url, x, y, size) {
  const code = qrcode(0,'M');
  code.addData(url);
  code.make();
  const count = code.getModuleCount();
  const cell = Math.floor(size/(count+8));
  const extent = cell*(count+8);
  x += Math.floor((size-extent)/2);
  y += Math.floor((size-extent)/2);
  ctx.fillStyle = '#fff';
  ctx.fillRect(x,y,extent,extent);
  ctx.fillStyle = '#111';
  for (let row=0; row<count; row++) {
    for (let column=0; column<count; column++) {
      if (code.isDark(row,column)) ctx.fillRect(x+(column+4)*cell,y+(row+4)*cell,cell,cell);
    }
  }
}
export function drawPoster(canvas, {template, values, footer, diagram, illustration, url}) {
  const ctx = canvas.getContext('2d');
  const palette = template === 'atlas'
    ? {top:'#153f35', ink:'#123e37', accent:'#b9e7ae', bg:'#f8fbf6', diagram:'#e5f2e3', paper:'#f8fbf6', line:'#4a836e'}
    : {top:'#102c59', ink:'#102c59', accent:'#9fe4ec', bg:'#f8fbfe', diagram:'#e4f3f7', paper:'#f9fcfe', line:'#288293'};
  const {top,ink,accent,bg,line} = palette;
  const left = 58;
  const full = 1084;
  let fits = true;
  ctx.setTransform(canvas.width/1200,0,0,canvas.height/1600,0,0);
  function text(value,x,y,width,font,leading,color,maxLines,align='left') {
    ctx.font = font;
    ctx.fillStyle = color;
    ctx.textAlign = align;
    const lines = wrap(ctx,value,width);
    if (lines.length > maxLines) fits = false;
    lines.slice(0,maxLines).forEach((item,i) => ctx.fillText(item,x,y+leading*i));
    return y+leading*Math.min(lines.length,maxLines);
  }
  function panel(x,y,width,height,fill,stroke) {
    ctx.beginPath();
    ctx.roundRect(x,y,width,height,18);
    ctx.fillStyle = fill;
    ctx.fill();
    ctx.strokeStyle = stroke;
    ctx.lineWidth = 2;
    ctx.stroke();
  }
  function heading(label,x,y,width,color=ink) {
    text(label,x,y,width,'bold 28px system-ui',30,color,1);
  }
  function card(label,value,x,y) {
    panel(x,y,530,201,palette.paper,line);
    heading(label,x+23,y+42,484);
    text(value,x+23,y+82,484,'26px system-ui',28,ink,5);
  }
  ctx.fillStyle = bg;
  ctx.fillRect(0,0,1200,1600);
  ctx.fillStyle = top;
  ctx.fillRect(0,0,1200,378);
  text('RESEARCH IN ONE MINUTE',left,62,full,'bold 24px system-ui',28,accent,1);
  text(values.headline || 'Your big question?',left,139,full,'bold 73px Georgia',74,'#fff',2);
  text(values.discovery,left,274,full,'bold 34px system-ui',37,'#fff',3);
  panel(left,404,full,313,palette.diagram,line);
  heading('How it fits together',left+24,446,710);
  text(illustration ? 'ILLUSTRATION' : 'CONCEPTUAL DIAGRAM',left+full-24,442,280,'bold 17px system-ui',20,ink,1,'right');
  if (illustration) {
    const scale = Math.min(1010 / illustration.width, 182 / illustration.height);
    const width = illustration.width * scale;
    const height = illustration.height * scale;
    ctx.drawImage(illustration, 600-width/2, 549-height/2, width, height);
  } else drawDiagram(ctx,diagram,palette);
  text(values.visualA,334,667,402,'bold 29px system-ui',30,ink,2,'center');
  text(values.visualB,866,667,402,'bold 29px system-ui',30,ink,2,'center');
  card('The puzzle',values.problem,left,738);
  card('What we did',values.contribution,612,738);
  card('What the evidence showed',values.finding,left,958);
  card('Why it matters',values.relevance,612,958);
  panel(left,1180,full,142,'#fff1d8','#ba8134');
  heading("What’s next",left+23,1221,full-46,'#68400c');
  text(values.limit,left+23,1261,full-46,'bold 26px system-ui',29,'#51330e',2);
  ctx.fillStyle = top;
  ctx.fillRect(0,1345,1200,255);
  const footerWidth = url ? 860 : full;
  text(values.invitation,left,1393,footerWidth,'bold 33px system-ui',35,accent,2);
  let footerY = 1470;
  for (const item of footer) {
    const maxLines = Math.max(0,Math.floor((1585-footerY)/22)+1);
    footerY = text(item,left,footerY,footerWidth,'18px system-ui',22,'#fff',maxLines);
  }
  if (url) {
    drawQR(ctx,url,955,1381,180);
    text('LEARN MORE',1045,1580,180,'bold 16px system-ui',20,'#fff',1,'center');
  }
  return fits;
}

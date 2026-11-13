// Embed the rendered poster as a single image on an 18 × 24 inch page.
export async function posterPDF(canvas) {
  const image = await new Promise(resolve => canvas.toBlob(resolve,'image/jpeg',0.97));
  if (!image) throw new Error('Poster image encoding failed');
  const pageWidth = 1296;
  const pageHeight = 1728;
  const drawing = 'q\n' + pageWidth + ' 0 0 ' + pageHeight + ' 0 0 cm\n/Poster Do\nQ\n';
  const objects = [
    ['<< /Type /Catalog /Pages 2 0 R >>'],
    ['<< /Type /Pages /Kids [3 0 R] /Count 1 >>'],
    ['<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ' + pageWidth + ' ' + pageHeight +
      '] /Resources << /XObject << /Poster 4 0 R >> >> /Contents 5 0 R >>'],
    ['<< /Type /XObject /Subtype /Image /Width ' + canvas.width + ' /Height ' + canvas.height +
      ' /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length ' + image.size + ' >>\nstream\n',
      image, '\nendstream'],
    ['<< /Length ' + drawing.length + ' >>\nstream\n' + drawing + 'endstream']
  ];
  const header = '%PDF-1.4\n';
  const parts = [header];
  const offsets = [];
  let position = header.length;
  objects.forEach((object,index) => {
    const chunks = [(index+1) + ' 0 obj\n', ...object, '\nendobj\n'];
    offsets.push(position);
    for (const chunk of chunks) {
      parts.push(chunk);
      position += typeof chunk === 'string' ? chunk.length : chunk.size;
    }
  });
  parts.push('xref\n0 6\n0000000000 65535 f \n',
    ...offsets.map(offset => String(offset).padStart(10,'0') + ' 00000 n \n'),
    'trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n' + position + '\n%%EOF\n');
  return new Blob(parts,{type:'application/pdf'});
}

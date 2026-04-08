#!/bin/bash
while true; do
  if ! pgrep -f "python3 scripts/find_pdfs.py" > /dev/null; then
    echo "✓ Script finished!"
    break
  fi
  
  progress=$(tail -1 scripts/bibliometrics/output/pdf_finder_log.txt 2>/dev/null)
  echo "$(date '+%H:%M:%S') - $progress"
  sleep 10
done

echo -e "\n=== FINAL RESULTS ==="
ls -lh scripts/bibliometrics/output/connectomics_papers_pdf* 2>/dev/null

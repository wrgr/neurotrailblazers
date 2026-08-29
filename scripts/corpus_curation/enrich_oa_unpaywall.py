#!/usr/bin/env python3
"""Checks Unpaywall and Europe PMC for remaining papers without OA PDFs."""
import json
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent

def check_unpaywall(doi: str):
    url = f"https://api.unpaywall.org/v2/{doi}?email=curation@neurotrailblazers.org"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            best_loc = data.get("best_oa_location") or {}
            pdf_url = best_loc.get("url_for_pdf") or best_loc.get("url")
            is_oa = data.get("is_oa", False)
            if pdf_url and is_oa:
                return doi, {
                    "pdf_url": pdf_url,
                    "is_oa": is_oa,
                    "oa_status": data.get("oa_status"),
                    "source": "unpaywall"
                }
    except Exception:
        pass
    return doi, None

def check_epmc(doi: str):
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22{urllib.parse.quote(doi)}%22&format=json"
    req = urllib.request.Request(url, headers={"User-Agent": "NeuroTrailblazers/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            results = data.get("resultList", {}).get("result", [])
            if results:
                res = results[0]
                pmcid = res.get("pmcid")
                is_oa = res.get("isOpenAccess") == "Y" or bool(pmcid)
                if pmcid:
                    return doi, {
                        "pdf_url": f"https://www.ncbi.nlm.nih.gov/pmc/articles/{pmcid}/pdf/",
                        "is_oa": True,
                        "oa_status": "gold",
                        "source": "europepmc"
                    }
    except Exception:
        pass
    return doi, None

def main():
    oa_path = SCRIPT_DIR / "oa_links_2000.json"
    oa_data = json.loads(oa_path.read_text()) if oa_path.exists() else {}

    sel_path = SCRIPT_DIR / "final_selection.json"
    sel_data = json.loads(sel_path.read_text())
    dois = [d.lower().strip() for d in sel_data["papers"].keys()]

    missing_dois = [d for d in dois if not oa_data.get(d, {}).get("pdf_url")]
    print(f"Checking Unpaywall and Europe PMC for {len(missing_dois)} remaining papers...")

    found = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_unpaywall, d): d for d in missing_dois}
        for fut in as_completed(futures):
            doi, res = fut.result()
            if res and res.get("pdf_url"):
                oa_data[doi] = res
                found += 1

    print(f"Unpaywall pass resolved {found} additional OA PDFs.")

    # Europe PMC pass on remaining
    still_missing = [d for d in dois if not oa_data.get(d, {}).get("pdf_url")]
    print(f"Checking Europe PMC for {len(still_missing)} remaining papers...")
    found_epmc = 0
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(check_epmc, d): d for d in still_missing}
        for fut in as_completed(futures):
            doi, res = fut.result()
            if res and res.get("pdf_url"):
                oa_data[doi] = res
                found_epmc += 1

    print(f"Europe PMC pass resolved {found_epmc} additional OA PDFs.")
    oa_path.write_text(json.dumps(oa_data, indent=2))

    total_pdf = sum(1 for v in oa_data.values() if v.get("pdf_url"))
    print(f"Final Total with Direct PDF Links: {total_pdf} / {len(dois)} ({total_pdf/len(dois)*100:.1f}%)")

if __name__ == "__main__":
    main()

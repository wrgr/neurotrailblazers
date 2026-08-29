#!/usr/bin/env python3
"""Ingests global BRAIN training/outreach, workforce development, and translational health/disease papers into the corpus."""
import json
import urllib.request
import urllib.parse
from pathlib import Path
from typing import Dict, Any, List

SCRIPT_DIR = Path(__file__).resolve().parent

# Target expansion DOIs across global training/outreach and translational health
EXPANSION_PAPERS = [
    # Training, Outreach, Workforce & Citizen Science
    {"doi": "10.18260/1-2--43271", "title": "Empowering Trailblazers toward Scalable, Systematized, Research-Based Workforce Development", "venue": "ASEE Annual Conference & Exposition", "year": 2023, "category_hint": "training-outreach"},
    {"doi": "10.18260/1-2--42839", "title": "Board 51: Utilizing Technical Competitions to Enhance Diverse Workforce Recruitment and Retention", "venue": "ASEE Annual Conference & Exposition", "year": 2023, "category_hint": "training-outreach"},
    {"doi": "10.18260/1-2--42544", "title": "A SwarmAI Testbed for Workforce Development and Collaborative, Interdisciplinary Research", "venue": "ASEE Annual Conference & Exposition", "year": 2023, "category_hint": "training-outreach"},
    {"doi": "10.1109/isecon.2018.8340503", "title": "CIRCUIT summer program: A computational neuroscience outreach experience for high-achieving undergraduates via sponsored research", "venue": "IEEE Integrated STEM Education Conference (ISEC)", "year": 2018, "category_hint": "training-outreach"},
    {"doi": "10.1109/isec49744.2020.9280735", "title": "STEM Leadership and Training for Trailblazing Students in an Immersive Research Environment", "venue": "IEEE Integrated STEM Education Conference (ISEC)", "year": 2020, "category_hint": "training-outreach"},
    {"doi": "10.48550/arxiv.1804.08197", "title": "syGlass: Interactive Exploration of Multidimensional Images Using Virtual Reality Head-mounted Displays", "venue": "arXiv / Frontiers in Neuroinformatics", "year": 2018, "category_hint": "training-outreach"},
    {"doi": "10.1016/j.neulet.2021.136074", "title": "Quantitative skills in undergraduate neuroscience education in the connectomics era", "venue": "Neuroscience Letters", "year": 2021, "category_hint": "training-outreach"},
    {"doi": "10.1016/j.conb.2017.06.007", "title": "Computational training for the next generation of neuroscientists", "venue": "Current Opinion in Neurobiology", "year": 2017, "category_hint": "training-outreach"},
    {"doi": "10.1073/pnas.1807190116", "title": "Citizen science frontiers: Efficiency, engagement, and learning in crowdsourced research", "venue": "Proceedings of the National Academy of Sciences (PNAS)", "year": 2019, "category_hint": "training-outreach"},
    {"doi": "10.1016/j.chb.2016.12.074", "title": "An investigation of player motivations in Eyewire, a gamified citizen science game for connectomics", "venue": "Computers in Human Behavior", "year": 2017, "category_hint": "training-outreach"},
    
    # Translational Health & Connectopathies (Global Milestones)
    {"doi": "10.1016/j.neuroimage.2011.12.090", "title": "Schizophrenia, neuroimaging and connectomics", "venue": "NeuroImage", "year": 2012, "category_hint": "health"},
    {"doi": "10.1038/s41467-019-08944-1", "title": "Atypical functional connectome hierarchy in autism", "venue": "Nature Communications", "year": 2019, "category_hint": "health"},
    {"doi": "10.1038/sdata.2017.10", "title": "Enhancing studies of the connectome in autism using the Autism Brain Imaging Data Exchange II", "venue": "Scientific Data", "year": 2017, "category_hint": "health"},
    {"doi": "10.1097/wco.0b013e32835ee5b8", "title": "Connectomics and epilepsy", "venue": "Current Opinion in Neurology", "year": 2013, "category_hint": "health"},
    {"doi": "10.1016/j.neuron.2012.03.004", "title": "Predicting Regional Neurodegeneration from the Healthy Brain Functional Connectome", "venue": "Neuron", "year": 2012, "category_hint": "health"},
    {"doi": "10.1038/s41582-021-00529-1", "title": "The human connectome in Alzheimer disease — relationship to biomarkers and genetics", "venue": "Nature Reviews Neurology", "year": 2021, "category_hint": "health"},
    {"doi": "10.1136/jnnp-2011-301944", "title": "Large scale brain models of epilepsy: dynamics meets connectomics", "venue": "Journal of Neurology, Neurosurgery & Psychiatry", "year": 2012, "category_hint": "health"},
    {"doi": "10.1111/epi.13133", "title": "Connectomics and graph theory analyses: Novel insights into network abnormalities in epilepsy", "venue": "Epilepsia", "year": 2015, "category_hint": "health"},
    {"doi": "10.1016/j.biopsych.2016.07.012", "title": "Connectome Disconnectivity and Cortical Gene Expression in Patients with Schizophrenia", "venue": "Biological Psychiatry", "year": 2016, "category_hint": "health"},
    {"doi": "10.1016/j.nicl.2014.05.004", "title": "Disruption of structure–function coupling in the schizophrenia connectome", "venue": "NeuroImage: Clinical", "year": 2014, "category_hint": "health"},
    {"doi": "10.1016/j.neuron.2014.08.052", "title": "Stroke and the Connectome: How Connectivity Guides Therapeutic Intervention", "venue": "Neuron", "year": 2014, "category_hint": "health"},
    {"doi": "10.1523/jneurosci.4396-15.2016", "title": "Multivariate Connectome-Based Symptom Mapping in Post-Stroke Patients", "venue": "Journal of Neuroscience", "year": 2016, "category_hint": "health"},
    {"doi": "10.1016/j.nicl.2018.06.018", "title": "The structural connectome in traumatic brain injury", "venue": "NeuroImage: Clinical", "year": 2018, "category_hint": "health"},
    {"doi": "10.1016/j.conb.2012.04.012", "title": "Human connectomics and clinical applications in neurological and psychiatric disease", "venue": "Current Opinion in Neurobiology", "year": 2012, "category_hint": "health"}
]

def fetch_openalex_abstract(doi: str) -> str:
    url = f"https://api.openalex.org/works/https://doi.org/{doi}"
    req = urllib.request.Request(url, headers={"User-Agent": "mailto:curation@neurotrailblazers.org"})
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            inv = data.get("abstract_inverted_index")
            if inv:
                words = []
                for word, pos_list in inv.items():
                    for pos in pos_list:
                        words.append((pos, word))
                words.sort()
                return " ".join([w[1] for w in words])
    except Exception:
        pass
    return ""

def main():
    print(f"Ingesting {len(EXPANSION_PAPERS)} global expansion papers...")
    
    # Load existing TSV entries
    tsv_meta = {}
    for b in range(20):
        p = SCRIPT_DIR / f"cbatches/cbatch_{b:02d}.tsv"
        if p.exists():
            for line in p.read_text().splitlines():
                if not line.strip(): continue
                parts = line.split("\t")
                tsv_meta[parts[0]] = {
                    "title": parts[1] if len(parts)>1 else "",
                    "venue": parts[2] if len(parts)>2 else "",
                    "abstract": parts[3] if len(parts)>3 else ""
                }
    
    # Ingest new records into expanded_meta.json
    expanded_meta = dict(tsv_meta)
    added = 0
    
    for item in EXPANSION_PAPERS:
        doi = item["doi"]
        if doi not in expanded_meta:
            abstract = fetch_openalex_abstract(doi)
            expanded_meta[doi] = {
                "title": item["title"],
                "venue": item["venue"],
                "abstract": abstract if abstract else item["title"]
            }
            added += 1
            print(f"  [+ Added] {doi:30s} | {item['title'][:60]}")
        else:
            print(f"  [Already in pool] {doi:30s}")
            
    out_file = SCRIPT_DIR / "expanded_corpus_meta.json"
    out_file.write_text(json.dumps(expanded_meta, indent=2))
    print(f"\nUnified Corpus Metadata written to {out_file} (Total: {len(expanded_meta)} papers, {added} newly ingested).")

if __name__ == "__main__":
    main()

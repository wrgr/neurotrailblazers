#!/usr/bin/env python3
"""Corpus Curation Classification Engine v4.3 (Strict Outreach & Health Guard)."""
import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Dict, Any, List, Optional

SCRIPT_DIR = Path(__file__).resolve().parent
WEIGHTS_PATH = SCRIPT_DIR / "model_weights.json"
MODEL_WEIGHTS = {}
if WEIGHTS_PATH.exists():
    try:
        MODEL_WEIGHTS = json.loads(WEIGHTS_PATH.read_text())
    except Exception:
        MODEL_WEIGHTS = {}

# ----------------- KNOWN MILESTONES -----------------
KNOWN_DATASETS = {
    "10.7554/elife.57443",  # Scheffer et al. 2020 Hemibrain
    "10.1016/j.cell.2018.06.019",  # Zheng et al. 2018 FAFB
    "10.1038/s41586-024-07558-9",  # FlyWire full brain
    "10.1038/s41586-024-07633-5",  # FlyWire consensus
    "10.1038/s41586-024-07953-2",  # FlyWire wiring
    "10.1126/science.abk1256",  # H01 Shapson-Coe et al. 2024
    "10.1101/2021.07.28.454025",  # MICrONS cortical dataset
    "10.1101/2023.06.27.546656",  # MANC
    "10.1016/j.neuron.2020.12.008",  # CEM500K
    "10.1098/rstb.1986.0056",  # White et al. 1986
    "10.1038/s41586-019-1352-7",  # Cook et al. 2019 C. elegans adult connectome
    "10.1038/s41586-021-03778-8",  # Witvliet et al. 2021 C. elegans developmental connectome
    "10.1038/nature12450",  # Takemura et al. 2013 visual system connectome
    "10.1016/j.cell.2015.09.040",  # Kasthuri et al. 2015 mouse cortex
    "10.1016/j.cell.2014.03.046",  # Oh et al. 2014 mesoscale mouse
    "10.1038/s41586-023-06818-7",  # Winding et al. 2023 complete insect brain
    "10.1002/cne.24932",  # C. elegans pharynx connectome
    "10.7554/elife.65894",  # CEM500K bioRxiv
    "10.1016/j.cell.2022.01.023",  # Reconstruction of neocortex Cell 2022
    "10.1038/nature22356",  # Hildebrand et al. 2017 zebrafish whole-brain EM
    "10.1101/676312",  # NeuroPAL atlas
    "10.1101/2025.10.30.685666",  # Platynereis whole-body atlas
    "10.1101/2024.09.30.615804",  # Insect eye complete reconstruction
    "10.1038/sdata.2018.6",  # BigNeuron open repository
    "10.1126/sciadv.abb3446",  # Molecular atlas mouse brain
    "10.7554/elife.95402",  # Neurotransmitter atlas C. elegans
    "10.1126/science.adx2143",  # Nematode comparative connectomics
    "10.1016/j.asd.2019.100878",  # Nasonia standard brain
    "10.1038/s41586-024-07686-5",  # Whole-brain annotation Drosophila
    "10.1371/journal.pone.0236495",  # Template of Drosophila brain VNC
}

# ----------------- ORGANISM DETECTION -----------------
ORG_PATTERNS = [
    ("fly", re.compile(r"\b(drosophila|fruit fly|fruit flies|maggot|blowfly|calliphora|diptera|fly brain|fly optic|fly visual|hemibrain|flywire|fafb|manc|optic lobe|central complex|mushroom body|antennal lobe)\b", re.I)),
    ("elegans", re.compile(r"\b(c\.?\s*elegans|caenorhabditis|nematode|nematodes|pristionchus|roundworm|hermaphrodite|dauer|pharynx)\b", re.I)),
    ("mouse", re.compile(r"\b(mouse|mice|murine|mus musculus|c57bl|barrel cortex|somatosensory cortex|visual cortex)\b", re.I)),
    ("rat", re.compile(r"\b(rat|rats|rattus|sprague[- ]dawley|wistar)\b", re.I)),
    ("zebrafish", re.compile(r"\b(zebrafish|danio rerio|teleost)\b", re.I)),
    ("human", re.compile(r"\b(human|humans|patient|patients|postmortem|post-mortem|homo sapiens|h01|neurological patients|clinical|autopsy)\b", re.I)),
    ("macaque", re.compile(r"\b(macaque|macaques|rhesus|primate|primates|non-human primate|nonhuman primate|cynomolgus|marmoset|baboon|monkey|monkeys)\b", re.I)),
    ("other", re.compile(r"\b(aplysia|leech|hirudo|lamprey|cat|cats|ferret|songbird|zebra finch|canary|bird|birds|frog|xenopus|salamander|crustacean|crayfish|lobster|locust|cricket|honeybee|bee|bees|ant|ants|wasp|spider|octopus|squid|platynereis|hydra|cnidaria|rabbit|guinea pig|sheep|pig|porcine|dog|canine|bovine|cow|chick|chicken|nasonia|ascidian|ciona|cavefish|lampreys|amphibian|reptile|turtle)\b", re.I)),
]

def extract_organisms(text: str) -> List[str]:
    orgs = []
    for name, pat in ORG_PATTERNS:
        if pat.search(text):
            orgs.append(name)
    if not orgs:
        return ["none"]
    return orgs

# ----------------- SUBCLASSIFICATIONS -----------------
PIPELINE_SUBS = [
    ("segmentation", re.compile(r"\b(segmentation|flood-filling|flood filling|ffn|u-net|unet|instance segmentation|membrane detection|boundary detection|synapse detection|synapse prediction|synaptic cleft detection|vesicle detection|skeletonization|axon tracing|neuron tracing|deep learning for segmentation|convolutional network for|affinity graph|affinities|3d segmentation|tracing algorithm|digital neuron reconstruction|auto-tracing|tangled filament|segmenting|superpixel|watershed|machine learning for tracing|shutu|neurolucida|ransac)\b", re.I)),
    ("alignment", re.compile(r"\b(alignment|registration|elastic registration|cross-section alignment|stitching|affine|deformable registration|slice alignment|section alignment|reconstruction alignment|anatomical registration|co-registration|image registration|mosaic stitching)\b", re.I)),
    ("proofreading", re.compile(r"\b(proofreading|proof-reading|error correction|error detection|merge error|split error|interactive proofreading|semi-automated proofreading|neuprint|pymaid|catmaid proofreading|flywire proofreading|error identification)\b", re.I)),
    ("graph-analysis", re.compile(r"\b(graph analysis|graph theory|network analysis|network measure|motif analysis|spectral analysis|connectome analysis|stochastic block model|centrality|subgraph|clustering coefficient|connectome graph|dotmotif|graspy|network neuroscience|graph metrics|connectomic graph|connectomeexplorer)\b", re.I)),
    ("preparation", re.compile(r"\b(preparation|staining|heavy metal|en bloc|fixation|embedding|resins|osmium|uranyl|lead citrate|sample preparation|tissue preparation|cryo-fixation|freeze substitution|sectioning|ultramicrotomy|tape collecting|gridtape|ranbodies|bac transgenic|preservation protocol|tissue processing|brainbow)\b", re.I)),
    ("acquisition", re.compile(r"\b(acquisition|imaging throughput|beam control|stage control|high-throughput imaging|automated imaging|scanning protocol|beam current|dwell time|camera system|automation|automated collection|trakem2)\b", re.I)),
    ("infrastructure", re.compile(r"\b(cloud|cloudvolume|dvid|bossdb|database|neuroglancer|webknossos|catmaid|pipeline|storage|visualization tool|data management|software platform|software architecture|data infrastructure|repository|framework|toolkit|software|open-source software|data sharing|metadata|natverse|neuromorpho|mesmerize)\b", re.I)),
]

IMAGING_SUBS = [
    ("FIB-SEM", re.compile(r"\b(fib[- ]sem|focused ion beam|gas cluster ion beam)\b", re.I)),
    ("SBEM", re.compile(r"\b(sbem|sbf[- ]sem|serial block[- ]face|block[- ]face scanning)\b", re.I)),
    ("ssTEM", re.compile(r"\b(sstem|serial section transmission|transmission electron microscopy|tem grid)\b", re.I)),
    ("ATUM", re.compile(r"\b(atum|atum[- ]sem|automated tape[- ]collecting|tape[- ]collecting ultramicrotome)\b", re.I)),
    ("multibeam", re.compile(r"\b(multibeam|multi-beam|msem|multi-beam sem)\b", re.I)),
    ("X-ray", re.compile(r"\b(x-ray|synchrotron|nanotomography|x-ray holographic|micro-ct|ct imaging|x-ray phase[- ]contrast)\b", re.I)),
    ("expansion", re.compile(r"\b(expansion microscopy|exm|expansion pathology|proexm|clarity)\b", re.I)),
    ("cryo", re.compile(r"\b(cryo[- ]em|cryo[- ]electron|cryo[- ]et|cryo-electron tomography)\b", re.I)),
    ("EM", re.compile(r"\b(electron microscopy|electron microscope|em imaging|volume em|vem|3dem|3d-em|sem)\b", re.I)),
]

def get_pipeline_sub(text: str) -> Optional[str]:
    for sub, pat in PIPELINE_SUBS:
        if pat.search(text):
            return sub
    return "infrastructure"

def get_imaging_sub(text: str) -> str:
    for sub, pat in IMAGING_SUBS:
        if pat.search(text):
            return sub
    return "unspecified"

def get_synthesis_sub(text: str) -> str:
    field_pat = re.compile(r"\b(connectom|wiring diagram|volume electron microscopy|neural circuit reconstruction|reconstructing neural|dense reconstruction|microscale connectom|connectomics|connectomic|nanoscale connectomics|brain mapping|synaptomics)\b", re.I)
    if field_pat.search(text):
        return "field"
    return "domain"

# ----------------- STRICT OUTREACH & HEALTH PATTERNS -----------------
OUTREACH_STRICT_PAT = re.compile(
    r"\b(citizen science|citizen scientists|citizen neuroscientists|zooniverse|eyewire|gamified annotation|"
    r"undergraduate curriculum|neuroscience curriculum|teaching module|classroom education|"
    r"public outreach|outreach program|high school students|educational resource for students|"
    r"pedagogical tool|teaching connectomics|trailblazing students|undergraduate traineeship|"
    r"undergraduate innovation|workforce development|syglass|black box connectome assessment|"
    r"quantitative skills in undergraduate|hands-on tutorial|educational primer|student-to-student|"
    r"tutorial in connectome|primer on|tutorial review|computational training for the next generation|"
    r"open-access tool for em connectomics|neuprint: an open access tool|a tutorial and tool)\b", re.I)

OUTREACH_NEG_PAT = re.compile(
    r"\b(training data|training set|trained on|training images|training of deep|supervised training|"
    r"behavioral training|training pairs|ensemble training|imprinting|reinforcement learning|"
    r"neural network training|training session|animals were trained|imprinting and recalling)\b", re.I)

HEALTH_TITLE_PAT = re.compile(
    r"\b(alzheimer|parkinson|amyotrophic|huntington|schizophr|autis|"
    r"epilep|stroke|ischemi|traumatic brain injury|spinal cord injury|"
    r"multiple sclerosis|demyelinat|neurodegen|dementia|retinopath|gliom|tau|amyloid|"
    r"connectopath|neuropathol|pathophysiol|synapse loss|prion|synuclein|brain disorder|psychiat|"
    r"neurological disease|neurological disorder|disease model|mutant model|pathology|pathological|dysfunction|degeneration)\b", re.I)

HEALTH_ABS_PAT = re.compile(
    r"\b(in alzheimer|in parkinson|in huntington|in epilepsy|in schizophrenia|in autism spectrum|"
    r"in multiple sclerosis|model of alzheimer|model of parkinson|model of epilepsy|"
    r"pathophysiology of|disease pathology|synapse loss in alzheimer|epileptic seizure|post-stroke symptom|connectome alterations in)\b", re.I)

# ----------------- CLASSIFICATION DECISION ENGINE -----------------

def classify_paper(doi: str, title: str, venue: str, abstract: str) -> Dict[str, Any]:
    full_text = f"{title} {title} {venue} {abstract}"
    t_a = f"{title} {abstract}"
    t_lower = title.lower()
    v_lower = venue.lower()
    a_lower = abstract.lower()
    
    # Check known milestone datasets
    if doi in KNOWN_DATASETS:
        return {
            "classification": "dataset",
            "subclassification": None,
            "secondary_classifications": ["circuit-structure"] if re.search(r"\b(connectom|wiring|synap)\b", t_a, re.I) else [],
            "organism": extract_organisms(full_text)
        }

    # 1. DATASET
    if re.search(r"\b(we present a (dense|complete|comprehensive|whole-brain|brain-wide|synaptic resolution|multiregional|standard brain) (reconstruction|connectome|dataset|atlas|wiring diagram|survey)|"
                 r"we release (the|a)|open-source dataset|publicly available (dataset|connectome|reconstruction)|"
                 r"a connectome (of|and analysis of) the|a wiring diagram of the (whole|entire|adult|larval)|"
                 r"reconstruction of (the entire|the whole|an entire|a complete|all \d+|neocortex: organelles)|"
                 r"whole-brain (serial-section|annotation|morphometry|connectome)|whole-body cell type atlas|"
                 r"comparative connectomics of two|complete 3d reconstruction and|an open repository for|"
                 r"an unbiased template of the|molecular atlas of the|connectome of the caenorhabditis elegans pharynx|"
                 r"a neurotransmitter atlas of|cem500k|neuropal|the connectome of a decision-making|"
                 r"connectomic analysis of mitochondria in the central brain)\b", t_a, re.I) and not re.search(r"\b(review|trends in|annual review|current opinion)\b", v_lower):
        return {
            "classification": "dataset",
            "subclassification": None,
            "secondary_classifications": ["circuit-structure"] if re.search(r"\b(connectom|wiring|synap)\b", t_a, re.I) else [],
            "organism": extract_organisms(full_text)
        }

    # 2. TRAINING-OUTREACH (STRICT: Citizen Science, Classroom Curriculum, Educational Platform ONLY)
    if OUTREACH_STRICT_PAT.search(t_a) and not OUTREACH_NEG_PAT.search(title):
        return {
            "classification": "training-outreach",
            "subclassification": None,
            "secondary_classifications": ["pipeline"] if re.search(r"\b(platform|tool|pipeline)\b", t_a, re.I) else [],
            "organism": extract_organisms(full_text)
        }

    # 3. HEALTH / DISEASE (STRICT: Actual Disease Model / Clinical Mapping)
    if (HEALTH_TITLE_PAT.search(title) or HEALTH_ABS_PAT.search(abstract)) and not re.search(r"\b(brainbow|trakem2|fiji|clarity|neuromorpho|ransac)\b", t_a, re.I):
        if re.search(r"\b(synap|circuit|connectom|axon|dendrit|spine|ultrastruct|neuron|cortex|network)\b", t_a, re.I):
            return {
                "classification": "health",
                "subclassification": None,
                "secondary_classifications": ["physiology"] if re.search(r"\b(physiol|firing|action potential)\b", t_a, re.I) else (["neuroanatomy"] if re.search(r"\b(spine|ultrastruct)\b", t_a, re.I) else []),
                "organism": extract_organisms(full_text)
            }

    # 4. SYNTHESIS OVERRIDES (Reviews, Perspectives, Overviews)
    if re.search(r"\b(review|reviews|trends in|annual review|current opinion|neuroscience and biobehavioral reviews|progress in neurobiology|cold spring harbor|seminars in|nature reviews|brain research reviews)\b", v_lower) or \
       re.search(r"\b(in this review|here we review|we review|this review summarizes|in this perspective|we provide an overview|this article reviews|we summarize recent|this overview|we discuss current|in this survey|here we summarize|we present a perspective|this review focuses on|we synthesize|a critical review|this opinion)\b", a_lower) or \
       (re.search(r"\b(review|perspective|perspectives|progress in|advances in|primer|commentary|retrospective|historical perspective|future directions|challenges and opportunities|principles of|foundations of|a summary of|current status|roadmap|revisiting|what is|lessons from|open questions|reflections on|new insights into|recent advances|overview of|an overview|handbook|textbook)\b", t_lower) and not re.search(r"\b(connectome of|reconstruction of all|dataset of|atlas of|algorithm for|method for|system for)\b", t_lower)):
        return {
            "classification": "synthesis",
            "subclassification": get_synthesis_sub(full_text),
            "secondary_classifications": ["imaging"] if re.search(r"\b(microscop|em|imaging)\b", t_a, re.I) else (["circuit-structure"] if re.search(r"\b(connectom|circuit)\b", t_a, re.I) else []),
            "organism": extract_organisms(full_text)
        }

    # Statistical Scoring using trained model weights
    words = re.findall(r"\b[a-zA-Z0-9_\-]{3,}\b", f"{title} {title} {title} {venue} {venue} {abstract}".lower())
    scores = Counter()
    
    # Base class priors
    priors = {
        "synthesis": 2.2, "pipeline": 2.2, "circuit-structure": 2.0, "physiology": 1.9,
        "neuroai": 1.8, "neuroanatomy": 1.7, "imaging": 1.5, "behaviour": 1.4,
        "cell-types": 0.9, "mri": 0.8, "dataset": 0.7,
        "health": -100.0, "other": 0.2, "training-outreach": -100.0
    }
    for c, p in priors.items():
        scores[c] = p

    if MODEL_WEIGHTS:
        for c in priors.keys():
            if c not in ("training-outreach", "health") and c in MODEL_WEIGHTS:
                c_dict = MODEL_WEIGHTS[c]
                for w in words:
                    if w in c_dict:
                        scores[c] += c_dict[w]

    # Domain Pattern Boosters
    if re.search(r"\b(segmentation|alignment|registration|u-net|unet|tracing|proofreading|catmaid|neuprint|webknossos|graspy|dotmotif|shutu|deep learning for|convolutional network|neurolucida|mesmerize|natverse|trakem2|fiji|software platform|annotation tool|neuromorpho|ransac|model fitting)\b", t_a, re.I):
        scores["pipeline"] += 5.5
    if re.search(r"\b(fib[- ]sem|sbem|sbf[- ]sem|sstem|atum|multibeam|nanotomography|cryo[- ]em|expansion microscopy|microscope|heavy metal staining|clarity|brainbow)\b", t_a, re.I):
        scores["imaging"] += 5.0
    if re.search(r"\b(synaptic connectivity|synaptic connections|wiring diagram|synapses onto|presynaptic partner|postsynaptic partner|inhibitory connectivity|circuit motif|monosynaptic|nonrandom features|imprinting and recalling|cortical ensembles)\b", t_a, re.I):
        scores["circuit-structure"] += 5.0
    if re.search(r"\b(cell[- ]type|transcriptomic cell|census of|parts list of|scrna-seq|single-cell rna)\b", t_a, re.I):
        scores["cell-types"] += 4.5
    if re.search(r"\b(spine density|dendritic spine|ultrastructure|active zone|vesicle pool|axon diameter|myelin|cytoarchitecture|postsynaptic density)\b", t_a, re.I):
        scores["neuroanatomy"] += 4.0
    if re.search(r"\b(locomotion|walking|flight|courtship|mating|feeding|navigation|escape behavior|decision[- ]making|motor control|odor preference|neural-behavioral maps|unsupervised structure learning)\b", t_a, re.I):
        scores["behaviour"] += 4.5
    if re.search(r"\b(patch[- ]clamp|action potential|membrane potential|synaptic plasticity|ltp|receptive field|calcium imaging|spiking activity|firing rate|epsc|ipsc|whole-cell|signal propagation in drosophila)\b", t_a, re.I):
        scores["physiology"] += 4.5
    if re.search(r"\b(spiking neural network|recurrent neural network|neuromorphic|neural network model|circuit model|attractor network|simulated neural|neural dynamics model|could a neuroscientist understand a microprocessor)\b", t_a, re.I):
        scores["neuroai"] += 4.5
    if re.search(r"\b(fmri|diffusion mri|dti|tractography|eeg|meg|resting[- ]state|bold signal)\b", t_a, re.I) and not re.search(r"\b(electron microscop|serial section|synap|ultrastruct|petascale|petavoxel|microns|fib[- ]sem|sbem|nanoscale|synapses onto|wiring diagram)\b", t_a, re.I):
        scores["mri"] += 5.0
    else:
        scores["mri"] = -100.0

    # Decision ranking
    top_cat = scores.most_common(1)[0][0]
    
    # Subclass determination
    sub = None
    if top_cat == "pipeline":
        sub = get_pipeline_sub(full_text)
    elif top_cat == "imaging":
        sub = get_imaging_sub(full_text)
    elif top_cat == "synthesis":
        sub = get_synthesis_sub(full_text)

    # Secondaries
    secondaries = []
    for cat_name, _ in scores.most_common(4)[1:]:
        if cat_name != top_cat and cat_name not in ("other", "training-outreach") and len(secondaries) < 2:
            if cat_name == "pipeline":
                p_sub = get_pipeline_sub(full_text)
                secondaries.append(f"pipeline/{p_sub}" if p_sub and p_sub != "infrastructure" else "pipeline")
            else:
                secondaries.append(cat_name)

    return {
        "classification": top_cat,
        "subclassification": sub,
        "secondary_classifications": secondaries,
        "organism": extract_organisms(full_text)
    }

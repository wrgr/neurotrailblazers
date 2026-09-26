---
layout: page
title: "Journal Papers: NeuroAI & Computational Modeling"
permalink: /content-library/journal-papers/neuroai/
description: "Curated papers on the intersection of neuroscience and AI with summaries at beginner, intermediate, and advanced levels."
dimension: neuroai
tags:
  - neuroai:structure-function
  - neuroai:bio-inspired-architecture
  - neuroai:connectome-constrained-model
  - neuroai:deep-learning
  - neuroai:representation-learning
  - neuroai:simulation
use_layout_hero: false
content_type: core
---

# NeuroAI & Computational Modeling Journal Papers

Curated papers at the intersection of neuroscience and artificial intelligence — bio-inspired computation, connectome-constrained models, and the mutual contributions of AI and brain science. Each paper includes summaries at three expertise levels.

---

## 1. Zador et al. (2023) — Catalyzing Next-Generation Artificial Intelligence Through NeuroAI

**Citation:** Zador A, Escola S, Richards B, Ölveczky B, Bengio Y, Boahen K, et al. Catalyzing next-generation artificial intelligence through NeuroAI. *Nature Communications*. 2023;14:1597.
**DOI:** [10.1038/s41467-023-37180-x](https://doi.org/10.1038/s41467-023-37180-x)

**Tags:** `neuroai:bio-inspired-architecture` `neuroai:structure-function` `neuroai:connectome-constrained-model` `neuroai:deep-learning` `methodology:experimental-design`

### Summaries

**Beginner:** Artificial intelligence and brain science have been inspiring each other for decades — neural networks were originally inspired by how the brain works. This paper argues that the next breakthroughs in AI will come from studying the abilities all animals share, such as moving through and interacting with the physical world, rather than abilities that are uniquely human. It proposes a new benchmark, the "embodied Turing test", and a research program in NeuroAI to reach it.

**Intermediate:** Zador et al. present a community position paper arguing that investment in fundamental NeuroAI research is needed to accelerate AI. Its core proposal is the embodied Turing test: AI models of animals should interact with the sensorimotor world at skill levels comparable to their living counterparts. The emphasis shifts from capabilities such as game playing and language toward capabilities inherited over hundreds of millions of years of evolution and shared with all animals. Connectomics appears as one supporting resource: the paper points to detailed neural anatomy and connectomics, alongside large-scale neural recordings during behavior, as a roadmap for building AI systems that control virtual animals, and it cites the MICrONS project as an effort aimed at catalyzing new AI algorithms.

**Advanced:** Read the paper as an agenda, not as a connectomics argument; connectomes are mentioned briefly, as one data source among several. The connectomics-specific implications are left to the reader: if evolution has built useful inductive biases into circuits, connectome data is one place to look for them, and comparative data across species could show which circuit structures are conserved. Neither is demonstrated in the paper. The gap between having a connectome and knowing what computation a circuit performs — the structure-to-function problem — is the central challenge any such program has to address.

**Key figures:** The single figure contrasts the original Turing test with the proposed embodied Turing test. Read the paper for the argument.

**Discussion prompts:**
- What specific connectomics findings have already influenced AI architecture design?
- Is a connectome sufficient to infer computation, or do you also need dynamics?
- Which brain circuits are most likely to yield AI-relevant insights?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 2. Richards et al. (2019) — A Deep Learning Framework for Neuroscience

**Citation:** Richards BA, Lillicrap TP, Beaudoin P, Bengio Y, Bogacz R, Christensen A, et al. A deep learning framework for neuroscience. *Nature Neuroscience*. 2019;22(11):1761-1770.
**DOI:** [10.1038/s41593-019-0520-2](https://doi.org/10.1038/s41593-019-0520-2)

**Tags:** `neuroai:deep-learning` `neuroai:representation-learning` `neuroai:structure-function` `neuroai:bio-inspired-architecture` `methodology:experimental-design`

### Summaries

**Beginner:** Deep learning works well in AI, but does it have anything to teach us about how real brains work? This paper argues yes: deep learning provides a framework for understanding brains by showing how complex behaviors can emerge from learning objectives, network architectures, and learning rules. The key idea is that we should study brains the way we study deep networks — by asking what objective is being optimized and what architecture enables that optimization.

**Intermediate:** Richards et al. propose that neuroscience should adopt the "three components" framework of deep learning: (1) objective functions (what is the brain optimizing?), (2) learning rules (how are synaptic weights updated?), and (3) architectures (what network structures support the computation?). For each component, they discuss what is known from neuroscience and where deep learning provides useful hypotheses. The connectomics connection: brain architectures are not arbitrary but reflect evolutionary optimization, and connectome data can constrain models of neural computation by specifying the actual architecture available for learning.

**Advanced:** This paper gives one framework for connecting connectomics to computational neuroscience. The key argument is that architecture constrains what a network can learn — therefore, knowing the architecture (from connectomics) constrains the space of possible computations. However, architecture alone is not sufficient: you also need to know the learning rule and objective. The paper's discussion of "credit assignment" — how the brain solves the problem of determining which synapses should change — is directly relevant to interpreting connectivity patterns.

**Key figures:** Read it for the three-component framework (objective functions, learning rules, architectures) and how each maps onto neuroscience questions.

**Discussion prompts:**
- Which architectural features visible in connectomes map to known deep learning architecture choices?
- How should connectomics research be designed to test predictions from the deep learning framework?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Graph representations](/content-library/connectomics/graph-representations/)

---

## 3. Lillicrap et al. (2020) — Backpropagation and the Brain

**Citation:** Lillicrap TP, Santoro A, Marris L, Akerman CJ, Hinton G. Backpropagation and the brain. *Nature Reviews Neuroscience*. 2020;21(6):335-346.
**DOI:** [10.1038/s41583-020-0277-3](https://doi.org/10.1038/s41583-020-0277-3)

**Tags:** `neuroai:deep-learning` `neuroai:bio-inspired-architecture` `neuroai:structure-function` `neuroanatomy:synapse` `neuroanatomy:dendrite`

### Summaries

**Beginner:** The most successful learning algorithm in AI — backpropagation — requires information to flow backwards through a network, which seems biologically implausible because synapses in the brain are one-directional. This review discusses whether and how the brain might implement something like backpropagation. It explores biological mechanisms (feedback connections, dendritic computation, local learning signals) that could achieve similar results without the exact algorithm.

**Intermediate:** Lillicrap et al. review the "weight transport problem" in biological learning: backpropagation requires exact knowledge of forward weights at each layer, which seems biologically unavailable. They discuss proposed solutions: feedback alignment (random feedback weights work surprisingly well), target propagation (each layer has a local target), predictive coding (top-down predictions generate error signals), and dendritic computation (different dendritic compartments carry different signals). For connectomics, the key question is whether feedback connectivity revealed by connectome data is consistent with any of these proposed mechanisms.

**Advanced:** Read this before interpreting feedback connectivity in connectomics data. Predictions we can draw from it: (1) if feedback alignment is the mechanism, feedback connection patterns need not mirror feedforward patterns (testable with connectome data); (2) if predictive coding is the mechanism, feedback connections should target specific dendritic compartments (testable with compartment-level connectivity data); (3) the paper's discussion of dendritic computation is particularly relevant for compartment-level connectomics, where the distinction between perisomatic and apical inputs becomes functionally meaningful.

**Key figures:** Look for the treatment of the weight transport problem, feedback alignment, and dendritic mechanisms for carrying error signals.

**Discussion prompts:**
- Which proposed learning mechanisms make testable predictions about connectivity that connectomics could verify?
- Do the feedback pathways visible in cortical connectomes look like feedback alignment or predictive coding?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Dendrite biology](/content-library/neuroanatomy/dendrite-biology/)

---

## 4. Bassett, Zurn & Gold (2018) — On the Nature and Use of Models in Network Neuroscience

**Citation:** Bassett DS, Zurn P, Gold JI. On the nature and use of models in network neuroscience. *Nature Reviews Neuroscience*. 2018;19(9):566-578.
**DOI:** [10.1038/s41583-018-0038-8](https://doi.org/10.1038/s41583-018-0038-8)

**Tags:** `connectomics:graph-theory` `neuroai:connectome-constrained-model` `neuroai:simulation` `methodology:experimental-design` `methodology:statistical-analysis`

### Summaries

**Beginner:** When scientists build mathematical models of brain networks, they make many choices: which data to include, what simplifications to make, and what questions to ask. This review provides a framework for understanding these choices. It sorts network models by what they are built from and what they represent, and it asks what it takes to show that a model is valid: does it describe the data, explain a mechanism, or predict something new? Knowing which kind of validity your model has prevents overclaiming.

**Intermediate:** Bassett, Zurn, and Gold organize network models along three dimensions: from data representations to first-principles theory; from biophysical realism to functional phenomenology; and from elementary descriptions to coarse-grained approximations. They then set out validation principles, distinguishing descriptive, explanatory, and predictive validity, and emphasize perturbation-based approaches for probing function. For connectomics, the distinction matters directly: computing network measures (degree, modularity) is description; claiming that hub neurons are causally important for information processing is an explanatory claim and requires evidence beyond connectivity.

**Advanced:** This review is worth reading before publishing any connectomics analysis. Lessons that carry over to nanoscale connectomes: (1) graph measures describe topology, not function — a hub is a structural property; (2) the choice of null model determines what counts as "significant" structure; (3) descriptive, explanatory, and predictive validity are different achievements, and one does not imply another; (4) perturbation experiments and out-of-sample prediction on held-out network data are the tests that move a model beyond description. The three-dimensional classification is a useful checklist for stating what kind of model a paper builds and what kind of claim it supports.

**Key figures:** Fig. 1 (schematic of network models), Fig. 2 (the three dimensions of network model types), Fig. 3 (descriptive, explanatory and predictive validity), Fig. 4 (bridging model types)

**Discussion prompts:**
- Which published connectomics claims are descriptive versus explanatory?
- What evidence beyond the connectome is needed to claim that a network motif is functionally important?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Motif analysis](/content-library/connectomics/motif-analysis/)

---

## 5. Saxe et al. (2021) — If Deep Learning Is the Answer, What Is the Question?

**Citation:** Saxe A, Nelli S, Summerfield C. If deep learning is the answer, what is the question? *Nature Reviews Neuroscience*. 2021;22(1):55-67.
**DOI:** [10.1038/s41583-020-00395-8](https://doi.org/10.1038/s41583-020-00395-8)

**Tags:** `neuroai:deep-learning` `neuroai:representation-learning` `neuroai:structure-function` `neuroai:bio-inspired-architecture` `methodology:experimental-design`

### Summaries

**Beginner:** Deep networks learn to perform tasks from experience, and some researchers hope they can serve as theories of how brains perceive, think and act. This Perspective asks how neuroscientists should use deep networks as models of brains, and what can go wrong when a network is compared with a brain.

**Intermediate:** Saxe, Nelli and Summerfield offer a road map for systems neuroscience in the age of deep learning. They discuss the conceptual and methodological challenges of comparing behavior, learning dynamics and neural representations between artificial and biological systems, and the new research questions that machine learning has raised for neuroscience. For connectomics, the relevant point is ours rather than theirs: if model-brain comparisons are hard to interpret, measured architecture is one more constraint a model can be held to.

**Advanced:** One implication for connectome-constrained modeling: if a network with measured architecture and a network with arbitrary architecture produce equally brain-like representations, the comparison says little about the architecture's role. Treat a deep network as a hypothesis, and vary architecture, task and training to see which of them the brain-like behavior depends on.

**Key figures:** Read it for the argument about how to compare behavior, learning and representations between networks and brains.

**Discussion prompts:**
- How can connectome data strengthen deep learning models of brain computation?
- When two models with different architectures produce the same representations, what does this tell us?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 6. Barabási et al. (2023) — Neuroscience Needs Network Science

**Citation:** Barabási DL, Bianconi G, Bullmore E, Burgess M, Chung S, Eliassi-Rad T, et al. Neuroscience needs network science. *The Journal of Neuroscience*. 2023;43(34):5989-5995.
**DOI:** [10.1523/JNEUROSCI.1014-23.2023](https://doi.org/10.1523/JNEUROSCI.1014-23.2023)

**Tags:** `neuroai:structure-function` `neuroai:connectome-constrained-model` `connectomics:graph-theory` `connectomics:motif` `methodology:statistical-analysis`

### Summaries

**Beginner:** Once you have a complete wiring diagram, what do you do with it? Twenty authors from network science and neuroscience argue that the field needs shared theory, not just bigger datasets. Their case is that neuroscience keeps re-deriving ideas network science already has, and that the two communities need a common language before connectome data can answer the questions people want to ask of it.

**Intermediate:** This is a perspective piece arguing that connectome-scale data has outrun the theory available to interpret it. The authors set out where network science already has machinery neuroscience needs — multilayer and temporal networks, controllability, generative models, network comparison — and where neural circuits break the assumptions those tools were built on: signed and directed edges, spatial embedding, and the fact that a structural connection is not a functional one. The practical argument for a connectomics reader is that importing a graph statistic without importing its assumptions is how a result stops being checkable.

**Advanced:** The paper is best read as a map of the gap rather than a method. It identifies the specific mismatches between standard network-science measures and neural data — degree and clustering assume unsigned undirected edges; community detection assumes a resolution you must choose; most generative null models ignore the distance dependence that dominates cortical connectivity — and it names the areas where theory is genuinely missing rather than merely unapplied. For anyone running the analyses in Unit 09, the value is the explicit statement that the null model and the thresholding choice are theoretical commitments, not preprocessing.

**Key figures:** Read it for the argument rather than the figures; it is a perspective piece, not a results paper.

**Discussion prompts:**
- Which network-science measures in your own analysis carry assumptions your connectome violates, and what would it take to check?
- The authors argue theory is the bottleneck rather than data. Is that true for the question you are working on?
- Where does a network-science framing actively mislead about a neural circuit?

**Related content:** [Network analysis methods](/content-library/connectomics/network-analysis-methods/), [Motif analysis](/content-library/connectomics/motif-analysis/), [Graph representations](/content-library/connectomics/graph-representations/)

---

## 7. Conwell et al. (2024) — A Large-Scale Examination of Inductive Biases Shaping High-Level Visual Representation in Brains and Machines

**Citation:** Conwell C, Prince JS, Kay KN, Alvarez GA, Konkle T. A large-scale examination of inductive biases shaping high-level visual representation in brains and machines. *Nature Communications*. 2024;15:9383. (Preprint title: "What can 1.8 billion regressions tell us about the pressures shaping high-level visual representation in brains and machines?" *bioRxiv* 2022.03.28.485868.)
**DOI:** [10.1038/s41467-024-53147-y](https://doi.org/10.1038/s41467-024-53147-y)

**Tags:** `neuroai:structure-function` `neuroai:deep-learning` `neuroai:representation-learning` `case-studies:human`

### Summaries

**Beginner:** Which artificial neural networks produce internal representations most similar to those found in real brains? This study ran a large controlled comparison, more than 1.8 billion regressions, testing how well the internal activity of 224 different vision models predicts human brain responses to natural images. The answer was that architecture and training objective mattered less than expected; the images the model was trained on mattered most.

**Intermediate:** Conwell et al. compare 224 diverse vision models against human fMRI responses in occipitotemporal cortex from the 7T Natural Scenes Dataset, using two model-to-brain linking methods (regression-based encoding and representational similarity analysis). By holding other factors constant, they isolate the effect of individual model properties. Models with qualitatively different architectures (for example, CNNs versus Transformers) and different task objectives (for example, purely visual contrastive learning versus vision-language alignment) reach nearly equivalent brain predictivity. Variation in the visual training diet has the largest and most consistent effect.

**Advanced:** The paper's most important methodological point is a warning: many models reach similarly high brain predictivity despite clear differences in their underlying representations, which suggests the standard model-to-brain linking methods may be too flexible to discriminate between hypotheses. For the connectomics-NeuroAI intersection, that has two implications. First, a finding that an architecture predicts neural responses well is weak evidence that the architecture is brain-like, because architecture had little effect when other factors were controlled. Second, connectome-constrained models may need benchmarks that are more discriminating than response predictivity alone — for example, predictions about specific cell types, connections, or perturbations.

**Key figures:** Look for the controlled comparisons of architecture, task objective, and training data, and the comparison of the two linking methods.

**Discussion prompts:**
- How should connectome-constrained architectures be evaluated if response predictivity cannot distinguish between architectures?
- If training data matters more than architecture for brain predictivity, what does that imply about what connectome data can and cannot constrain?
- Is predicting neural activity a sufficient benchmark for a "good" brain model?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 8. Lappalainen et al. (2024) — Connectome-Constrained Networks Predict Neural Activity Across the Fly Visual System

**Citation:** Lappalainen JK, Tschopp FD, Prakhya S, McGill M, Nern A, Shinomiya K, Takemura S, Gruntman E, Macke JH, Turaga SC. Connectome-constrained networks predict neural activity across the fly visual system. *Nature*. 2024;634:1132-1140.
**DOI:** [10.1038/s41586-024-07939-3](https://doi.org/10.1038/s41586-024-07939-3)

**Tags:** `neuroai:connectome-constrained-model` `neuroai:structure-function` `neuroai:simulation` `case-studies:Drosophila`

### Summaries

**Beginner:** If you know how the neurons in a circuit are connected, can you predict what they will do? This paper takes the measured wiring of the motion-detection pathways in the fruit fly's visual system and builds a computer model with the same connections. The model was never trained on recordings from real neurons — only on a visual task — yet its neurons behaved much like the real ones measured in earlier experiments.

**Intermediate:** Lappalainen et al. build a model network with the experimentally determined connectivity of 64 cell types in the motion pathways of the fly optic lobe. Connectivity is fixed by the connectome; the single-neuron and single-synapse parameters, which the connectome does not measure, are left unknown and optimized with deep-learning methods so that the network detects visual motion. The resulting model makes experimentally testable predictions for every neuron in the connectome, and those predictions agreed with measured neural activity reported across 26 studies.

**Advanced:** This paper shows that connectivity alone can constrain a mechanistic model enough to predict neural activity. The connectome does not supply a simulation; it removes enough free parameters that the model's predictions can fail. Two methodological choices deserve close reading. First, the parameters are fit to a task rather than to the neural data being predicted, so agreement with recordings is a genuine held-out test rather than a fit. Second, many parameter settings can solve the task, so the authors examine an ensemble of trained models and ask which predictions are consistent across it. The authors also report that the strategy is more likely to succeed when neurons are sparsely connected. The scope is limited: a small, stereotyped, well-characterized visual circuit with a known computational task. Whether the approach extends to mammalian cortex, where the task is less clear and the connectome less complete, is open.

**Key figures:** Look for the construction of the model from the connectome, the task-optimized training, the comparison of predicted and measured responses, and the analysis of variability across the model ensemble.

**Discussion prompts:**
- Which parameters does the connectome fix, and which remain free? Why does that ratio determine whether the model is falsifiable?
- Why does training on a task rather than on recordings make the comparison with neural data more convincing?
- What properties of the fly visual system made this work, and which of them does mouse cortex lack?
- How should this approach scale to larger connectomes (mouse, human), where the relevant task is less well defined?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Network analysis papers](/content-library/journal-papers/network-analysis/), [Unit 09 §5](/technical-training/09-connectome-analysis-neuroai/)

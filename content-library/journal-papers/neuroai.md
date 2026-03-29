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
---

# NeuroAI & Computational Modeling Journal Papers

Curated papers at the intersection of neuroscience and artificial intelligence — bio-inspired computation, connectome-constrained models, and the mutual contributions of AI and brain science. Each paper includes summaries at three expertise levels.

---

## 1. Zador et al. (2023) — Catalyzing Next-Generation Artificial Intelligence Through NeuroAI

**Citation:** Zador A, Escola S, Richards B, Olveczky B, Bhaya Y, Boahen K, et al. Catalyzing next-generation artificial intelligence through NeuroAI. *Nature Communications*. 2023;14:1597.
**DOI:** [10.1038/s41467-023-37180-x](https://doi.org/10.1038/s41467-023-37180-x)

**Tags:** `neuroai:bio-inspired-architecture` `neuroai:structure-function` `neuroai:connectome-constrained-model` `neuroai:deep-learning` `methodology:experimental-design`

### Summaries

**Beginner:** Artificial intelligence and brain science have been inspiring each other for decades — neural networks were originally inspired by how the brain works. This paper argues that a deeper understanding of brain wiring (from connectomics) and brain computation could spark the next breakthroughs in AI. It outlines a research agenda where neuroscience data, including connectomes, directly informs the design of new AI systems.

**Intermediate:** Zador et al. present a community position paper arguing that neuroscience — particularly connectomics, developmental neurobiology, and systems neuroscience — should play a central role in developing next-generation AI. They identify specific areas where brain data can inform AI design: innate circuit architectures (wiring present at birth that encodes evolutionary priors), learning rules (synaptic plasticity mechanisms that differ from backpropagation), and embodied computation (how brains interact with bodies and environments). The paper identifies connectomics as a key enabling technology for understanding innate circuit structure.

**Advanced:** The paper's connectomics-specific arguments are: (1) connectome data can reveal architectural motifs that encode useful inductive biases, potentially replacing hand-designed neural network architectures; (2) comparative connectomics across species can identify conserved circuit structures that represent convergent solutions to computational problems; (3) developmental connectomics can reveal how self-organizing rules generate functional circuits, suggesting alternatives to end-to-end learning. The paper acknowledges the gap between having connectome data and understanding what computations a circuit performs — this "structure-to-function" mapping problem is the central challenge.

**Key figures:** Fig. 1 (NeuroAI research agenda), Fig. 2 (levels of biological inspiration), Fig. 3 (connectome-to-computation pipeline)

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

**Beginner:** Deep learning has been remarkably successful in AI, but does it have anything to teach us about how real brains work? This paper argues yes: deep learning provides a framework for understanding brains by showing how complex behaviors can emerge from learning objectives, network architectures, and learning rules. The key idea is that we should study brains the way we study deep networks — by asking what objective is being optimized and what architecture enables that optimization.

**Intermediate:** Richards et al. propose that neuroscience should adopt the "three components" framework of deep learning: (1) objective functions (what is the brain optimizing?), (2) learning rules (how are synaptic weights updated?), and (3) architectures (what network structures support the computation?). For each component, they discuss what is known from neuroscience and where deep learning provides useful hypotheses. The connectomics connection: brain architectures are not arbitrary but reflect evolutionary optimization, and connectome data can constrain models of neural computation by specifying the actual architecture available for learning.

**Advanced:** This paper provides the theoretical framework that connects connectomics to computational neuroscience. The key argument is that architecture constrains what a network can learn — therefore, knowing the architecture (from connectomics) constrains the space of possible computations. However, architecture alone is not sufficient: you also need to know the learning rule and objective. The paper's discussion of "credit assignment" — how the brain solves the problem of determining which synapses should change — is directly relevant to interpreting connectivity patterns.

**Key figures:** Fig. 1 (three-component framework), Fig. 2 (architecture-computation relationship), Fig. 3 (biological learning rules)

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

**Advanced:** This review is essential for interpreting feedback connectivity in connectomics data. Key testable predictions: (1) if feedback alignment is the mechanism, feedback connection patterns need not mirror feedforward patterns (testable with connectome data); (2) if predictive coding is the mechanism, feedback connections should target specific dendritic compartments (testable with compartment-level connectivity data); (3) the paper's discussion of dendritic computation is particularly relevant for compartment-level connectomics, where the distinction between perisomatic and apical inputs becomes functionally meaningful.

**Key figures:** Fig. 1 (weight transport problem), Fig. 2 (feedback alignment), Fig. 3 (dendritic error computation), Fig. 4 (biological credit assignment)

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

**Beginner:** When scientists build mathematical models of brain networks, they make many choices: which data to include, what simplifications to make, and what questions to ask. This review provides a philosophical framework for understanding these choices. It distinguishes between models that describe data (what does the network look like?), models that predict outcomes (what will happen?), and models that explain mechanisms (why does the network work?). Knowing which type you are building prevents overclaiming.

**Intermediate:** Bassett, Zurn, and Gold provide a taxonomy of models in network neuroscience: descriptive (summarizing data), explanatory (identifying mechanisms), and predictive (forecasting outcomes). They argue that most network analyses in neuroscience are descriptive but are sometimes presented as explanatory. For connectomics, this framework is essential: computing network measures (degree, modularity) is descriptive; claiming that hub neurons are causally important for information processing is explanatory and requires additional evidence beyond connectivity.

**Advanced:** This review should be required reading before publishing any connectomics analysis paper. Key arguments: (1) graph measures describe topology, not function — a hub is a structural property; (2) the choice of null model determines what counts as "significant" structure; (3) predictive models provide stronger evidence than descriptive models but still do not establish mechanism; (4) connectome-constrained models that reproduce dynamics observed in functional data provide the strongest evidence for structure-function relationships. The paper's call for explicit statement of model type and evidentiary claims is a useful checklist for peer review.

**Key figures:** Fig. 1 (model taxonomy), Fig. 2 (descriptive vs. explanatory), Fig. 3 (prediction vs. mechanism)

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

**Beginner:** Deep learning networks can match human performance on many tasks, and their internal representations look surprisingly similar to brain activity patterns. Does this mean deep networks are good models of the brain? This review argues: not necessarily. Networks trained on different tasks with different architectures can produce similar representations, making it hard to determine which aspects of the model are actually brain-like.

**Intermediate:** Saxe et al. critically examine the practice of using task-trained deep networks as models of brain computation. They identify a key problem: representational similarity between model and brain does not uniquely identify the computational mechanism, because many different models can produce similar representations. They advocate for stronger tests: comparing across architectures, tasks, and training regimes to identify which factors are necessary for brain-like representations. For connectomics, this implies that architecture-specific predictions (from connectome data) could provide stronger constraints than representation-level comparisons alone.

**Advanced:** The paper's argument has direct implications for connectome-constrained modeling: if you train a network with brain-like architecture (from connectome data) and it produces brain-like representations, this is stronger evidence for the architecture's computational role than if an arbitrary architecture produces the same representations. The key methodological contribution is a framework for "strong inference" with deep learning models: systematically varying architecture, task, and training to identify the minimal factors that produce brain-like computation.

**Key figures:** Fig. 1 (representational similarity analysis), Fig. 2 (multiple models problem), Fig. 3 (strong inference framework)

**Discussion prompts:**
- How can connectome data strengthen deep learning models of brain computation?
- When two models with different architectures produce the same representations, what does this tell us?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 6. Eckstein et al. (2024) — Neuroscience Needs Network Ecology

**Citation:** Eckstein N, Bates AS, Champion A, Du M, Yin Y, Schlegel P, et al. Neuroscience needs network ecology. *Neuron*. 2024;112(9):1397-1408.
**DOI:** [10.1016/j.neuron.2024.03.008](https://doi.org/10.1016/j.neuron.2024.03.008)

**Tags:** `neuroai:structure-function` `neuroai:connectome-constrained-model` `connectomics:graph-theory` `connectomics:motif` `methodology:statistical-analysis` `case-studies:Drosophila`

### Summaries

**Beginner:** Having a complete brain wiring diagram is incredible, but what do you actually do with it? This paper argues that neuroscience needs tools from "network ecology" — the study of complex interaction networks in ecosystems — to make sense of connectome data. Just as ecologists study food webs (who eats whom), neuroscientists should study connectomes using frameworks that account for the asymmetric, hierarchical nature of neural circuits.

**Intermediate:** Eckstein et al. argue that standard connectomics analysis tools (from network science and social networks) miss important biological structure. They advocate for approaches from network ecology that handle: asymmetric interactions (excitatory versus inhibitory), hierarchical organization, spatial embedding, and multi-scale structure simultaneously. Applied to the *Drosophila* connectome, they show that ecological network tools reveal circuit organization that standard graph measures miss, including trophic level analysis (information processing depth) and interaction strength distributions.

**Advanced:** The core argument is that generic graph-theoretic measures (degree, clustering, modularity) are not biologically informed enough for neural circuits. The ecological tools they advocate handle: (1) signed, weighted, directed graphs natively; (2) the distinction between processing hierarchies and recurrent loops; (3) asymmetries where connectivity meaning depends on cell type. The trophic analysis framework provides a continuous "processing depth" measure that outperforms community-detection-based layer assignment. This approach complements Winding et al.'s spectral signal flow analysis.

**Key figures:** Fig. 1 (network ecology parallels), Fig. 2 (trophic level analysis), Fig. 3 (interaction strength), Fig. 4 (comparison with standard graph measures)

**Discussion prompts:**
- Which ecological network concepts translate directly to neural circuits, and which require adaptation?
- How do signed (excitatory/inhibitory) analyses change conclusions compared with unsigned analyses?

**Related content:** [Network analysis methods](/content-library/connectomics/network-analysis-methods/), [Motif analysis](/content-library/connectomics/motif-analysis/), [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/)

---

## 7. Conwell et al. (2024) — What Can 1.8 Billion Regressions Tell Us About the Pressures Shaping High-Level Visual Representation in Brains and Machines?

**Citation:** Conwell C, Prince JS, Kay KN, Alvarez GA, Konkle T. What can 1.8 billion regressions tell us about the pressures shaping high-level visual representation in brains and machines? *bioRxiv/NeurIPS*. 2024.

**Tags:** `neuroai:structure-function` `neuroai:deep-learning` `neuroai:representation-learning` `case-studies:mouse` `case-studies:human`

### Summaries

**Beginner:** Which artificial neural networks produce internal representations most similar to those found in real brains? This study ran a massive comparison — 1.8 billion regressions — testing how well the internal activity of hundreds of different AI models predicts brain activity in both humans and mice viewing images. The results reveal which design choices (network architecture, training data, training objective) matter most for producing brain-like representations.

**Intermediate:** Conwell et al. conduct the largest systematic comparison to date of neural network representations with neural data from both human fMRI and mouse calcium imaging. By varying model architecture, training objective, dataset, and other factors across hundreds of models, they identify the key pressures that shape brain-like representations. Key findings include: training on naturalistic tasks (object recognition, self-supervised learning) produces more brain-predictive representations than arbitrary tasks; scale alone does not guarantee brain-likeness; and the factors predicting human neural responses partially diverge from those predicting mouse responses, reflecting species-specific computational strategies.

**Advanced:** This paper provides the most comprehensive empirical answer to date on what makes a neural network a good model of visual cortex. The methodological contribution is a factorial analysis across model design axes: architecture family (CNNs, Transformers, MLPs), training paradigm (supervised, self-supervised, language-supervised), dataset scale and composition, and model scale. The regression framework maps model layers to neural data using ridge regression with cross-validation. Key findings for the connectomics-NeuroAI intersection: (1) architecture matters — models with more brain-like connectivity patterns (e.g., recurrent, hierarchical) tend to predict neural data better; (2) the human-mouse divergence in model predictivity suggests species-specific architectural constraints shape representation; (3) the diminishing returns of scale challenge purely scaling-based approaches to brain modeling.

**Key figures:** Fig. 1 (regression framework), Fig. 2 (model factor analysis), Fig. 3 (architecture effects), Fig. 4 (human vs. mouse divergence)

**Discussion prompts:**
- How should connectome-constrained architectures be evaluated in this regression framework?
- What does the human-mouse divergence in model predictivity tell us about cross-species connectomic differences?
- Is predicting neural activity a sufficient benchmark for a "good" brain model?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [Network analysis methods](/content-library/connectomics/network-analysis-methods/)

---

## 8. Lappalainen et al. (2024) — Connectome-Constrained Networks Predict Neural Activity Across the Fly Brain

**Citation:** Lappalainen JK, Tschopp FD, Varber S, Dasgupta M, Clandinin TR, Romani S, et al. Connectome-constrained networks predict neural activity across the fly brain. *Nature*. 2024.
**DOI:** [10.1038/s41586-024-07939-3](https://doi.org/10.1038/s41586-024-07939-3)

**Tags:** `neuroai:connectome-constrained-model` `neuroai:structure-function` `neuroai:simulation` `case-studies:Drosophila` `case-studies:FlyWire`

### Summaries

**Beginner:** If you know how all the neurons in a brain are connected, can you predict what they will do? This paper takes the complete wiring diagram of the fruit fly brain (from the FlyWire connectome) and uses it to build an artificial neural network with the same connection pattern. When they trained this network, it could predict real neural activity recorded from living flies. This is the first demonstration that a connectome-constrained model can predict brain dynamics at a whole-brain scale.

**Intermediate:** Lappalainen et al. construct a neural network model whose architecture is directly derived from the FlyWire connectome — neurons in the model correspond to real neurons, and connections exist only where the connectome specifies them. The model is trained to predict neural activity recorded via calcium imaging in behaving *Drosophila*. Key findings: the connectome-constrained model outperforms randomly wired models with matched statistics, demonstrating that the specific wiring pattern carries computational information. The model also generates predictions about the activity of unrecorded neurons, effectively completing the brain-wide activity map.

**Advanced:** This paper is the first rigorous demonstration that connectome structure constrains neural dynamics in a predictive, quantitative sense. The modeling framework uses the connectome as a hard architectural constraint (only connectome-specified connections are allowed) while learning synaptic weights from functional data. Key methodological choices: (1) the model uses a continuous-time recurrent architecture with Dale's law (separate excitatory/inhibitory neurons); (2) training uses a combination of reconstruction loss on recorded neurons and regularization; (3) comparison with shuffled-connectome controls isolates the contribution of specific wiring. The results validate the central premise of connectome-constrained modeling: that wiring diagrams contain functionally relevant information beyond what is captured by aggregate statistics. Limitations include the gap between synapse count and effective synaptic strength, and the absence of neuromodulation.

**Key figures:** Fig. 1 (connectome-to-model pipeline), Fig. 2 (prediction of neural activity), Fig. 3 (comparison with shuffled controls), Fig. 4 (whole-brain activity prediction)

**Discussion prompts:**
- What fraction of neural dynamics is explained by connectome structure versus other factors (neuromodulation, plasticity)?
- How should this approach scale to larger connectomes (mouse, human)?
- Does the success of connectome-constrained models validate the "structure determines function" hypothesis?

**Related content:** [NeuroAI bridge](/content-library/connectomics/neuroai-bridge/), [FlyWire whole-brain](/content-library/case-studies/flywire-whole-brain/)

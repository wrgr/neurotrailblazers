---
layout: dataset
title: "Accessing Public EM Datasets"
description: "Resources and notebooks for downloading and exploring connectomics data."
---

<div class="main-content">

# Getting Started with EM Connectomics Datasets

A guide to resources and example notebooks for accessing major public Electron Microscopy (EM) connectomics datasets.

---

## 🧠 Google Research (FAFB & H01)

Google's connectomics team has released several landmark datasets, most famously a large volume of the fly brain (FAFB) and a cubic millimeter of human cerebral cortex (H01). The primary tool for programmatic access is **CAVEclient**.

* **Key Datasets:**
    * **FAFB (FlyWired):** A full adult female *Drosophila* brain.
    * **H01 (Human):** A 1 mm³ sample of human temporal lobe cortex.
* **Primary Tool:** `caveclient`
* **Resources & Notebooks:** The official documentation and tutorials are the best place to start. They are designed as Jupyter notebooks you can run directly in Google Colab.

    1.  **Installation:**
        ```bash
        pip install caveclient
        ```

    2.  **Example Notebooks 📓:**
        * **CAVEclient Basics:** This is the best starting point. It covers connecting to a dataset, finding neurons, and querying their properties (synapses, locations, etc.).
            * [**Run the "Introduction to CAVE" Tutorial in Colab**](https://colab.research.google.com/github/seung-lab/PyChunkedGraph/blob/master/notebooks/Introduction%20to%20CAVE.ipynb)
        * **Advanced Queries:** Once you're comfortable, this notebook shows how to perform more complex queries, like finding all the inputs to a specific neuron compartment.
            * [**Run the "Queries" Tutorial in Colab**](https://colab.research.google.com/github/seung-lab/PyChunkedGraph/blob/master/notebooks/Queries.ipynb)

---

## 🐭 Allen Institute for Brain Science (MICrONS)

The Allen Institute's MICrONS project produced a cubic millimeter dataset from the mouse visual cortex, complete with functional imaging data for many neurons. Access is typically through the **AllenSDK**.

* **Key Dataset:** A 1 mm³ volume of mouse primary visual cortex.
* **Primary Tool:** `allensdk`
* **Resources & Notebooks:** The Allen Institute provides excellent documentation and tutorials for accessing the MICrONS data.

    1.  **Installation:**
        ```bash
        pip install allensdk
        ```

    2.  **Example Notebooks 📓:**
        * **MICrONS Data Access:** This notebook walks you through the entire process: finding cells, downloading synapse data, and retrieving the 3D mesh of a neuron. It's the most comprehensive starting point.
            * [**Official MICrONS Tutorial on GitHub**](https://github.com/AllenInstitute/MicronsBinder/blob/main/notebooks/intro_to_microns_data.ipynb)
        * **Visualizing Meshes:** This notebook shows how to take the data you've queried and visualize it in 3D.
            * [**Working with Mesh Data Tutorial**](https://github.com/AllenInstitute/MicronsBinder/blob/main/notebooks/meshing.ipynb)

---

## 🪰 Janelia Research Campus / HHMI (Hemibrain)

Janelia's FlyEM team produced the "hemibrain" dataset, a dense reconstruction of a large portion of the central fly brain. It's one of the most complete and widely used connectomes. Data is most easily accessed via the **neuPrint** service and its Python client.

* **Key Dataset:** Hemibrain (a large portion of the *Drosophila* central brain)
* **Primary Tool:** `neuprint-python`
* **Resources & Notebooks:** The neuPrint ecosystem is very user-friendly, with many examples available.

    1.  **Installation:**
        ```bash
        pip install neuprint-python
        ```

    2.  **Example Notebooks 📓:**
        * **neuPrint Starter Guide:** This is the official "getting started" notebook. You'll learn how to connect to the server, find neurons by name or type, and fetch their connectivity. You will need to get a free authentication token from the [neuPrint website](https://neuprint.janelia.org/).
            * [**neuPrint Python Tutorial on GitHub**](https://github.com/connectome-neuprint/neuprint-python/blob/master/notebooks/Neuprint_Tutorial.ipynb)
        * **Common Recipes:** This notebook provides solutions for common analysis tasks, such as finding paths between neurons or identifying the strongest inputs to a cell.
            * [**neuPrint Recipes Notebook**](https://github.com/connectome-neuprint/neuprint-python/blob/master/notebooks/Neuprint_Recipes.ipynb)

---

## 💾 bossDB (Multiple Datasets)

The Brain Observatory Storage Service & Database (bossDB) from Johns Hopkins APL is a repository for multiple large-scale neuroscience datasets, including several EM volumes. It has its own Python library for access.

* **Key Datasets:** Includes data from the IARPA MICrONS program, mouse cortex data (e.g., Kasthuri15), and others.
* **Primary Tool:** `intern` (the bossDB Python client)
* **Resources & Notebooks:** The bossDB team provides tutorials showing how to access and download cutouts (small volumes) of data.

    1.  **Installation:**
        ```bash
        pip install intern
        ```

    2.  **Example Notebooks 📓:**
        * **Getting Started with bossDB:** This notebook covers the authentication process, finding data, and downloading a small cutout of EM data.
            * [**bossDB cutout example on GitHub**](https://github.com/jhuapl-boss/intern/blob/master/notebooks/Boss_cutout_example.ipynb)

---

## 🚀 General Tools & Visualization

Once you have the data, you need to see it!

* **Neuroglancer:** This is the standard in-browser viewer for volumetric data. Most of the tutorials above will generate Neuroglancer links to let you instantly see the neurons or synapses you've queried in 3D.
* **Napari:** For more powerful, local visualization and analysis, [Napari](https://napari.org/) is a fantastic Python-based viewer. It's great for overlaying synapse locations on neuron meshes or viewing raw EM imagery you've downloaded.

</div>

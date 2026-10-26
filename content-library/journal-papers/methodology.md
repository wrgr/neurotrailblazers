---
layout: page
title: "How the paper collection is maintained"
permalink: /content-library/journal-papers/methodology/
description: "The distinction between bibliographic discovery, navigational tags, and source-checked scientific contributions."
use_layout_hero: false
content_type: core
---

# How the paper collection is maintained

## Discovery is not scientific verification

The corpus contains {{ site.data.journal_papers.papers.size }} publication records. It was assembled through literature retrieval and category-based selection. Coverage and selection are incomplete: the distribution of papers in this collection must not be interpreted as the distribution of research in the field.

Topic, organism, and network-role labels are aids to navigation, not evidence that a publication used a particular dataset, implemented a method, achieved an outcome, or belongs to a consortium. Labels may be wrong. The 500- and 1,000-paper subsets retain historical selection rules; they do not certify papers as landmarks or rank their scientific quality.

## Evidence before a contribution note

A public contribution note requires a matching digital object identifier (DOI), a source-checked status, a specific contribution and reported result, its test context, its limitations, a source URL and location, the evidence basis, and the checker and date. Without this record, the site shows the publication metadata and abstract without inventing a summary.

The checking basis is visible. An AI-assisted check of an abstract is not an expert assessment or independent replication. Notes should report what the source supports, including null results and limitations where relevant, rather than manufacture a positive outcome for every publication.

## What changed

Earlier category-based templates produced publication-specific-looking statements without publication-specific support. That approach was inappropriate for research evidence. Those generators are retired, and their output is not used in public cards, graph search, review prompts, or corpus downloads. Historical input files remain in the source repository for traceability, not as verified scientific annotations.

## Citation relationships

Directed links represent recorded references among papers in this corpus. The displayed neighborhood counts are resolved within this corpus. Imported degree and network-role fields have a different scope and are not claims of importance, agreement, or successful method transfer. Bibliographic and citation metadata still require independent source review; mechanical consistency does not establish their truth.

## Downloads and reuse

[Return to the corpus hub]({{ '/content-library/journal-papers/' | relative_url }}) for nested downloads. Schema version 2 excludes legacy generated annotations and preserves bibliography, abstracts, recorded citations, navigation labels, and source-checked contribution notes where available. Review prompts explicitly require source access, reported evidence, test context and limitations; a list of titles is not sufficient evidence for a scientific synthesis.

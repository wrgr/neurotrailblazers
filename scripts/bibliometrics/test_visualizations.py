#!/usr/bin/env python3
"""
Test suite for visualization and data generation scripts.

Validates:
1. Data file integrity and completeness
2. HTML generation correctness
3. Embedded data in visualizations
4. Author/paper counts consistency
"""
import json
import re
from pathlib import Path


class TestDataIntegrity:
    """Test that data files have expected content."""

    def test_corpus_has_papers(self):
        """Corpus should have papers with required fields."""
        with open(Path("output/corpus_kcore_25.json")) as f:
            corpus = json.load(f)

        assert isinstance(corpus, list), "Corpus should be a list"
        assert len(corpus) > 0, "Corpus should not be empty"

        # Check first paper has required fields
        paper = corpus[0]
        assert "openalex_id" in paper, "Paper should have openalex_id"
        assert "title" in paper, "Paper should have title"
        assert "year" in paper, "Paper should have year"
        assert "cited_by_count" in paper, "Paper should have cited_by_count"
        assert "referenced_works" in paper, "Paper should have referenced_works"

        print(f"✓ Corpus has {len(corpus)} papers with required fields")

    def test_author_rankings_completeness(self):
        """Author rankings should have paper_count for all authors."""
        with open(Path("output/author_rankings.json")) as f:
            authors = json.load(f)

        assert len(authors) > 100, "Should have many authors"

        # Check all authors have paper_count
        missing_counts = [a for a in authors if "paper_count" not in a]
        assert len(missing_counts) == 0, f"{len(missing_counts)} authors missing paper_count"

        print(f"✓ Author rankings: {len(authors)} authors, all have paper_count")

    def test_lineage_data_generation(self):
        """Lineage data should have all papers with generation info."""
        with open(Path("../../assets/analysis/lineage_data.json")) as f:
            lineage = json.load(f)

        assert "nodes" in lineage, "Should have nodes"
        assert "links" in lineage, "Should have links"
        assert len(lineage["nodes"]) == 1064, "Should have 1064 core papers"
        assert len(lineage["links"]) > 20000, "Should have many citation links"

        # Check all nodes have generation
        missing_gen = [n for n in lineage["nodes"] if "generation" not in n]
        assert len(missing_gen) == 0, f"{len(missing_gen)} nodes missing generation"

        print(f"✓ Lineage data: {len(lineage['nodes'])} nodes, {len(lineage['links'])} links")

    def test_metadata_accuracy(self):
        """Metadata should match actual data counts."""
        with open(Path("../../assets/analysis/lineage_data.json")) as f:
            lineage = json.load(f)

        meta = lineage["metadata"]
        assert meta["total_papers"] == len(lineage["nodes"]), "Paper count mismatch"
        assert meta["total_citations"] == len(lineage["links"]), "Citation count mismatch"

        print(f"✓ Metadata accurate: {meta['total_papers']} papers, {meta['total_citations']} citations")


class TestHTMLGeneration:
    """Test HTML visualization generation."""

    def test_field_map_has_authors(self):
        """Field map HTML should embed all authors."""
        with open(Path("../../assets/analysis/field_map.html")) as f:
            content = f.read()

        # Find authorRankings array
        match = re.search(r'const authorRankings = (\[.*?\]);', content, re.DOTALL)
        assert match, "authorRankings not found in field_map.html"

        try:
            authors = json.loads(match.group(1))
            assert len(authors) > 100, f"Should have many authors, got {len(authors)}"
            assert len(authors) == 35641, f"Should have all 35641 authors, got {len(authors)}"

            # Spot check first author has required fields
            assert "name" in authors[0], "Author missing name"
            assert "paper_count" in authors[0], "Author missing paper_count"

            print(f"✓ Field map embedded: {len(authors)} authors")
        except json.JSONDecodeError as e:
            raise AssertionError(f"Invalid JSON in authorRankings: {e}")

    def test_field_map_has_papers(self):
        """Field map HTML should embed citation data."""
        with open(Path("../../assets/analysis/field_map.html")) as f:
            content = f.read()

        # Find citationData
        match = re.search(r'const citationData = (\{.*?\});', content, re.DOTALL)
        assert match, "citationData not found in field_map.html"

        try:
            data = json.loads(match.group(1))
            assert "nodes" in data, "citationData missing nodes"
            assert "links" in data, "citationData missing links"
            assert len(data["nodes"]) > 0, "citationData has no nodes"
            assert len(data["links"]) > 0, "citationData has no links"

            print(f"✓ Field map papers: {len(data['nodes'])} nodes, {len(data['links'])} links")
        except json.JSONDecodeError as e:
            raise AssertionError(f"Invalid JSON in citationData: {e}")

    def test_lineage_html_loads_data(self):
        """Lineage HTML should have valid fetch call for data."""
        with open(Path("../../assets/analysis/citation-lineage.html")) as f:
            content = f.read()

        # Check for fetch call
        assert "fetch('lineage_data.json')" in content, "Missing fetch for lineage_data.json"

        # Check for initialization function
        assert "loadData()" in content, "Missing loadData function"
        assert "initVisualization()" in content, "Missing initVisualization function"
        assert "updateViz()" in content, "Missing updateViz function"

        print("✓ Lineage HTML properly loads data")

    def test_no_syntax_errors(self):
        """Test for common syntax errors in generated HTML."""
        files = [
            "../../assets/analysis/field_map.html",
            "../../assets/analysis/citation-lineage.html",
            "../../assets/analysis/citation-network.html",
        ]

        for filepath in files:
            with open(Path(filepath)) as f:
                content = f.read()

            # Check for unclosed if statements
            if_count = content.count("if (")
            close_count = content.count("}")
            assert if_count <= close_count, f"{filepath}: Possible unclosed if statement"

            # Check for valid JSON embedded
            json_arrays = re.findall(r'const (\w+) = (\{|\[)', content)
            assert len(json_arrays) > 0, f"{filepath}: No data objects found"

            print(f"✓ {Path(filepath).name}: No syntax errors detected")


class TestDataConsistency:
    """Test consistency between different data sources."""

    def test_paper_data_consistency(self):
        """Papers should have consistent data across sources."""
        with open(Path("output/corpus_kcore_25.json")) as f:
            corpus = json.load(f)

        with open(Path("output/paper_rankings_all.json")) as f:
            rankings = json.load(f)

        # Check paper count consistency
        corpus_ids = {p["openalex_id"] for p in corpus}
        ranking_ids = {p["openalex_id"] for p in rankings}

        # Most corpus papers should be in rankings (allow some variance)
        overlap = corpus_ids & ranking_ids
        overlap_ratio = len(overlap) / len(corpus_ids)
        assert overlap_ratio > 0.95, f"Only {overlap_ratio:.1%} corpus papers in rankings"

        print(f"✓ Paper consistency: {len(overlap)} of {len(corpus_ids)} corpus papers in rankings ({overlap_ratio:.1%})")

    def test_author_paper_counts(self):
        """Author paper counts should be positive."""
        with open(Path("output/author_rankings.json")) as f:
            authors = json.load(f)

        invalid_counts = [a for a in authors if a.get("paper_count", 0) < 0]
        assert len(invalid_counts) == 0, f"{len(invalid_counts)} authors with negative paper counts"

        # At least top authors should have papers
        top_author = authors[0]
        assert top_author.get("paper_count", 0) > 0, "Top author should have papers"

        print(f"✓ Author counts valid: top author has {top_author.get('paper_count')} papers")


def run_all_tests():
    """Run all test suites."""
    print("\n" + "=" * 60)
    print("VISUALIZATION TEST SUITE")
    print("=" * 60 + "\n")

    test_classes = [
        TestDataIntegrity,
        TestHTMLGeneration,
        TestDataConsistency,
    ]

    total_tests = 0
    passed = 0

    for test_class in test_classes:
        print(f"\n{test_class.__name__}:")
        print("-" * 40)

        instance = test_class()
        test_methods = [m for m in dir(instance) if m.startswith("test_")]

        for method_name in test_methods:
            total_tests += 1
            try:
                method = getattr(instance, method_name)
                method()
                passed += 1
            except AssertionError as e:
                print(f"✗ {method_name}: {e}")
            except FileNotFoundError as e:
                print(f"✗ {method_name}: File not found: {e}")
            except Exception as e:
                print(f"✗ {method_name}: {type(e).__name__}: {e}")

    print(f"\n" + "=" * 60)
    print(f"RESULTS: {passed}/{total_tests} tests passed")
    print("=" * 60 + "\n")

    return passed == total_tests


if __name__ == "__main__":
    import sys
    success = run_all_tests()
    sys.exit(0 if success else 1)

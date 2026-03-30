"""
Rate-limited, file-cached OpenAlex API client.

Caches every API response as a JSON file so the pipeline is resumable.
Uses the polite pool (10 req/sec) via mailto parameter.
"""
import json
import hashlib
import time
from pathlib import Path

import requests

from config import OPENALEX_BASE, OPENALEX_EMAIL, REQUESTS_PER_SECOND, CACHE_DIR


class OpenAlexClient:
    """Rate-limited OpenAlex API client with file-based caching."""

    def __init__(self):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = (
            f"NeuroTrailblazers-Bibliometrics/1.0 (mailto:{OPENALEX_EMAIL})"
        )
        self.min_interval = 1.0 / REQUESTS_PER_SECOND
        self._last_request_time = 0.0
        self.works_cache = CACHE_DIR / "works"
        self.query_cache = CACHE_DIR / "queries"
        self.works_cache.mkdir(parents=True, exist_ok=True)
        self.query_cache.mkdir(parents=True, exist_ok=True)

    # ── Core request with rate limiting ───────────────────────────────

    def _rate_limit(self):
        """Sleep if needed to respect rate limit."""
        elapsed = time.time() - self._last_request_time
        if elapsed < self.min_interval:
            time.sleep(self.min_interval - elapsed)
        self._last_request_time = time.time()

    def _request(self, url, params=None):
        """Make a rate-limited GET request with retry on 429/5xx."""
        if params is None:
            params = {}
        params["mailto"] = OPENALEX_EMAIL

        for attempt in range(4):
            self._rate_limit()
            try:
                resp = self.session.get(url, params=params, timeout=30)
                if resp.status_code == 200:
                    return resp.json()
                if resp.status_code == 429 or resp.status_code >= 500:
                    wait = 2 ** attempt
                    print(f"  HTTP {resp.status_code}, retrying in {wait}s...")
                    time.sleep(wait)
                    continue
                if resp.status_code == 404:
                    return None
                resp.raise_for_status()
            except requests.exceptions.RequestException as e:
                wait = 2 ** attempt
                print(f"  Request error: {e}, retrying in {wait}s...")
                time.sleep(wait)
        return None

    # ── Cache helpers ─────────────────────────────────────────────────

    def _work_cache_path(self, openalex_id):
        """Cache path for a work by OpenAlex ID (e.g. W2100837269)."""
        safe_id = openalex_id.replace("https://openalex.org/", "")
        return self.works_cache / f"{safe_id}.json"

    def _query_cache_path(self, query_key):
        """Cache path for a search query result."""
        h = hashlib.sha256(query_key.encode()).hexdigest()[:16]
        return self.query_cache / f"{h}.json"

    def _load_cache(self, path):
        if path.exists():
            with open(path) as f:
                return json.load(f)
        return None

    def _save_cache(self, path, data):
        with open(path, "w") as f:
            json.dump(data, f)

    # ── Public API ────────────────────────────────────────────────────

    def get_work_by_doi(self, doi):
        """
        Fetch an OpenAlex Work by DOI.

        Args:
            doi: DOI string (with or without https://doi.org/ prefix)

        Returns:
            dict: Full OpenAlex work object, or None if not found.
            Fields include: id, title, authorships, cited_by_count,
            referenced_works, concepts, publication_year, type, etc.
        """
        # Normalize DOI
        doi = doi.strip().lower()
        doi = doi.replace("https://doi.org/", "").replace("http://doi.org/", "")

        # Check cache by DOI — we may have fetched this before
        doi_cache = self.query_cache / f"doi_{doi.replace('/', '_')}.json"
        cached = self._load_cache(doi_cache)
        if cached is not None:
            return cached

        url = f"{OPENALEX_BASE}/works/doi:{doi}"
        data = self._request(url)
        if data:
            self._save_cache(doi_cache, data)
            # Also cache by OpenAlex ID
            oa_id = data.get("id", "")
            if oa_id:
                self._save_cache(self._work_cache_path(oa_id), data)
        return data

    def get_work(self, openalex_id):
        """
        Fetch an OpenAlex Work by its OpenAlex ID.

        Args:
            openalex_id: e.g. "https://openalex.org/W2100837269" or "W2100837269"

        Returns:
            dict: Full OpenAlex work object, or None.
        """
        cache_path = self._work_cache_path(openalex_id)
        cached = self._load_cache(cache_path)
        if cached is not None:
            return cached

        oa_id = openalex_id.replace("https://openalex.org/", "")
        url = f"{OPENALEX_BASE}/works/{oa_id}"
        data = self._request(url)
        if data:
            self._save_cache(cache_path, data)
        return data

    def get_cited_by(self, openalex_id, max_results=200):
        """
        Fetch works that cite a given paper.

        Args:
            openalex_id: OpenAlex work ID
            max_results: Max papers to return (sorted by cited_by_count desc)

        Returns:
            list[dict]: List of OpenAlex work objects citing this paper.
        """
        oa_id = openalex_id.replace("https://openalex.org/", "")
        cache_key = f"cited_by_{oa_id}_{max_results}"
        cache_path = self._query_cache_path(cache_key)
        cached = self._load_cache(cache_path)
        if cached is not None:
            return cached

        results = []
        cursor = "*"
        url = f"{OPENALEX_BASE}/works"
        while len(results) < max_results and cursor:
            params = {
                "filter": f"cites:{oa_id}",
                "sort": "cited_by_count:desc",
                "per_page": min(200, max_results - len(results)),
                "cursor": cursor,
            }
            data = self._request(url, params)
            if not data or not data.get("results"):
                break
            results.extend(data["results"])
            cursor = data.get("meta", {}).get("next_cursor")

        # Cache each individual work too
        for work in results:
            wid = work.get("id", "")
            if wid:
                self._save_cache(self._work_cache_path(wid), work)

        self._save_cache(cache_path, results)
        return results

    def search_works(self, query, filters=None, sort="cited_by_count:desc",
                     max_results=200):
        """
        Search OpenAlex works by query string.

        Args:
            query: Search string (for default.search or title.search)
            filters: dict of OpenAlex filters, e.g.
                     {"publication_year": ">1985", "cited_by_count": ">5"}
            sort: Sort order
            max_results: Max results to return

        Returns:
            list[dict]: List of OpenAlex work objects.
        """
        filter_str = ""
        if filters:
            parts = [f"{k}:{v}" for k, v in filters.items()]
            filter_str = ",".join(parts)

        cache_key = f"search_{query}_{filter_str}_{sort}_{max_results}"
        cache_path = self._query_cache_path(cache_key)
        cached = self._load_cache(cache_path)
        if cached is not None:
            return cached

        results = []
        cursor = "*"
        url = f"{OPENALEX_BASE}/works"
        while len(results) < max_results and cursor:
            params = {
                "search": query,
                "sort": sort,
                "per_page": min(200, max_results - len(results)),
                "cursor": cursor,
            }
            if filter_str:
                params["filter"] = filter_str
            data = self._request(url, params)
            if not data or not data.get("results"):
                break
            results.extend(data["results"])
            cursor = data.get("meta", {}).get("next_cursor")

        for work in results:
            wid = work.get("id", "")
            if wid:
                self._save_cache(self._work_cache_path(wid), work)

        self._save_cache(cache_path, results)
        return results

    def search_works_by_title(self, title_query, filters=None,
                               sort="cited_by_count:desc", max_results=200):
        """
        Search OpenAlex works by title.

        Same as search_works but uses title.search parameter.
        """
        filter_str = ""
        if filters:
            parts = [f"{k}:{v}" for k, v in filters.items()]
            filter_str = ",".join(parts)

        cache_key = f"title_search_{title_query}_{filter_str}_{sort}_{max_results}"
        cache_path = self._query_cache_path(cache_key)
        cached = self._load_cache(cache_path)
        if cached is not None:
            return cached

        results = []
        cursor = "*"
        url = f"{OPENALEX_BASE}/works"
        while len(results) < max_results and cursor:
            params = {
                "filter": f"title.search:{title_query}",
                "sort": sort,
                "per_page": min(200, max_results - len(results)),
                "cursor": cursor,
            }
            if filter_str:
                params["filter"] += "," + filter_str
            data = self._request(url, params)
            if not data or not data.get("results"):
                break
            results.extend(data["results"])
            cursor = data.get("meta", {}).get("next_cursor")

        for work in results:
            wid = work.get("id", "")
            if wid:
                self._save_cache(self._work_cache_path(wid), work)

        self._save_cache(cache_path, results)
        return results

    def search_works_by_concept(self, concept_id, sort="cited_by_count:desc",
                                 max_results=200):
        """
        Fetch top works tagged with a given OpenAlex concept.

        Args:
            concept_id: e.g. "C2776102887" for connectomics
        """
        cache_key = f"concept_{concept_id}_{sort}_{max_results}"
        cache_path = self._query_cache_path(cache_key)
        cached = self._load_cache(cache_path)
        if cached is not None:
            return cached

        results = []
        cursor = "*"
        url = f"{OPENALEX_BASE}/works"
        while len(results) < max_results and cursor:
            params = {
                "filter": f"concepts.id:{concept_id}",
                "sort": sort,
                "per_page": min(200, max_results - len(results)),
                "cursor": cursor,
            }
            data = self._request(url, params)
            if not data or not data.get("results"):
                break
            results.extend(data["results"])
            cursor = data.get("meta", {}).get("next_cursor")

        for work in results:
            wid = work.get("id", "")
            if wid:
                self._save_cache(self._work_cache_path(wid), work)

        self._save_cache(cache_path, results)
        return results

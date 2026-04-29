import os
import sys
from pathlib import Path

import pytest

pytest.importorskip("reportlab")

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from generate_report import derive_date, derive_url


class TestDeriveUrl:
    def test_standard_folder(self):
        assert derive_url(Path("20240101_120000_linear_app")) == "Linear App"

    def test_single_word_site(self):
        assert derive_url(Path("20240101_120000_github")) == "Github"

    def test_multi_word_site(self):
        assert derive_url(Path("20240101_120000_the_internet")) == "The Internet"

    def test_no_site_name_returns_raw(self):
        # Only 2 parts — falls back to raw folder name
        assert derive_url(Path("20240101_120000")) == "20240101_120000"

    def test_single_part_returns_raw(self):
        assert derive_url(Path("short")) == "short"


class TestDeriveDate:
    def test_valid_folder(self):
        assert derive_date(Path("20240101_120000_test")) == "January 1, 2024"

    def test_another_valid_folder(self):
        assert derive_date(Path("20250315_093045_test")) == "March 15, 2025"

    def test_invalid_returns_empty(self):
        assert derive_date(Path("invalid_folder_name")) == ""

    def test_too_short_returns_empty(self):
        assert derive_date(Path("short")) == ""

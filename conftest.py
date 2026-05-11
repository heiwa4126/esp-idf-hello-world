import importlib.util
import os
from pathlib import Path

import pytest

_idf_path = os.environ.get("IDF_PATH")
if not _idf_path:
    raise RuntimeError("IDF_PATH is not set. Run: source $IDF_PATH/export.sh")

idf_conftest = Path(_idf_path) / "conftest.py"
if not idf_conftest.is_file():
    raise RuntimeError(f"ESP-IDF conftest not found: {idf_conftest}")

spec = importlib.util.spec_from_file_location("esp_idf_conftest", idf_conftest)
if spec is None or spec.loader is None:
    raise RuntimeError(f"Failed to load ESP-IDF conftest: {idf_conftest}")

esp_idf_conftest = importlib.util.module_from_spec(spec)
spec.loader.exec_module(esp_idf_conftest)

# Import only the fixture we need from ESP-IDF conftest.
# Do not re-export pytest hooks, as CI-specific hooks can break local runs.
log_minimum_free_heap_size = esp_idf_conftest.log_minimum_free_heap_size


@pytest.fixture
def idf_path() -> str | None:
    return _idf_path

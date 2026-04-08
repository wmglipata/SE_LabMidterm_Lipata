import pytest
# Ensure your folder structure allows this import
from src.module import CoreProcessor, validate_config

def test_processor_initialization():
    """Verify that the processor starts with empty results."""
    proc = CoreProcessor()
    assert proc.results == []
    assert isinstance(proc.config, dict)

def test_process_data_valid_input():
    """Verify that valid strings are trimmed and uppercased."""
    proc = CoreProcessor()
    result = proc.process_data("  moodleplus project  ")
    assert result == "MOODLEPLUS PROJECT"
    assert "MOODLEPLUS PROJECT" in proc.results


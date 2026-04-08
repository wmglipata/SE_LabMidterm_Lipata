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

def test_process_data_null_input():
    """Verify that the processor raises a ValueError on None input."""
    proc = CoreProcessor()
    with pytest.raises(ValueError, match="Input cannot be null."):
        proc.process_data(None)

def test_validate_config_helper():
    """Check if the config validator identifies dictionaries correctly."""
    assert validate_config({"key": "value"}) is True
    assert validate_config("not a dict") is False

# Positive test cases for additional coverage
def test_process_data_numeric_string():
    """Positive: Verify numeric strings are handled correctly."""
    proc = CoreProcessor()
    assert proc.process_data("12345") == "12345"

def test_process_data_special_chars():
    """Positive/Edge: Verify special characters are preserved."""
    proc = CoreProcessor()
    assert proc.process_data("!@#$%^&*()") == "!@#$%^&*()"

def test_process_data_very_long_string():
    """Edge: Verify handling of large inputs."""
    long_input = "a" * 1000
    proc = CoreProcessor()
    assert proc.process_data(long_input) == long_input.upper()

def test_process_data_mixed_case():
    """Positive: Verify mixed case is standardized to uppercase."""
    proc = CoreProcessor()
    assert proc.process_data("mOoDlEpLuS") == "MOODLEPLUS"
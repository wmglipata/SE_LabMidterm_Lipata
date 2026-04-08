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

# Positive and Edge test cases for additional coverage
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

# Negative test case for invalid config
def test_process_data_empty_string():
    """Negative: Verify empty string raises ValueError (per our module logic)."""
    proc = CoreProcessor()
    with pytest.raises(ValueError, match="Input data cannot be empty."):
        proc.process_data("")

def test_process_data_whitespace_only():
    """Negative: Verify string with only spaces is treated as empty."""
    proc = CoreProcessor()
    with pytest.raises(ValueError, match="Input data cannot be empty."):
        proc.process_data("   ")

def test_process_data_integer_input():
    """Negative: Verify non-string input handling."""
    proc = CoreProcessor()
    # If your logic only expects strings, this should be tested
    with pytest.raises(Exception):
        proc.process_data(12345)

# Non-functional test cases
import time

def test_process_data_performance():
    """Non-Functional: Ensure processing takes less than 10ms."""
    proc = CoreProcessor()
    start_time = time.time()
    proc.process_data("Performance Test")
    end_time = time.time()
    duration = end_time - start_time
    assert duration < 0.01  # 10 milliseconds

def test_results_list_integrity():
    """Non-Functional: Verify results list grows correctly over 100 iterations."""
    proc = CoreProcessor()
    for i in range(100):
        proc.process_data(f"data_{i}")
    assert len(proc.results) == 100

def test_config_immutability():
    """Non-Functional: Verify config doesn't change during processing."""
    config = {"id": 1}
    proc = CoreProcessor(config)
    proc.process_data("test")
    assert proc.config == {"id": 1} # Ensure processing didn't leak into config

def test_processor_reset_simulation():
    """Non-Functional: Verify starting a new instance provides a fresh state."""
    proc1 = CoreProcessor()
    proc1.process_data("First")
    proc2 = CoreProcessor()
    assert len(proc2.results) == 0  # Should be fresh
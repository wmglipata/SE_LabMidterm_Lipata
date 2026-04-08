import pytest
# Ensure your folder structure allows this import
from src.module import CoreProcessor, validate_config

def test_processor_initialization():
    """Verify that the processor starts with empty results."""
    proc = CoreProcessor()
    assert proc.results == []
    assert isinstance(proc.config, dict)


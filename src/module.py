import logging

# Configure logging to see the output in your CI/CD logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_config(config):
    """TC 4: Helper to ensure configuration is a dictionary."""
    return isinstance(config, dict)

class CoreProcessor:
    def __init__(self, config=None):
        # TC 1: Initialize with empty results
        # TC 8 & 14: Handle config and ensure it's a dict
        self.config = config if config is not None else {}
        self.results = []

    def process_data(self, raw_input):
        """
        Processes string data with strict validation.
        Fixes TC 3, 9, 10, and 11.
        """
        # TC 3: Check for Null/None input
        if raw_input is None:
            raise ValueError("Input cannot be null.")

        # TC 11: Strict Type Enforcement (Reject integers/floats)
        if not isinstance(raw_input, str):
            raise TypeError("Input must be a string.")

        # TC 2 & 10: Trim whitespace and check if result is empty
        processed = raw_input.strip()
        if not processed:
            raise ValueError("Input data cannot be empty.")

        # TC 2, 5, 6, 7, 8: Final Transformation
        # Standardizes to uppercase and preserves symbols
        final_result = processed.upper()
        
        # TC 13: Integrity - save to results history
        self.results.append(final_result)
        
        logger.info(f"Processed: {final_result}")
        return final_result
import logging

# Set up logging for the module
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class CoreProcessor:
    """
    Main logic handler for the Moodleplus software engineering project.
    """
    def __init__(self, config_data=None):
        self.config = config_data or {}
        self.results = []
        logger.info("CoreProcessor initialized.")

    def process_data(self, raw_input):
        """
        Processes input data with basic validation and error handling.
        """
        try:
            if raw_input is None:
                raise ValueError("Input cannot be null.")
            
            # Transformation logic
            processed = str(raw_input).strip().upper()
            self.results.append(processed)
            
            logger.info(f"Successfully processed data: {processed}")
            return processed
        except Exception as e:
            logger.error(f"Processing error: {e}")
            raise
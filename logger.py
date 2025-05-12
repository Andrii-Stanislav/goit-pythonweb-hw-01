import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Create a logger instance
logger = logging.getLogger(__name__)

def get_logger():
    return logger 
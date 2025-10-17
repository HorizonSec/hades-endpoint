"""Shared logging utilities for HADES Endpoint Security."""

import logging
import sys


def setup_logging(level=logging.INFO):
    """
    Set up logging configuration.
    
    Args:
        level: The logging level (default: logging.INFO)
    
    Returns:
        Logger instance
    """
    logger = logging.getLogger("hades_endpoint")
    
    # Avoid adding handlers multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    logger.setLevel(level)
    return logger

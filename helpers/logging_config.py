# helpers/logging_config.py

import logging

def setup_logging():
    """
    Set up logging configuration.

    This function configures the logging module to output messages with a specified format and level.

    Example:
        Usage:

        >>> setup_logging()
    """
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

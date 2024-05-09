# helpers/config_helper.py

import configparser

def read_config(config_file):
    """
    Read configuration from a specified file.

    Args:
        config_file (str): The path to the configuration file.

    Returns:
        configparser.ConfigParser: A ConfigParser object containing the configuration.

    Example:
        Assuming 'config.ini' contains the following:

        [Settings]
        key1 = value1
        key2 = value2

        Usage:

        >>> config = read_config('config.ini')
        >>> config['Settings']['key1']
        'value1'
    """
    config = configparser.ConfigParser()
    config.read(config_file)
    return config
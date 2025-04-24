import yaml
import os
import numpy as np
import pandas as pd
from typing import Dict, Any, List, Tuple
from pathlib import Path
import logging
from .logging_setup import logger
from box import ConfigBox

def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a YAML file and return its contents as a ConfigBox object
    
    Args:
        path_to_yaml (Path): Path to the YAML file
        
    Returns:
        ConfigBox: YAML contents as a ConfigBox object
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except Exception as e:
        logger.error(f"Error loading YAML file {path_to_yaml}: {str(e)}")
        raise e

def create_directories(paths: List[Path]) -> None:
    """
    Create directories if they don't exist
    
    Args:
        paths (List[Path]): List of directory paths to create
    """
    try:
        for path in paths:
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Directory {path} created successfully")
    except Exception as e:
        logger.error(f"Error creating directories: {str(e)}")
        raise e

def save_yaml(path: Path, data: Dict[str, Any]) -> None:
    """
    Save data to a YAML file
    
    Args:
        path (Path): Path to save the YAML file
        data (Dict[str, Any]): Data to save
    """
    try:
        with open(path, 'w') as yaml_file:
            yaml.dump(data, yaml_file, default_flow_style=False)
        logger.info(f"YAML file saved successfully to {path}")
    except Exception as e:
        logger.error(f"Error saving YAML file to {path}: {str(e)}")
        raise e

def get_size(path: Path) -> str:
    """
    Get size of file in KB
    
    Args:
        path (Path): Path to the file
        
    Returns:
        str: Size of file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

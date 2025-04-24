import os
import pathlib
import logging  # Import the logging library
import sys
import yaml
from pathlib import Path
from typing import List, Dict

# --- Configure Logging ---
# Set up basic configuration for logging to the console
logging.basicConfig(
    level=logging.INFO,  # Set the minimum level of messages to log (INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
    datefmt='%Y-%m-%d %H:%M:%S'  # Define the date format
)

# --- Define Version ---
VERSION = "0.0.0"


# --- Define Project Description ---
DESCRIPTION = "Wine Quality Prediction using Machine Learning"

# --- Define Project Name ---
PROJECT_NAME = "wine_quality_ml"

# --- Define Directories to Create ---
dirs_to_create = [
    PROJECT_NAME,  # Root project directory
    f"{PROJECT_NAME}/config",
    f"{PROJECT_NAME}/data/01_raw",
    f"{PROJECT_NAME}/data/02_interim",
    f"{PROJECT_NAME}/data/03_processed",
    f"{PROJECT_NAME}/data/04_external",
    f"{PROJECT_NAME}/docs",
    f"{PROJECT_NAME}/logs",
    f"{PROJECT_NAME}/models/evaluation",
    f"{PROJECT_NAME}/notebooks",
    f"{PROJECT_NAME}/reports/figures",
    f"{PROJECT_NAME}/tests",
    f"{PROJECT_NAME}/src/data",
    f"{PROJECT_NAME}/src/features",
    f"{PROJECT_NAME}/src/models",
    f"{PROJECT_NAME}/src/evaluation",
    f"{PROJECT_NAME}/src/utils",
    f"{PROJECT_NAME}/src/components",
    f"{PROJECT_NAME}/src/pipeline",
    f"{PROJECT_NAME}/src/constants",
    f"{PROJECT_NAME}/src/config",
    f"{PROJECT_NAME}/src/visualization",
]
# --- Define Files to Create ---
project_files_to_create = [
    # Config files
    f"{PROJECT_NAME}/config/config.yaml",
    f"{PROJECT_NAME}/config/model_config.yaml",
    f"{PROJECT_NAME}/config/logging_config.yaml",
    
    # Documentation
    f"{PROJECT_NAME}/docs/README.md",
    
    # Source code files
    f"{PROJECT_NAME}/src/__init__.py",
    f"{PROJECT_NAME}/src/data/__init__.py",
    f"{PROJECT_NAME}/src/data/make_dataset.py",
    f"{PROJECT_NAME}/src/data/data_validation.py",
    f"{PROJECT_NAME}/src/features/__init__.py",
    f"{PROJECT_NAME}/src/features/build_features.py",
    f"{PROJECT_NAME}/src/models/__init__.py",
    f"{PROJECT_NAME}/src/models/train_model.py",
    f"{PROJECT_NAME}/src/models/predict_model.py",
    f"{PROJECT_NAME}/src/visualization/__init__.py",
    f"{PROJECT_NAME}/src/visualization/visualize.py",
    f"{PROJECT_NAME}/src/utils/__init__.py",
    f"{PROJECT_NAME}/src/utils/utils.py",
    f"{PROJECT_NAME}/src/evaluation/__init__.py",
    f"{PROJECT_NAME}/src/evaluation/evaluate_model.py",
    
    # Test files
    f"{PROJECT_NAME}/tests/__init__.py",
    f"{PROJECT_NAME}/tests/test_data.py",
    f"{PROJECT_NAME}/tests/test_features.py",
    f"{PROJECT_NAME}/tests/test_models.py",
    
    # Components
    f"{PROJECT_NAME}/src/components/__init__.py",
    f"{PROJECT_NAME}/src/components/data_ingestion.py",
    f"{PROJECT_NAME}/src/components/data_validation.py",
    f"{PROJECT_NAME}/src/components/data_transformation.py",
    f"{PROJECT_NAME}/src/components/model_trainer.py",
    f"{PROJECT_NAME}/src/components/model_evaluation.py",
    
    # Pipeline
    f"{PROJECT_NAME}/src/pipeline/__init__.py",
    f"{PROJECT_NAME}/src/pipeline/stage_01_data_ingestion.py",
    f"{PROJECT_NAME}/src/pipeline/stage_02_data_validation.py",
    f"{PROJECT_NAME}/src/pipeline/stage_03_data_transformation.py",
    f"{PROJECT_NAME}/src/pipeline/stage_04_model_trainer.py",
    f"{PROJECT_NAME}/src/pipeline/stage_05_model_evaluation.py",
    
    # Constants
    f"{PROJECT_NAME}/src/constants/__init__.py",
    f"{PROJECT_NAME}/src/constants/constants.py",
    
    # Config
    f"{PROJECT_NAME}/src/config/__init__.py",
    f"{PROJECT_NAME}/src/config/configuration.py",
    
    # params.yaml
    f"{PROJECT_NAME}/params.yaml",
]

# --- Define Root Level Files ---
root_files_to_create = [
    "setup.py",
    "requirements.txt",
    ".gitignore",
    "README.md"
]

# --- Basic Gitignore Content ---
gitignore_content = """
# Standard Python ignores...
__pycache__/
*.py[cod]
*.so

# Environment stuff...
.env
.venv
env/
venv/

# Data (usually managed outside git or with LFS/DVC)
# data/

# Logs
logs/
*.log

# Models (usually large)
models/*.pkl
models/*.h5
models/*.onnx

# Notebook checkpoints
.ipynb_checkpoints

# IDE folders
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db
"""

def write_file_with_encoding(path: Path, content: str):
    """Write file content with proper encoding handling."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    except Exception as e:
        logging.error(f"Error writing to {path}: {str(e)}")
        raise

def create_project_structure():
    """Create the project directory structure and files."""
    try:
        # Create directories
        for dir_path in dirs_to_create:
            path = Path(dir_path)
            path.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {path}")

        # Create project files
        for file_path in project_files_to_create:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)
            logging.info(f"Created file: {path}")

            # Add content to specific files
            if file_path.endswith('config.yaml'):
                content = """# Data paths
data:
  raw: data/01_raw/winequality-red.csv
  interim: data/02_interim/
  processed: data/03_processed/
  external: data/04_external/

# Model parameters
model:
  random_state: 42
  test_size: 0.2
  n_estimators: 100
  max_depth: None

# Logging configuration
logging:
  level: INFO
  format: '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  datefmt: '%Y-%m-%d %H:%M:%S'
"""
                write_file_with_encoding(path, content)
                logging.info(f"Added content to {file_path}")

        # Create root level files
        for file_path in root_files_to_create:
            path = Path(file_path)
            path.touch(exist_ok=True)
            logging.info(f"Created file: {path}")

            if file_path == '.gitignore':
                write_file_with_encoding(path, gitignore_content.strip())
                logging.info(f"Added content to {file_path}")

            elif file_path == 'requirements.txt':
                content = """pandas>=1.3.0
numpy>=1.21.0
scikit-learn>=0.24.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
pytest>=6.2.0
pytest-cov>=2.12.0
black>=21.5b2
flake8>=3.9.0
isort>=5.9.0
"""
                write_file_with_encoding(path, content)
                logging.info(f"Added content to {file_path}")

            elif file_path == 'README.md':
                content = f"""# {PROJECT_NAME}

{DESCRIPTION}

## Project Structure
```
{PROJECT_NAME}/
├── config/               # Configuration files
├── data/                # Data files
│   ├── 01_raw/         # Raw data
│   ├── 02_interim/     # Intermediate data
│   ├── 03_processed/   # Processed data
│   └── 04_external/    # External data
├── docs/               # Documentation
├── logs/              # Log files
├── models/            # Trained models
├── notebooks/         # Jupyter notebooks
├── reports/           # Reports and figures
├── src/               # Source code
│   ├── components/    # Pipeline components
│   ├── pipeline/      # Training pipeline
│   ├── utils/         # Utility functions
│   └── ...
└── tests/             # Test files
```

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
# Train the model
wine-quality-train

# Make predictions
wine-quality-predict
```

## Version
{VERSION}
"""
                write_file_with_encoding(path, content)
                logging.info(f"Added content to {file_path}")

        logging.info("Project structure created successfully!")
        
    except Exception as e:
        logging.error(f"Error creating project structure: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    create_project_structure()



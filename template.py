import os
import pathlib
import logging
import sys
import yaml
from pathlib import Path
from typing import List, Dict, Optional
import shutil

# --- Configure Logging ---
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# --- Define Version ---
VERSION = "0.0.0"

# --- Define Project Description ---
DESCRIPTION = "Wine Quality Prediction using Machine Learning"

# --- Define Project Name ---
PROJECT_NAME = "wine_quality_ml"

class ProjectTemplate:
    def __init__(self):
        self.project_root = Path(PROJECT_NAME)
        self.dirs_to_create = self._get_directories()
        self.files_to_create = self._get_files()
        self.config_content = self._get_config_content()
        self.gitignore_content = self._get_gitignore_content()
        self.readme_content = self._get_readme_content()
        self.requirements_content = self._get_requirements_content()

    def _get_directories(self) -> List[str]:
        """Return list of directories to create."""
        return [
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
        ]

    def _get_files(self) -> List[str]:
        """Return list of files to create."""
        return [
            # Config files
            f"{PROJECT_NAME}/config/config.yaml",
            f"{PROJECT_NAME}/config/model_config.yaml",
            f"{PROJECT_NAME}/config/logging_config.yaml",
            
            # Documentation
            f"{PROJECT_NAME}/docs/README.md",
            f"{PROJECT_NAME}/README.md",
            
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
            
            # Setup files
            "setup.py",
            "requirements.txt",
            ".gitignore",
            
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

    def _get_config_content(self) -> str:
        """Return content for config.yaml."""
        return """# Data paths
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

    def _get_gitignore_content(self) -> str:
        """Return content for .gitignore."""
        return """
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

    def _get_readme_content(self) -> str:
        """Return content for README.md."""
        return f"""# {PROJECT_NAME}

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
python src/main.py
```

## Version
{VERSION}
"""

    def _get_requirements_content(self) -> str:
        """Return content for requirements.txt."""
        return """pandas>=1.3.0
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

    def create_directory(self, dir_path: str) -> bool:
        """Create a directory if it doesn't exist."""
        try:
            path = Path(dir_path)
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created directory: {path}")
            return True
        except Exception as e:
            logger.error(f"Error creating directory {dir_path}: {e}")
            return False

    def create_file(self, file_path: str, content: Optional[str] = None) -> bool:
        """Create a file with optional content."""
        try:
            path = Path(file_path)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.touch(exist_ok=True)
            if content:
                path.write_text(content)
            logger.info(f"Created file: {path}")
            return True
        except Exception as e:
            logger.error(f"Error creating file {file_path}: {e}")
            return False

    def create_project_structure(self) -> bool:
        """Create the complete project structure."""
        try:
            # Check if project directory already exists
            if self.project_root.exists():
                logger.warning(f"Project directory {self.project_root} already exists.")
                response = input("Do you want to overwrite it? (y/n): ")
                if response.lower() != 'y':
                    logger.info("Project creation aborted.")
                    return False
                shutil.rmtree(self.project_root)

            # Create directories
            for dir_path in self.dirs_to_create:
                if not self.create_directory(dir_path):
                    return False

            # Create files
            for file_path in self.files_to_create:
                content = None
                if file_path.endswith('config.yaml'):
                    content = self.config_content
                elif file_path.endswith('.gitignore'):
                    content = self.gitignore_content
                elif file_path.endswith('README.md'):
                    content = self.readme_content
                elif file_path.endswith('requirements.txt'):
                    content = self.requirements_content
                
                if not self.create_file(file_path, content):
                    return False

            logger.info("Project structure created successfully!")
            return True
            
        except Exception as e:
            logger.error(f"Error creating project structure: {str(e)}")
            return False

def main():
    """Main function to create the project structure."""
    template = ProjectTemplate()
    success = template.create_project_structure()
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()



from setuptools import setup, find_packages
from typing import List

# Read the README.md for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Read requirements.txt for dependencies
def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a requirements file.
    """
    requirements = []
    with open(file_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.append(line)
    return requirements

__version__ = "0.0.0"

REPO_NAME = "ML_WineQuality"
AUTHOR_USER_NAME = "rezjsh"
SRC_REPO = "wine_quality_ml"

# Define development dependencies
DEV_REQUIREMENTS = [
    "pytest>=6.2.0",
    "pytest-cov>=2.12.0",
    "black>=21.5b2",
    "flake8>=3.9.0",
    "isort>=5.9.0",
    "mypy>=0.910",
    "pre-commit>=2.13.0",
]

# Define documentation dependencies
DOCS_REQUIREMENTS = [
    "sphinx>=4.0.0",
    "sphinx-rtd-theme>=0.5.0",
    "nbsphinx>=0.8.0",
]

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A machine learning package for Wine Quality Prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Documentation": f"https://{AUTHOR_USER_NAME}.github.io/{REPO_NAME}/",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    package_dir={"": SRC_REPO},
    packages=find_packages(where=SRC_REPO),
    python_requires=">=3.8",
    install_requires=get_requirements("requirements.txt"),
    extras_require={
        "dev": DEV_REQUIREMENTS,
        "docs": DOCS_REQUIREMENTS,
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        "console_scripts": [
            "wine-quality-train=wine_quality_ml.src.pipeline.stage_04_model_trainer:main",
            "wine-quality-predict=wine_quality_ml.src.models.predict_model:main",
        ],
    },
    package_data={
        "wine_quality_ml": [
            "config/*.yaml",
            "data/01_raw/*.csv",
            "data/02_interim/*.csv",
            "data/03_processed/*.csv",
            "data/04_external/*.csv",
        ],
    },
    include_package_data=True,
    zip_safe=False,
) 
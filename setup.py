from setuptools import setup, find_packages
from typing import List

# Read the README.md for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements.txt for dependencies
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

__version__ = "0.0.1"

REPO_NAME = "ML_WineQuality"
AUTHOR_USER_NAME = "Reza"
SRC_REPO = "wine_quality_ml"

# Define development dependencies
DEV_REQUIREMENTS = []

# Define documentation dependencies
DOCS_REQUIREMENTS = []

setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email="your.email@example.com",
    description="Wine Quality Prediction using Machine Learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Documentation": f"https://{AUTHOR_USER_NAME}.github.io/{REPO_NAME}/",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
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
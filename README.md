# wine_quality_ml

Wine Quality Prediction using Machine Learning

## Project Structure
```
wine_quality_ml/
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
0.0.0

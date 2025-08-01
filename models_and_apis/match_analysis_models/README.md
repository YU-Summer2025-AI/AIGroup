# match_analysis_models

This folder contains scripts and notebooks for analyzing the behavior and interpretability of match prediction models, with a focus on feature importance and SHAP-based explanations.

## Contents
- **future_importance_api.ipynb**: Jupyter notebook that computes and visualizes feature importances for match models, using SHAP values to explain model predictions and highlight the most influential features.
- **Prefrence_Model_SHAP_API_Analysis/**: Directory containing:
  - `female_model_analysis.py` / `male_model_analysis.py`: Scripts for running SHAP analysis on female and male preference models, respectively.
  - `female_model_graphs.py` / `male_model_graphs.py`: Generate detailed SHAP summary plots and dependence graphs for each gender's model.
  - `female_model_singular_graphs.py` / `male_model_singular_graphs.py`: Create individual-level SHAP visualizations for specific users or predictions.
  - `female_model.py` / `male_model.py`: Model training and inference code for each gender's preference model.
  - `female_pref.sql` / `male_pref.sql`: SQL queries to extract and preprocess data for SHAP analysis.
  - `main.py`: Entry point for running the SHAP analysis pipeline.
- **README.md**: This file.

Use this folder to interpret and visualize model predictions, understand which features drive acceptance or rejection, and generate both global and local explanations for match outcomes. The scripts support both batch and individual-level analysis, and are designed to help improve model transparency and trustworthiness.


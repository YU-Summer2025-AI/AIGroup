# match_prediction_models

This folder contains code and resources for predicting match outcomes using a variety of machine learning algorithms, with a focus on both approval and on-target match prediction.

## Contents
- **random_forest_clean.ipynb**: Jupyter notebook implementing a Random Forest model for predicting match acceptance, including data preprocessing, feature engineering, model training, and evaluation.
- **xgboost_approval_model/**: Contains:
  - `api/`: API endpoints for serving XGBoost-based approval predictions.
  - `queries/`: SQL queries for extracting and preparing features for the approval model.
  - `views/`: Database views to support feature engineering.
  - `xgboost_model/`: Scripts and model files for training and deploying the XGBoost approval model.
  - `requirements.txt`: Python dependencies for this module.
- **xgboost_on_target_model/**: Contains:
  - `get_data.py`: Script for extracting and preparing data for on-target match prediction.
  - `on_target_prediction_models.ipynb`: Notebook for training and evaluating XGBoost models focused on predicting on-target matches.
  - `process_matches_and_members.py`: Data processing utilities for matches and members.
  - `rejection_type_counts.py`: Script for analyzing rejection types in the dataset.

Use this folder to develop, train, and deploy models that predict match acceptance, rejection, and other outcomes, leveraging both tree-based and ensemble methods. The structure supports both research and production deployment workflows.


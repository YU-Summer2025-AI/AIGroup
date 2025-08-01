# attempted_models

This folder contains experimental and in-progress machine learning models and utilities for exploring different approaches to match prediction and analysis.

## Subfolders and Files
- **fastai/**: Contains scripts and requirements for models built using the FastAI library, including:
  - `dataQuery.py`: Script for querying and preparing data for FastAI models.
  - `query.sql`: SQL queries for extracting relevant features from the database.
  - `requirements.txt`: Python dependencies for FastAI-based experiments.
  - `later_fastai_models/`: Jupyter notebooks for advanced or alternative FastAI model experiments (e.g., `first_model.ipynb`, `second_model.ipynb`).
- **normalization/**: Contains SQL views and a Python script for normalizing match and member data:
  - `matches_values_view.sql` / `member_values_view.sql`: SQL views for standardizing and cleaning match/member features.
  - `model.py`: Python code for applying normalization logic.

Use this folder to prototype new modeling ideas, test data preprocessing strategies, and experiment with different ML frameworks before integrating them into the main pipeline.


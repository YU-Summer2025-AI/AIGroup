# AIGroup Project

## Overview

This repository contains code, data, and models for a comprehensive ETL and machine learning pipeline focused on match analysis, recommendation, and prediction. The project is organized into several modules, each responsible for a different aspect of the data workflow, from extraction and transformation to advanced analytics and API deployment.

## Directory Structure

- **etl/**: Contains scripts and resources for Extract, Transform, Load (ETL) processes, including distance calculations, embedding generation, and PostgreSQL setup scripts.
  - `calculate_distances/`: Scripts for geolocation and distance calculations.
  - `embeddings/`: Scripts for creating and managing embeddings.
  - `postgres_setup/`: SQL and Python scripts for setting up and loading data into PostgreSQL, including support for pgvector.
- **models_and_apis/**: Contains machine learning models, APIs, and analysis tools.
  - `attempted_models/`: Experimental and in-progress models, including FastAI and normalization scripts.
  - `match_analysis_models/`: Analysis notebooks and scripts for understanding model behavior and feature importance.
  - `match_prediction_models/`: Notebooks and scripts for predicting match outcomes using various ML algorithms (e.g., Random Forest, XGBoost).
  - `match_recommendation_models/`: Scripts and APIs for generating match recommendations, including data processing and encryption utilities.

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL (with pgvector extension for vector search)
- Docker (optional, for containerized database setup)

### Installation
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd AIGroup
   ```
2. Install Python dependencies for each module as needed:
   ```bash
   pip install -r etl/calculate_distances/requirements.txt
   pip install -r models_and_apis/attempted_models/fastai/requirements.txt
   pip install -r models_and_apis/match_recommendation_models/requirements.txt
   # ...and others as required
   ```
3. (Optional) Set up PostgreSQL using the provided Dockerfiles and SQL scripts in `etl/postgres_setup/`.

### Usage
- **ETL Pipeline**: Use scripts in `etl/` to process and load data.
- **Model Training & Analysis**: Explore and run notebooks/scripts in `models_and_apis/` for training, evaluation, and analysis.
- **APIs**: Deploy or test APIs for recommendations and analysis as provided in the relevant subfolders.


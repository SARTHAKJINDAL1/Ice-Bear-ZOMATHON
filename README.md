# CSAO Recommendation System

This project implements a contextual sequential recommendation system 
for Cart Super Add-On (CSAO) rail optimization.

## Features
- Synthetic realistic data generator
- Feature engineering pipeline
- LightGBM ranking model
- Offline evaluation metrics
- Production-ready inference simulation

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Generate data:
python src/data_generator.py

3. Train model:
python src/train_gbm.py

4. Evaluate:
python src/evaluate.py
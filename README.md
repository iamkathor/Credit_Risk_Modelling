# Credit Risk Modelling Project

This project is a simple machine learning application for predicting whether a person is likely to be a good or bad credit risk based on historical customer data. It uses a German credit dataset and demonstrates the full workflow of data analysis, model training, and deployment through a web app.

## What this project does
- Explores the dataset to understand factors related to credit approval and repayment behavior
- Trains a classification model to predict credit risk
- Provides an interactive Streamlit app where users can input customer details and receive a prediction

## Project Files
- `analysis_model.ipynb` - notebook used for data exploration and model development
- `app.py` - Streamlit web application for making predictions
- `german_credit_data.csv` - dataset used for training the model

## Why this project is useful
Credit risk modelling helps financial institutions estimate the probability that a borrower may default. This project shows how data science and machine learning can support such decisions in a simple and practical way.

## How to run locally
1. Install the required Python packages:
```bash
pip install pandas numpy scikit-learn streamlit matplotlib seaborn
```

2. Start the app:
```bash
streamlit run app.py
```


# EPL Insight Engine and Predictor

Machine learning and data analysis project focused on predicting English Premier League match outcomes using historical football statistics.

## Project Overview

This project explores the use of machine learning models to predict Premier League match results (Home Win, Draw, Away Win) using historical match data and engineered football performance metrics.

The project includes:

* Data collection and preprocessing
* Exploratory Data Analysis (EDA)
* Feature engineering using rolling team statistics
* Logistic Regression baseline model
* Random Forest classification
* XGBoost classification
* Model evaluation and comparison

---

## Dataset

Data sourced from:

* football-data.co.uk

The dataset contains:

* Match results
* Goals scored
* Shots and shots on target
* Corners
* Fouls
* Team information
* Historical Premier League seasons

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib
* Jupyter Notebook

---

## Project Structure

```text
EPLInsightEngine/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_data_loading.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_logistic_regression.ipynb
│   ├── 06_random_forest.ipynb
│   └── 07_xgboost.ipynb
│
├── src/
│   └── data_loader.py
│
├── README.md
├── .gitignore
```

---

## Feature Engineering

Rolling historical statistics were created for each team, including:

* Average goals scored
* Average shots on target
* Average corners
* Average fouls

To avoid data leakage, rolling metrics were calculated using only previous matches via shifted rolling windows.

Example:

* Last 10-match attacking form
* Previous shots on target averages
* Historical team performance trends

---

## Models Implemented

### Logistic Regression

Used as a baseline classification model for match outcome prediction.

### Random Forest

Ensemble tree-based model used to capture nonlinear relationships between football statistics and match outcomes.

### XGBoost

Gradient boosting model used to improve predictive performance on structured football data.

---

## Model Performance

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | ~45%     |
| Random Forest       | ~49%     |
| XGBoost             | ~47%     |

Random Forest produced the strongest performance on the current feature set.

---

## Key Findings

* Home wins were predicted more accurately than draws
* Draws proved difficult to model due to class imbalance and football match variability
* Shots on target were among the most important predictive features
* Rolling form metrics provided stronger predictive power than raw match statistics alone

---

## Future Improvements

Potential future enhancements include:

* Expected Goals (xG) data
* Player-level statistics
* Elo ratings/team strength metrics
* Hyperparameter tuning
* Time-series cross validation
* Deployment as a web application

---



## Author

Ross Wadhams

Computer Science Graduate — First Class Honours
Aspiring Data Analyst / Data Scientist

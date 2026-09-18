# Project Statement

## Project Title

RUL Prediction Using Bayesian Linear Regression

## Problem Statement

Aircraft turbofan engines generate sensor and operating-condition data during their operation. Predicting the Remaining Useful Life (RUL) of an engine can help identify how many operating cycles remain before the engine reaches the end of its useful life.

The objective of this project is to develop a machine learning system that uses engine operating settings and sensor measurements to predict the Remaining Useful Life of turbofan engines.

The project uses the NASA C-MAPSS turbofan engine dataset and applies Bayesian Linear Regression to predict RUL for the FD001 and FD002 datasets.

## Scope

The project covers:

- Processing NASA C-MAPSS turbofan engine data.
- Calculating Remaining Useful Life for training data.
- Training a Bayesian Linear Regression model.
- Predicting Remaining Useful Life for test engine data.
- Evaluating predictions using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).
- Providing an interactive application for RUL prediction.
- Testing the main project modules.

The project is limited to the FD001 and FD002 datasets and the Bayesian Linear Regression model implemented in the project.

## Target Users

The project is intended for:

- Students learning machine learning and predictive maintenance.
- Researchers studying Remaining Useful Life prediction.
- Users interested in applying machine learning to aircraft engine sensor data.
- Developers who want to experiment with RUL prediction using the NASA C-MAPSS dataset.

## High-Level Features

### 1. Data Preparation

The system loads the NASA C-MAPSS dataset and converts the raw data into structured processed files.

For training data, Remaining Useful Life is calculated using the operating cycle information for each engine.

### 2. Bayesian Linear Regression

The system trains a Bayesian Linear Regression model using:

- 3 operating settings
- 21 sensor measurements

The model is trained separately using FD001 and FD002.

### 3. RUL Prediction

The trained model predicts the Remaining Useful Life of engine observations.

The system generates prediction files containing:

- Engine ID
- Cycle
- Predicted RUL

### 4. Model Evaluation

The system evaluates the predictions using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

### 5. Interactive Application

The application allows the user to:

- Select FD001 or FD002.
- Train the Bayesian Linear Regression model.
- Enter engine parameters manually.
- Select an existing engine and cycle from the training dataset.
- View the predicted Remaining Useful Life.

### 6. Automated Testing

The project includes tests for:

- Data processing
- RUL prediction
- Evaluation

A test aggregator is provided to run the project tests together.

## Expected Outcome

The expected outcome is a modular machine learning application capable of processing NASA C-MAPSS data, predicting Remaining Useful Life using Bayesian Linear Regression, evaluating prediction errors, and providing an interactive prediction interface.

## Project Limitations

The current project uses Bayesian Linear Regression as the prediction model and focuses only on the FD001 and FD002 datasets.

The interactive application is intended as a demonstration of the prediction system and is not intended to represent a production aircraft maintenance system.
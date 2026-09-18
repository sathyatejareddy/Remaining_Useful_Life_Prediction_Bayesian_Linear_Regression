# VITyarthi Project

**Name:** Nagilla Sathya Teja Reddy  
**Registration Number:** 25MIM10058  
**Course:** Fundamentals of AIML  
**Professor:** Atul Onkarrao Thakare  
**Slot:** A11 + A12 + A13  
**Course Code:** CSA2001  

---

# RUL Prediction Using Bayesian Linear Regression

## Overview

This project predicts the Remaining Useful Life (RUL) of aircraft turbofan engines using Bayesian Linear Regression.

The project uses the NASA C-MAPSS turbofan engine dataset and works with two datasets:

- FD001
- FD002

The same Bayesian Linear Regression approach is applied separately to both datasets.

## Features

- Data preparation and cleaning
- Remaining Useful Life calculation for training data
- Bayesian Linear Regression model training
- RUL prediction
- Model evaluation using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE)
- Interactive RUL prediction application
- Automated project testing
- Architecture, workflow, use case, sequence, and class diagrams

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Bayesian Linear Regression
- NASA C-MAPSS dataset

## Project Structure

```
RUL_Prediction_BLR/
│
├── app/
│   └── main.py
│
├── DATA/
│   ├── Raw/
│   │   ├── RUL_FD001.txt
│   │   ├── RUL_FD002.txt
│   │   ├── test_FD001.txt
│   │   ├── test_FD002.txt
│   │   ├── train_FD001.txt
│   │   └── train_FD002.txt
│   │
│   ├── Processed/
│   │   ├── test_FD001.csv
│   │   ├── test_FD002.csv
│   │   ├── train_FD001.csv
│   │   └── train_FD002.csv
│   │
│   └── Results/
│       ├── predictions_FD001.csv
│       └── predictions_FD002.csv
│
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│   ├── usecase.png
│   ├── sequence.png
│   └── class_diagram.png
│
├── src/
│   ├── data_processing.py
│   ├── rul_prediction.py
│   └── evaluation.py
│
├── tests/
│   ├── test_all.py
│   ├── test_data_processing.py
│   ├── test_evaluation.py
│   └── test_rul_prediction.py
│
├── .gitignore
├── README.md
├── requirements.txt
└── statement.md
```

## Functional Modules

### 1. Data Preparation and Cleaning

The raw NASA C-MAPSS data is loaded and converted into structured CSV files.

For the training data, Remaining Useful Life is calculated for each engine using its operating cycles.

### 2. RUL Prediction

A Bayesian Linear Regression model is trained using the operating settings and sensor measurements.

The trained model is then used to predict the Remaining Useful Life of test engines.

### 3. Model Evaluation and Error Calculation

The predicted RUL values are compared with the actual RUL values provided for the test engines.

The project uses:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

## Dataset

The project uses the NASA C-MAPSS turbofan engine dataset.

Two experiments are used:

- FD001
- FD002

FD001 contains one operating condition, while FD002 contains six operating conditions.

Each engine contains measurements recorded over multiple operating cycles.

The model uses 24 input features:

- 3 operating settings
- 21 sensor measurements

The target variable is Remaining Useful Life (RUL).

## Model Selection

The project uses Bayesian Linear Regression implemented using Scikit-learn's `BayesianRidge`.

Bayesian Linear Regression was selected as the prediction model because it provides a linear relationship between the input features and RUL while incorporating a Bayesian approach to estimate model parameters.

The same model is applied separately to FD001 and FD002.

The general prediction form can be represented as:

Predicted RUL = b0 + b1x1 + b2x2 + ... + b24x24

where the input features consist of the three operating settings and 21 sensor measurements.

## Evaluation Methodology

The model is evaluated separately for FD001 and FD002.

For each engine in the test dataset, the prediction corresponding to its final available operating cycle is selected.

This prediction is compared with the actual RUL value provided in the corresponding NASA C-MAPSS RUL file.

The following evaluation metrics are used:

- **Mean Absolute Error (MAE)** — measures the average absolute difference between the predicted RUL and the actual RUL.
- **Root Mean Squared Error (RMSE)** — measures the square root of the average squared difference between the predicted RUL and the actual RUL.

Lower error values indicate that the predictions are closer to the actual RUL values.

## Application

The project includes an interactive RUL prediction application located at:

`app/main.py`

The application allows the user to:

- Select FD001 or FD002.
- Train the Bayesian Linear Regression model.
- Choose an input method.
- Enter engine parameters manually, or select an existing engine and cycle from the training dataset.
- Obtain a predicted Remaining Useful Life.

When an existing training engine is selected, the application also displays its actual RUL so that the prediction can be compared with the known value.

## Testing

The project contains automated tests for:

- Data processing
- RUL prediction
- Evaluation

The test files are located in `tests/`.

All tests can be executed together using `tests/test_all.py`.

The tests verify that:

- Processed data files are created.
- RUL values are calculated correctly and contain valid values.
- Prediction files are created.
- Prediction data contains valid values.
- Error calculations work correctly.
- Perfect predictions produce zero error.

## Documentation and Design Diagrams

The project contains design diagrams in the `docs/` folder.

The diagrams include:

- `architecture.png` — System architecture
- `workflow.png` — Project workflow
- `usecase.png` — Use case diagram
- `sequence.png` — Sequence diagram
- `class_diagram.png` — Class diagram

These diagrams describe the system structure, workflow, user interactions, component interactions, and project modules.

## How to Run

### 1. Install Dependencies

Install the required Python packages using:

```
pip install -r requirements.txt
```

### 2. Data Processing

Run:

```
python src/data_processing.py
```

This processes the raw dataset and creates the processed CSV files.

### 3. RUL Prediction

Run:

```
python src/rul_prediction.py
```

This trains the Bayesian Linear Regression model and generates RUL predictions for FD001 and FD002.

### 4. Evaluation

Run:

```
python src/evaluation.py
```

This calculates the Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE) for both datasets.

### 5. Interactive Application

Run:

```
python app/main.py
```

The application provides an interactive interface for selecting the dataset and generating RUL predictions.

### 6. Testing

Run:

```
python tests/test_all.py
```

This executes all project tests together.

## Input Features

The model uses the following 24 input features:

- Setting1, Setting2, Setting3
- Sensor1 through Sensor21

Engine ID and Cycle are used for identifying and tracking engine data but are not used as model input features.

## Functional Requirements

- The system shall load and process the NASA C-MAPSS dataset.
- The system shall calculate Remaining Useful Life for training data.
- The system shall train a Bayesian Linear Regression model.
- The system shall predict Remaining Useful Life for test engine data.
- The system shall calculate prediction errors using MAE and RMSE.
- The system shall provide an interactive application for RUL prediction.
- The system shall allow the user to select between FD001 and FD002.

## Non-Functional Requirements

**Performance**
The system should process the available datasets and generate predictions within a reasonable execution time.

**Reliability**
The system should produce consistent results when the same data and model configuration are used.

**Maintainability**
The project should use separate modules for data processing, prediction, evaluation, application, and testing.

**Error Handling**
The application should handle invalid dataset selections, engine IDs, cycle values, and non-numeric user inputs without terminating unexpectedly.

## Future Enhancements

Possible future improvements include:

- Testing additional machine learning models.
- Feature selection and feature engineering.
- Hyperparameter tuning.
- Improved visualization of engine degradation.
- Comparing Bayesian Linear Regression with other RUL prediction methods.
- Developing more advanced RUL prediction approaches.
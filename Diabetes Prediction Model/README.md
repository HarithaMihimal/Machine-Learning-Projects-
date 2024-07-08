# Diabetes Prediction System

This project builds a system to predict whether a person is diabetic or not using the PIMA diabetes dataset. The system employs a Support Vector Machine (SVM) model for classification.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project utilizes the PIMA diabetes dataset to classify individuals as diabetic or non-diabetic. The system leverages the Support Vector Machine (SVM) algorithm for classification, providing an effective machine learning approach to tackle this health-related problem.

## Dataset
The dataset used is the PIMA diabetes dataset, which contains medical records for women of Pima Indian heritage. Each feature represents medical measurements such as glucose levels, blood pressure, and BMI. The target variable indicates whether the person is diabetic (1) or non-diabetic (0).

## Installation
To get started, clone this repository and install the required dependencies.

## Usage
Ensure you have the diabetes data file (`diabetes.csv`) in the project directory. Then, run the following script to train the model and make predictions:

## Model Training and Evaluation
The script performs the following steps:
1. Loads the PIMA diabetes dataset.
2. Preprocesses the dataset by splitting it into features (X) and target (Y).
3. Standardizes the feature data.
4. Divides the data into training and testing sets.
5. Trains an SVM model using the training set.
6. Makes predictions on the testing set.
7. Evaluates the model's accuracy.

## Results
The SVM model provides an accuracy of approximately 78-80% on the testing set, depending on the random state and data split.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

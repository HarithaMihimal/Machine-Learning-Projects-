# Rock or Mine Prediction System with SONAR Data

This project builds a system to predict whether an object is a rock or a mine using SONAR data. We employ a Logistic Regression model for our predictions.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Usage](#usage)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This project uses SONAR data to classify objects as either rocks or mines. The system leverages the Logistic Regression algorithm for classification, providing an accessible and straightforward machine learning approach to tackle this problem.

## Dataset
The dataset used is the SONAR dataset, which contains sonar returns bouncing off different surfaces. Each feature represents the energy within a particular frequency band, integrated over a certain period. The target variable indicates whether the object is a rock (R) or a mine (M).

## Usage
Ensure you have the SONAR data file (`sonar data.csv`) in the project directory. Then, run the following script to train the model and make predictions:

## Model Training and Evaluation
The script performs the following steps:
1. Loads the SONAR dataset.
2. Preprocesses the dataset by splitting it into features (X) and target (y).
3. Divides the data into training and testing sets.
4. Trains a Logistic Regression model using the training set.
5. Makes predictions on the testing set.
6. Evaluates the model's accuracy.

## Results
The Logistic Regression model provides an accuracy of approximately 82-85% on the testing set, depending on the random state and data split.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

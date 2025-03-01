# Machine-Failure-Prediction


This project predicts machine failures based on sensor data such as air temperature, machine temperature, torque, and other parameters. The goal is to predict potential failures in advance to prevent downtime and reduce maintenance costs.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Dataset](#dataset)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AryakumarMishra/Machine-Failure-Prediction.git
   ```

2. Navigate to the project directory:
   ```bash
   cd machine-failure-prediction
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Open the Jupyter notebook `Predictive_Maintenance.ipynb`.
2. Run the cells to load the dataset, preprocess the data, and train the 1D-CNN model.
3. To predict machine failure for a new input, use the trained model and input new sensor data.

## Model

This project uses a **1D Convolutional Neural Network (1D-CNN)** to predict machine failure. The model is trained on historical sensor data, which includes features like temperature, pressure, and torque, to classify whether a machine will fail or not.

## Dataset

The dataset used in this project is the **AI4I 2020 Predictive Maintenance Dataset**, which can be accessed from the following link:

- [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i%2B2020%2Bpredictive%2Bmaintenance%2Bdataset)

### Dataset Description

The AI4I 2020 Predictive Maintenance Dataset is a synthetic dataset that reflects real-world predictive maintenance data encountered in industrial settings. It consists of 10,000 data points with 14 features.

#### Features:
- **UID**: Unique identifier ranging from 1 to 10,000.
- **Product ID**: Consists of a letter (L, M, or H) for low, medium, or high product quality variants, respectively, along with a variant-specific serial number.
- **Air temperature [K]**: Generated using a random walk process, later normalized to a standard deviation of 2 K around 300 K.
- **Process temperature [K]**: Generated using a random walk process, normalized to a standard deviation of 1 K, added to the air temperature plus 10 K.
- **Rotational speed [rpm]**: Calculated from a power of 2860 W, overlaid with normally distributed noise.
- **Torque [Nm]**: Normally distributed torque values around 40 Nm with a standard deviation of 10 Nm.
- **Tool wear [min]**: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process.

#### Target Variable:
- **Machine failure**: A binary variable indicating whether the machine failed (1) or not (0) based on various failure modes.

### Failure Modes:
The **machine failure** label is set to 1 when any of the following failure modes occur:

- **Tool Wear Failure (TWF)**: The tool will fail at a randomly selected tool wear time between 200 and 240 minutes. The tool is replaced 69 times and fails 51 times.
- **Heat Dissipation Failure (HDF)**: Occurs when the difference between air and process temperature is below 8.6 K and the rotational speed is below 1380 rpm.
- **Power Failure (PWF)**: Occurs when the product of torque and rotational speed is below 3500 W or above 9000 W.
- **Overstrain Failure (OSF)**: Occurs when the product of tool wear and torque exceeds certain limits for different product variants (L, M, H).
- **Random Failures (RNF)**: A 0.1% chance of failure due to random factors, occurring very infrequently.

At least one of these failure modes must be true for the machine failure label to be set to 1.

## Results

The model achieved an accuracy of **98%** on the test set, with promising results for precision, recall, and F1-score. The trained model is saved as `cnn_model_final.h5` and can be used to predict machine failure for new sensor data.

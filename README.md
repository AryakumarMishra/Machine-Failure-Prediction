# AI-Based Machine Failure Prediction

This project uses machine learning to intelligently predict machine failures based on sensor data like temperature, rotational speed, torque, and tool wear. It aims to provide early warnings to reduce unplanned downtime and optimize maintenance schedules in industrial systems.

## Key Highlights

- Real-world industrial problem addressed using **AI**
- Final model: **XGBoost**, optimized with **SMOTE**, **threshold tuning**, and **feature scaling**
- Achieved **~99% accuracy**, **94% precision**, and **83% F1-score** on test data
- Fixed critical data leakage issue from earlier versions
- Feature engineering + hyperparameter tuning + model explainability
- Ready for deployment with Flask API

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Model](#model)
- [Dataset](#dataset)
- [Results](#results)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AryakumarMishra/Machine-Failure-Prediction.git
  ```

2. Navigate to the project directory:

   ```bash
   cd Machine-Failure-Prediction
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```


## Usage

1. Open the Jupyter Notebook `Predictive_Maintenance.ipynb`
2. Run all cells to:
   * Load and preprocess the data
   * Perform feature engineering
   * Apply SMOTE for class imbalance
   * Train and evaluate the XGBoost model
   * Save the trained model
3. Optionally, deploy via Flask API for real-time predictions

## Model

This project **originally used a 1D Convolutional Neural Network (1D-CNN)**.
However, after discovering **data leakage** due to dependent failure mode columns (`TWF`, `HDF`, etc.), those features were dropped and the pipeline was rebuilt.

Final model:

* **XGBoost Classifier**
* Tuned `scale_pos_weight` using `GridSearchCV`
* Threshold optimized at `0.95` for best trade-off between precision and recall

---

## Dataset

I used the [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i%2B2020%2Bpredictive%2Bmaintenance%2Bdataset) from UCI ML Repository.

### Features used:

* Air temperature \[K]
* Process temperature \[K]
* Rotational speed \[rpm]
* Torque \[Nm]
* Tool wear \[min]
* Product quality (one-hot encoded: `_L`, `_M`, `_H`)

### Label:

* `Machine failure`: Binary (0 = no failure, 1 = failure)

---

## Results

| Metric    | Value  |
| --------- | ------ |
| Accuracy  | 98.95% |
| Precision | 94.34% |
| Recall    | 73.53% |
| F1-Score  | 82.64% |
| ROC-AUC   | 86.69% |

These results were achieved **without any data leakage**, and can be ready for **production use**.

---

## Future Work

* Deploy with a simple React frontend or Streamlit dashboard
* Add LIME or SHAP for explainability
* Modify for real-time Failure Detections and Precautions
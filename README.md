# AI-Based Machine Failure Prediction

An end-to-end machine learning project to predict industrial machine failures based on sensor data such as temperature, rotational speed, torque, and tool wear. This system aims to enable proactive maintenance, reduce unplanned downtime, and improve operational efficiency.

---

## Key Features

* Tackles a real-world predictive maintenance problem using **AI**
* Final model: **XGBoost classifier** with tuned hyperparameters and imbalance handling (`scale_pos_weight`)
* Robust **feature engineering** and **threshold tuning** for optimal precision-recall balance
* Model interpretability with **SHAP** explanations integrated into the API
* Full stack deployment with **Flask backend** and **React frontend** for user-friendly predictions
* Achieves **\~99% accuracy**, **94% precision**, and strong **F1-score** without data leakage

---

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Model Details](#model-details)
* [Dataset](#dataset)
* [Results](#results)
* [Future Work](#future-work)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AryakumarMishra/Machine-Failure-Prediction.git
   ```

2. Navigate to project directory:

   ```bash
   cd Machine-Failure-Prediction
   ```

3. Create and activate a Python virtual environment:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # or source .venv/bin/activate on Mac
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```


## Usage

### Backend Setup

1. Run `main.py` to preprocess data, train the model, and generate necessary artifacts (model, scaler, background data for SHAP):

   ```bash
   python main.py
   ```

2. Start the Flask backend API server (`app.py`):

   ```bash
   python app/app.py
   ```

   This will run the backend on `http://localhost:5000`.

---

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install frontend dependencies (this will create the `node_modules` folder):

   ```bash
   npm install
   ```

3. Start the React development server:

   ```bash
   npm start
   ```

   This will run the frontend on `http://localhost:3000` and automatically open your browser.

---

### How to Use

* Open your browser to `http://localhost:3000`
* Use the form to input sensor values and product quality
* The app will call the Flask API to get the failure prediction and feature explanations
* View the prediction probability, risk level, and SHAP feature importance directly on the UI

---

### Notes

* Make sure your Python virtual environment (`.venv`) is activated when running backend commands.
* Node.js (version 16+) and npm must be installed on your system to run the React frontend.
* The frontend and backend run independently but communicate via HTTP requests.

---

## Model Details

Originally explored a 1D-CNN approach but discovered data leakage from failure mode columns (e.g., `TWF`, `HDF`). After removing these, rebuilt the pipeline with:

* **XGBoost Classifier**
* Hyperparameter tuning with `GridSearchCV` (including `scale_pos_weight=2`)
* Threshold optimized at 0.95 for precision-recall tradeoff
* SHAP for model interpretability

---

## Dataset

Based on the [AI4I 2020 Predictive Maintenance Dataset](https://archive.ics.uci.edu/dataset/601/ai4i%2B2020%2Bpredictive%2Bmaintenance%2Bdataset) from UCI Machine Learning Repository.

### Features

* Air temperature \[K]
* Process temperature \[K]
* Rotational speed \[rpm]
* Torque \[Nm]
* Tool wear \[min]
* Product quality (encoded as one-hot `_L`, `_M`, `_H`)

### Target

* Machine failure (binary: 0 = no failure, 1 = failure)

---

## Results

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 98.95% |
| Precision | 94.34% |
| Recall    | 73.53% |
| F1-Score  | 82.64% |
| ROC-AUC   | 86.69% |

> These metrics reflect a robust model ready for production deployment, with explainability and a user-friendly frontend.

---

## Future Work

* Implement **real-time prediction simulation** with streaming sensor data
* Improve frontend UI/UX for clearer visualization and interaction
* Integrate **LIME/SHAP** explanations directly in the React app
* Containerize with **Docker** and implement CI/CD pipelines for MLOps
* Expand to multi-class failure modes and anomaly detection

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from data_loader import load_data, basic_eda
from feature_engineering import encode_and_engineer
from model_training import train_model
from model_evaluation import evaluate_model
import joblib

if __name__ == "__main__":
    data = load_data('data/pred_maintenance.csv')  # adjusted path
    basic_eda(data)

    processed_data = encode_and_engineer(data)

    model, x_test, y_test, scaler, x_train = train_model(processed_data)

    evaluate_model(model, x_test, y_test, threshold=0.95)

    # Save model and scaler
    joblib.dump(model, 'models/xgb_model.joblib')
    joblib.dump(scaler, 'models/scaler.joblib')

    # Save x_train for SHAP background data
    x_train.to_csv('data/x_train_background.csv', index=False)

    print("Model, scaler, and background data saved!")

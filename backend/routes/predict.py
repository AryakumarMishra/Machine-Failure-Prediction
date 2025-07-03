from flask import Blueprint, request, jsonify
import joblib
import pandas as pd
from utils.preprocessing import preprocess_input
from utils.shap_utils import get_shap_values

predict_bp = Blueprint('predict', __name__)

model = joblib.load('models/xgb_model.joblib')
scaler = joblib.load('models/scaler.joblib')
background_data = pd.read_csv('data/x_train_background.csv')
threshold = 0.95

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.json
    try:
        print("🔥 Incoming JSON:", data)
        input_df = preprocess_input(data, background_data.columns)
        scaled = scaler.transform(input_df)
        proba = model.predict_proba(scaled)[0][1]

        shap_values = get_shap_values(model, background_data, input_df)

        return jsonify({
            'probability': float(round(proba, 4)),
            'risk_level': risk_text(proba),
            'shap_values': [float(val) for val in shap_values]
        })


    except Exception as e:
        return jsonify({'error': str(e)}), 500

def risk_text(prob):
    if prob < 0.40:
        return 'Low'
    elif prob < 0.75:
        return 'Moderate'
    elif prob < 0.91:
        return 'High'
    else:
        return 'Critical'

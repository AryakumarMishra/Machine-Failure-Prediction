import shap

def get_shap_values(model, background_data, input_df):
    explainer = shap.Explainer(model, background_data)
    shap_vals = explainer(input_df)
    return shap_vals.values[0].tolist()

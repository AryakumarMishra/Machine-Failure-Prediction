from sklearn.metrics import (
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score
)

def evaluate_model(model, x_test, y_test, threshold=0.95):
    # Predict probabilities
    y_proba = model.predict_proba(x_test)[:, 1]
    y_pred_custom = (y_proba >= threshold).astype(int)

    print("Classification Report:")
    print(classification_report(y_test, y_pred_custom, digits=4))

    print("Accuracy:", accuracy_score(y_test, y_pred_custom))
    print("Precision:", precision_score(y_test, y_pred_custom))
    print("Recall:", recall_score(y_test, y_pred_custom))
    print("F1-Score:", f1_score(y_test, y_pred_custom))
    print("ROC-AUC-SCORE:", roc_auc_score(y_test, y_pred_custom))

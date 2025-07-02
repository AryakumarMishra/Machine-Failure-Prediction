from typing import Tuple, cast
from numpy.typing import NDArray
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

def train_model(data: pd.DataFrame, target_column: str = 'Machine failure') -> Tuple[XGBClassifier, NDArray[np.float64], pd.Series, StandardScaler, pd.DataFrame]:
    x = data.drop(columns=[target_column])
    y = data[target_column]

    x_train, x_test, y_train, y_test = train_test_split(
        x, y, stratify=y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    x_train_scaled: NDArray[np.float64] = scaler.fit_transform(x_train)
    x_test_scaled: NDArray[np.float64] = scaler.transform(x_test)

    smote = SMOTE(random_state=42)
    
    # Cast to expected return type to satisfy type checker
    resampled = smote.fit_resample(x_train_scaled, y_train.to_numpy())
    x_resampled_raw, y_resampled_raw = cast(
        Tuple[NDArray[np.float64], NDArray[np.int64]],
        resampled
    )

    model = XGBClassifier(
        objective='binary:logistic',
        scale_pos_weight=2,
        learning_rate=0.03,
        max_depth=5,
        n_estimators=500,
        subsample=0.8,
        colsample_bytree=0.8,
        gamma=1,
        reg_alpha=0.3,
        reg_lambda=1,
        use_label_encoder=False,
        eval_metric='logloss',
        random_state=42
    )

    model.fit(x_resampled_raw, y_resampled_raw)

    return model, x_test_scaled, y_test, scaler, x_train

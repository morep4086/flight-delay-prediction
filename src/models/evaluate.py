import joblib
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score
from sklearn.model_selection import train_test_split
from src.data.data_loader import load_config, load_raw_data
from src.data.data_preprocessing import preprocess_data
from src.features.feature_builder import build_features

def evaluate():
    config = load_config()
    df = load_raw_data(config)
    df_processed = preprocess_data(df, config)
    X, y = build_features(df_processed)
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = joblib.load('models/best_model.pkl')
    preds = model.predict(X_test)

    rmse = mean_squared_error(y_test, preds, squared=False)
    mae = mean_absolute_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    accuracy = accuracy_score(y_test, preds)

    print(f"Evaluation Results:\nAccuracy: {accuracy:.4f}\nRMSE: {rmse:.4f}\nMAE: {mae:.4f}\nR^2 Score: {r2:.4f}")

if __name__ == '__main__':
    evaluate()

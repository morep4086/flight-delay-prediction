import joblib
import pytest
from src.data.data_loader import load_config, load_raw_data
from src.data.data_preprocessing import preprocess_data
from src.features.feature_builder import build_features

def test_model_prediction():
    config = load_config()
    df = load_raw_data(config)
    df_processed = preprocess_data(df, config)
    X, y = build_features(df_processed)
    model = joblib.load('models/best_model.pkl')
    preds = model.predict(X.head(5))
    assert len(preds) == 5
    assert all(pred in [0, 1] for pred in preds)

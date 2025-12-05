import pytest
from src.data.data_loader import load_raw_data, load_config
from src.data.data_preprocessing import preprocess_data
from src.features.feature_builder import build_features

def test_features_shape():
    config = load_config()
    df = load_raw_data(config)
    df_processed = preprocess_data(df, config)
    X, y = build_features(df_processed)
    assert len(X) == len(y)
    assert 'PEAK_HOUR' in X.columns

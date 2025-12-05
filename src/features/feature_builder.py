import pandas as pd

def build_features(df):
    # Features are already created in preprocessing
    # Just separate features and target
    feature_cols = [col for col in df.columns if col not in ['IS_DELAY']]
    X = df[feature_cols]
    y = df['IS_DELAY']
    return X, y
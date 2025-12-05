import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from src.data.data_loader import load_config, load_raw_data
from src.data.data_preprocessing import preprocess_data
from src.features.feature_builder import build_features

def train_models():
    config = load_config()
    df = load_raw_data(config)
    df_processed = preprocess_data(df, config)
    X, y = build_features(df_processed)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train simple Random Forest for speed
    rf = RandomForestClassifier(n_estimators=5, random_state=42)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)
    rf_acc = accuracy_score(y_test, rf_preds)

    print(f"Random Forest Accuracy: {rf_acc:.4f}")
    
    # Create models directory if it doesn't exist
    import os
    os.makedirs('models', exist_ok=True)
    
    joblib.dump(rf, 'models/best_model.pkl')
    print("Best model (Random Forest) saved as best_model.pkl")

if __name__ == '__main__':
    train_models()
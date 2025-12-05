import joblib
import pandas as pd
import sys

def predict(input_csv=None):
    model = joblib.load('models/best_model.pkl')

    # Load and preprocess input features
    if input_csv is None:
        input_csv = 'data/processed/processed_flights.csv'
    # Use processed data directly
    if input_csv is None:
        input_csv = 'data/processed/processed_flights.csv'
    data = pd.read_csv(input_csv, nrows=100)  # Limit for display
    
    # Remove target column if present
    feature_cols = [col for col in data.columns if col not in ['IS_DELAY']]
    X = data[feature_cols]

    preds = model.predict(X)
    
    print("\nFLIGHT DELAY PREDICTION RESULTS")
    print("="*50)
    print("Flight#  Predicted    Status")
    print("-"*50)
    
    delayed_count = 0
    for i, pred in enumerate(preds[:20]):  # Show first 20
        pred_text = "Delayed" if pred == 1 else "On Time"
        if pred == 1:
            delayed_count += 1
        print(f"{i+1:7d}  {pred_text:9s}    {'[DELAY]' if pred == 1 else '[OK]'}")
    
    print(f"\nSUMMARY:")
    print(f"Total Flights Analyzed: {len(preds)}")
    print(f"Predicted Delays: {sum(preds)}")
    print(f"On Time Flights: {len(preds) - sum(preds)}")
    print(f"Delay Rate: {sum(preds)/len(preds)*100:.1f}%")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python predict.py <input_csv>")
    else:
        predict(sys.argv[1])

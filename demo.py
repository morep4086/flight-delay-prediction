import pandas as pd
import joblib

# Load model and data
model = joblib.load('models/best_model.pkl')
df = pd.read_csv('data/processed/processed_flights.csv', nrows=10)
X = df[[col for col in df.columns if col != 'IS_DELAY']]
preds = model.predict(X)
actual = df['IS_DELAY'].values

print("FLIGHT DELAY PREDICTION RESULTS")
print("="*50)
print("Flight#  Predicted    Actual      Correct?")
print("-"*50)

for i in range(10):
    pred_text = "Delayed" if preds[i] == 1 else "On Time"
    actual_text = "Delayed" if actual[i] == 1 else "On Time"
    correct = "YES" if preds[i] == actual[i] else "NO"
    print(f"{i+1:7d}  {pred_text:9s}  {actual_text:9s}     {correct}")

print(f"\nAccuracy: {sum(preds == actual)}/{len(preds)} = {sum(preds == actual)/len(preds)*100:.1f}%")
print(f"Total Delayed: {sum(actual)} out of {len(actual)} flights")
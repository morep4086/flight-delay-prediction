import pandas as pd

def preprocess_data(df, config):
    # Your dataset already has DEP_DEL15 (delay indicator)
    df['IS_DELAY'] = df['DEP_DEL15']
    
    # Extract hour from time block
    df['HOUR'] = df['DEP_TIME_BLK'].str[:2].astype(int)
    df['PEAK_HOUR'] = ((df['HOUR'] >= 6) & (df['HOUR'] <= 10)) | ((df['HOUR'] >= 17) & (df['HOUR'] <= 20))
    df['PEAK_HOUR'] = df['PEAK_HOUR'].astype(int)
    
    # One-hot encode categorical variables
    df = pd.get_dummies(df, columns=['CARRIER_NAME', 'DEPARTING_AIRPORT'], drop_first=True)
    
    # Drop unnecessary columns
    cols_to_drop = ['DEP_TIME_BLK', 'DEP_DEL15']
    df = df.drop(columns=[col for col in cols_to_drop if col in df.columns])
    
    # Save processed data
    df.to_csv(f"{config['data']['processed_path']}processed_flights.csv", index=False)
    return df
import pandas as pd
import yaml

def load_config(config_path='src/config/config.yaml'):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def load_raw_data(config):
    # Use your real dataset (sample for speed)
    import os
    if os.path.exists('data/raw/full_data_flightdelay.csv'):
        df = pd.read_csv('data/raw/full_data_flightdelay.csv', nrows=100)
    else:
        df = pd.read_csv(config['data']['raw_path'])
    return df

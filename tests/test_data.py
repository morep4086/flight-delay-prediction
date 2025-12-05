import pytest
from src.data.data_loader import load_raw_data, load_config

def test_load_data():
    config = load_config()
    df = load_raw_data(config)
    assert not df.empty
    assert 'DEP_DELAY' in df.columns

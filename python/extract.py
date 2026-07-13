import pandas as pd
from config import CSV_FILE

def extract_data():
    return pd.read_csv(CSV_FILE)
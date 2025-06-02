import pandas as pd

def load_logs(file):
    df = pd.read_csv(file)
    return df
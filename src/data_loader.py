import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def basic_eda(data):
    print(f"'Head'\n{data.head()}\n")
    print(f"'Info'\n{data.info()}\n")
    print(f"'Description'\n{data.describe()}\n")
    print(f"'Null Values?'\n{data.isnull().sum()}\n")
    print(f"'Unique Values'\n{data.nunique()}\n")
    print(f"'Duplicates?'\n{data.duplicated().sum()}")

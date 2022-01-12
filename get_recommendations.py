import pandas as pd

def get_recommendations():
    df = pd.read_csv("./new_profile.csv",delimiter = "|",)
    df = df.drop([0])
    df.columns = df.columns.str.replace(' ', '')
    for i in df.columns:
        df[i] = df[i].str.replace(' ', '')
    pay_load = df.to_json()
    return pay_load

if __name__ == "__main__":
    print(get_recommendations())
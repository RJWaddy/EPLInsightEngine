import pandas as pd
import glob

def load_data():
    files = glob.glob("../data/raw/*.csv")
    print(files)
    print("Hello")
    dfs = []

    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)

    epl_data = pd.concat(dfs, ignore_index=True)

    return epl_data


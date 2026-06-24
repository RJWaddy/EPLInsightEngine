import pandas as pd
import glob

def load_data():
    files = glob.glob("../data/raw/*.csv")
    dfs = []

    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)

    epl_data = pd.concat(dfs, ignore_index=True)

    print(epl_data.count())


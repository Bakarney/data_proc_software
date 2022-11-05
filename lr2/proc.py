import pandas as pd
import os


def pollutantmean(directory: str, pollutant: str, ids: int or list) -> int:
    if isinstance(ids, int):
        ids = [ids]

    df = pd.concat([pd.read_csv(directory + "/" + format(i, "03d") + ".csv") for i in ids])
    mean = df[pollutant].mean()

    return mean


def complete(directory: str, ids: int or list) -> dict:
    if isinstance(ids, int):
        ids = [ids]

    dfs = {i: pd.read_csv(directory + "/" + format(i, "03d") + ".csv") for i in ids}
    dfs = {i: df[(df["sulfate"].notnull()) & (df["nitrate"].notnull())] for i, df in dfs.items()}
    lengths = {i: len(df) for i, df in dfs.items()}

    return lengths


def corr(directory: str, threshold: int) -> list:
    dfs = [pd.read_csv(directory + "/" + file) for file in os.listdir(directory)]
    dfs = [df[(df["sulfate"].notnull()) & (df["nitrate"].notnull())] for df in dfs]
    lengths = [len(df) for df in dfs]
    correlations = [df["sulfate"].corr(df["nitrate"]) for i, df in enumerate(dfs) if lengths[i] >= threshold]

    return correlations

import json
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.DataFrame(json.load(open("result.json", "r")))

mapping = {}
for i in df.keys():
    mapping[i] = i
    mapping[i] = mapping[i].replace("metadata_", "")
    mapping[i] = mapping[i].replace("info_", "")
    mapping[i] = mapping[i].replace("participants_", "player")

df = df.rename(columns=mapping)

for i in df.keys():
    print(i)

picks = df[["player0_championName"]] \
    .groupby("player0_championName", as_index=False) \
    .size() \
    .rename(columns={"player0_championName": "champion", "size": "count"}) \
    .set_index("champion") \
    .fillna(0)
for i in range(1, 10):
    tmp = df[["player{}_championName".format(i)]] \
        .groupby("player{}_championName".format(i), as_index=False) \
        .size() \
        .rename(columns={"player{}_championName".format(i): "champion"}) \
        .set_index("champion") \
        .fillna(0)
    picks = picks.join(tmp)
    picks["count"] += picks["size"]
    picks = picks[["count"]]

sum_picks = picks.sum()[0] / 10
picks["pick_rate"] = picks["count"] / sum_picks

picks \
    .sort_values("pick_rate", ascending=False) \
    .head(10) \
    .plot(y="pick_rate", kind="bar")

plt.figure()
picks["top"] = np.where(picks["pick_rate"] >= 0.1, "Popular", "Unpopular")
picks \
    .groupby("top") \
    .size() \
    .plot(subplots=True, kind="pie", autopct="%.0f%%")

picks[["top", "count"]] \
    .groupby("top") \
    .sum() \
    .plot(subplots=True, kind="pie", autopct="%.0f%%")

games_dur = pd.DataFrame()
games_dur["gameDuration"] = df["gameDuration"] / 60
games_dur.plot(kind='hist')

plt.figure()
team_kills = pd.DataFrame({"blueTeam": [], "redTeam": []})
for i, team in enumerate(["blueTeam", "redTeam"]):
    team_kills[team] = df["player{}_kills".format(i * 5)]
    for j in range(1, 5):
        team_kills[team] += df["player{}_kills".format(i * 5 + j)]

team_kills.groupby("blueTeam").size().plot(color="blue")
team_kills.groupby("redTeam").size().plot(color="red")

plt.show()

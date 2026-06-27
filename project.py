# import required libraries
import pandas as pd
import numpy as np

# load dataset
deliveries = pd.read_csv("deliveries.csv")
matches = pd.read_csv("matches.csv")

# Explore data
print(deliveries.shape)
print(matches.shape)

print(deliveries.head())
print(matches.head())

print(deliveries.info())
print(matches.info())

print(deliveries.columns)
print(matches.columns)

# Check null values
print(deliveries.isnull().sum())
print(matches.isnull().sum())

# Fill null values
matches["winner"] = matches["winner"].fillna("No Result")
print(matches)

matches["player_of_match"] = matches["player_of_match"].fillna("No Award")
print(matches)

matches["city"] = matches["city"].fillna("Unknown")
print(matches)

# Check duplicate data
print("Matches duplicates:", matches.duplicated().sum())
print("Deliveries duplicates:", matches.duplicated().sum())

# check shape of data
print("Matches duplicates:", matches.shape)
print("Deliveries duplicates:", deliveries.shape)


# EDA operations

# top teams by win
team_wins = matches["winner"].value_counts().head(10)
print(team_wins)

# Top run score
top_batsman = deliveries.groupby("batter")["batsman_runs"].sum()
top_batsman = top_batsman.sort_values(ascending= False)
print(top_batsman.head(10))

# Top wicket taker
wicket = deliveries[deliveries["dismissal_kind"].notna()]
top_bowler = wicket.groupby("bowler").size()
top_bowler = top_bowler.sort_values(ascending=False)
print(top_bowler.head(10))

# Most six hit by cricketer 
sixes = deliveries[deliveries["batsman_runs"] == 6]
top_six = sixes.groupby("batter").size()
top_six = top_six.sort_values(ascending=False)
print(top_six.head(10))

# Most four hit by cricketer 
four = deliveries[deliveries["batsman_runs"] == 4]
top_six = four.groupby("batter").size()
top_six = top_six.sort_values(ascending=False)
print(top_six.head(10))

# Toss impact on Match result
matches["toss_match_win"] = matches["toss_winner"] == matches["winner"]
matches["toss_match_win"].value_counts()
percentage = matches["toss_match_win"].mean() * 100
print("Toss winner match win %:", percentage)

# Merge dataset
ipl = pd.merge(deliveries,matches,left_on="match_id",right_on="id",how="inner")
print(ipl.shape)
print(ipl.head())

batting = ipl.groupby("batter")["batsman_runs"].sum().sort_values(ascending=False).head(10)
print(batting)

wickets = ipl[ipl["dismissal_kind"].notna()]
bowling = wickets.groupby("bowler").size().sort_values(ascending=False).head(10)
print(bowling)

venue_runs = ipl.groupby("venue")["total_runs"].sum().sort_values(ascending=False).head(10)
print(venue_runs)

batting.to_csv("top_batsmen.csv")
bowling.to_csv("top_bowlers.csv")
venue_runs.to_csv("venue_runs.csv")

ipl["toss_match_win"] = ipl["toss_winner"] == ipl["winner"]
ipl["toss_match_win"].mean() * 100

ipl["winner"].value_counts()

matches["target_runs"] = matches["target_runs"].fillna(0)
matches["target_overs"] = matches["target_overs"].fillna(0)
matches.to_csv("matches_clean.csv", index=False)

print(matches["venue"].unique())
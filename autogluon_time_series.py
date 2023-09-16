import pandas as pd
from autogluon.timeseries import TimeSeriesDataFrame, TimeSeriesPredictor

df = pd.read_csv("2023_smartFarm_AI_hackathon_dataset.csv")
df.head()
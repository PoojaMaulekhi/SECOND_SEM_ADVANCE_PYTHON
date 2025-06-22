
import numpy as np
import pandas as pd

ipl=pd.read_csv('./datasets-session-16/kohli_ipl.csv')

print(ipl[['Team1','Team2','Team3']])
ipl.iloc(5)

# find all winners
mask=ipl['MatchNumber']=='Final'
new_df=ipl[mask]
new_df[['Season','WinningTeam']]

ipl[ipl['MatchNumber']]

# iloc =>search using  index position
# loc => search using index labels
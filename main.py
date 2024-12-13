'''Perform Crime Analysis on dataset'''
from IPython.display import display

from mylib.lib import read_df, summarize_df, hist_time_occ

df = read_df("Crime_Data_from_2020_to_Present.csv.zip")
print('Crime Dataset Loaded from zipped csv file.')

print('Summary Statistics:')
display(summarize_df(df))

print('Histogram Plot:')
hist_time_occ(df)

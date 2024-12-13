'''This file contains methods to read a crime dataset based on LAPD.
It produces summary statistics and data visualizations'''

import zipfile
import pandas as pd
import matplotlib.pyplot as plt


def read_df(filepath):
    '''Reads a zipped csv file and returns a pandas dataframe'''
    with zipfile.ZipFile(filepath) as z:
        with z.open("Crime_Data_from_2020_to_Present.csv") as f:
            df = pd.read_csv(f)
    df['TimeOccHr'] = df['TIME OCC']//100 + df['TIME OCC']%100/60
    return df

def summarize_df(df):
    '''Returns summary statistics of the dataframe'''
    return df.describe()

def hist_time_occ(df):
    '''Plots a histogram of the time of day when crimes occur'''
    plt.figure(figsize = (15,6))
    h = (df['TimeOccHr']).hist(bins = 24)
    h.set(xlabel = "Hour of Day", ylabel = "Crime Occurences",
          title = "Distribution of Crime Occurences over Time of Day")
    plt.xticks(ticks = [2*i for i in range(13)])
    plt.show(block = False)
    return "Histogram Loaded"
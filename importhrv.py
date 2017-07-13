#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 12:10:10 2017

@author: christopher
"""

import pandas as pd
from pandas import DataFrame
import glob
import datetime
import re
path = 'data/eliteHRV/export/'

def createTimestamps(df,time):    
    time = datetime.datetime.strptime(time, '%Y-%m-%d %H-%M-%S')

    firstTime = time + datetime.timedelta(milliseconds=0) 
    curTime = time
    lastTime = time
    df["time"] = firstTime
    for i, row in df.iterrows():
        if i == 0:
            curTime = time
            lastTime = curTime
            df.loc[i, 'time'] = time + datetime.timedelta(milliseconds=0)
        else:

            curTime = lastTime + datetime.timedelta(milliseconds=row["interval in seconds"])
            df.loc[i, 'time']  = curTime
            lastTime = curTime

    return df


def importDriveData(file = path,type = "*.txt"):
    print("Reading files")
    df = DataFrame()

    allFiles = glob.glob(path + type)
    allFiles.sort()
   # print(allFiles)
    count = 0
    for file in allFiles:
        time = ((re.sub(r'.*/20', '20', file)).rsplit('.txt', 1))[0]
        print(time)
        
        
        print("File: ", file)
        if (count == 0): # first run
             df = pd.read_table(file, skiprows=None, header=None, delim_whitespace=True)
             df.columns = ["interval in seconds"]
            # print("Create timestamps")
             df = createTimestamps(df,time)
             
        else:
             dftemp = pd.read_table(file, skiprows=None, header=None, delim_whitespace=True)
             dftemp.columns = ["interval in seconds"]
             dftemp= createTimestamps(dftemp,time)
             df = df.append(dftemp)
             
        count+=1
    

    return df

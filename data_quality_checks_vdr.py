#!/usr/bin/env python
# coding: utf-8

# In[1]:


###############################################################################
##
## Name: data_quality_checks_vdr.ipynb
## Purpose: 
## Author: VDR
## Email: dellarocca.vale@gmail.com
## Date: 2021-04-09
## Version: v1
##
###############################################################################
##
## Notes: Same output of what provided in April, just rewritten in Python
##
###############################################################################


## 0. General set up ----------------------------------------------------------


# Libraries
import os
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from functools import reduce



## 1. Function definition -----------------------------------------------


def data_quality_checks_f(df):
    
    
    
    
    ## This part plots histograms to check for outliers
    for i in range(0,len(df.columns)):
        dataset_temp = df.copy()
        dataset_temp["temp_col"] = dataset_temp.iloc[:, i]

        if pd.api.types.is_numeric_dtype(dataset_temp["temp_col"]) == True:
            plt.hist(x=dataset_temp["temp_col"], bins='auto', color='#0504aa',alpha=0.7, rwidth=0.85)
            plt.title(df.columns[i])
            temp_name = str(df.name) + "_" + str(df.columns[i]) + ".pdf"
            plt.savefig(temp_name)
            plt.clf()

            
    ## This part saves a csv with basic info on the data
    temp_name_2 = str(df.name) + ".csv"
    dataset_temp.describe().to_csv(temp_name_2) 

    
    
    ## This parts prints the missing rate in each column
    print("Missing rate")

    percent_missing = df.isnull().sum() * 100/len(df)
    print(percent_missing)
    
    
    
    ## This parts prints the Zero rate in each column
    print("Zero rate")
    
    for i in range(0,len(df.columns)):

        dataset_temp = df.copy()
        dataset_temp["temp_col"] = dataset_temp.iloc[:, i]

        print(df.columns[i])
        percent_zero = dataset_temp.loc[dataset_temp['temp_col'] == 0,'temp_col'].count()/dataset_temp['temp_col'].count()
        print(percent_zero)
        
        


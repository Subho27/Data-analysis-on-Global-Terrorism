# -*- coding: utf-8 -*-

""" This is the function module. """

#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
#
#str1 = "Welcome to the DATA ANALYSIS OF GLOBAL TERRORISM"
#print(str1.center(58,"*"))
#
#dataset = pd.read_csv("Data.csv",encoding="latin")
#df = pd.DataFrame(dataset)
##print(list(df.columns))
#
## =============================================================================
## renaming the columns
## =============================================================================
#
#df.rename(columns = {"iyear":"year","imonth":"month","iday":"day",\
#                    "country_txt":"country","attacktype1_txt":"attacktype",\
#                    "targtype1_txt":"targtype","corp1":"corporation",\
#                    "target1":"target","natlty1_txt":"nationality",\
#                    "gname":"group","weaptype1_txt":"weaptype",\
#                    "weapsubtype1_txt":"weapsubtype","nkill":"kill","nwound":"wound",\
#                    "propextent_txt":"propextent"},inplace = True)

from main import df,np,plt,pd

emp=df.groupby(["year"])["kill"].agg(np.sum)
year=[2012,2013,2014,2015,2016]
plt.pie(emp,labels=year)
#plt.legend()
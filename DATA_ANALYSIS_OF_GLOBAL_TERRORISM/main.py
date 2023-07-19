# -*- coding: utf-8 -*-

""" This is the main module. """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import functions

str1 = "Welcome to the DATA ANALYSIS OF GLOBAL TERRORISM"
print(str1.center(58,"*"))

dataset = pd.read_csv("Data.csv",encoding="latin")
df = pd.DataFrame(dataset)
#print(list(df.columns))

# =============================================================================
# renaming the columns
# =============================================================================

df.rename(columns = {"iyear":"year","imonth":"month","iday":"day",\
                    "country_txt":"country","attacktype1_txt":"attacktype",\
                    "targtype1_txt":"targtype","corp1":"corporation",\
                    "target1":"target","natlty1_txt":"nationality",\
                    "gname":"group","weaptype1_txt":"weaptype",\
                    "weapsubtype1_txt":"weapsubtype","nkill":"kill","nwound":"wound",\
                    "propextent_txt":"propextent"},inplace = True)
#print(list(df.columns))

# =============================================================================
# deleting column with neglible number of values
# =============================================================================

#lst = list(df["ransomamt"])
#print(len(lst))
#print(df["ransomamt"].count())
df = df.drop("ransomamt",1)
#print(list(df.columns))   #Number of non-NaN values is very less than total number of rows

# =============================================================================
# creating one date column 
# =============================================================================

df["date"] = df["year"].apply(str)+"-"+df["month"].apply(str)+"-"+df["day"].apply(str)
##print(df["date"].head(12))
#df = df.drop(["year","month","day"],axis = 1)
#print(list(df.columns))

# =============================================================================
# handling NaN values
# =============================================================================

i = j = 0
lst = {}
while j<len(df.index):
    flag = 0
    lst = df.iloc[j].to_dict()
    for data in lst.values():
        if pd.isnull(data):
            flag = 1
            break
    if flag == 0:
        break
    j=j+1

for col_name,value in lst.items():
    try:
        num = int(value)
        mean_value = df[col_name].mean()
        df[col_name]=df[col_name].fillna(round(mean_value))
    except Exception as e:
        df[col_name]=df[col_name].fillna("Missing")

#print(df["kill"][182])
#print(df["wound"][182])
#print(df["weapdetail"][182])

# =============================================================================
# functions
# =============================================================================

while True:
    print("Data analysis broad categories: ")
    print("1.Year-wise.")
    print("2.Country-wise.")
    print("3.Attack-typewise.")
    print("4.Target-typewise.")
    print("5.Target-wise.")
    print("6.Groupname-wise")
    print("7.Exit.")
    try:
        ch = int(input("Enter your choice: "))
    except Exception as e:
        print("Enter a valid input.")
        continue
    if ch == 1:
        empdf = df.groupby(["year"])
        while True:
            print("Incidents year-wise :")
            print("1.Year-wise number of incidents.")
            print("2.Year-wise number of kills.")
            print("3.Year-wise number of wounds.")
            print("4.Year-wise comparison of kills and wounds.")
            print("5.Year-wise top 5 weapons used for terrorist activity.")
            print("6.Year-wise top 5 countries that got attacked.")
            print("7.Year-wise top 5 targets.")
            print("8.Exit.")
            try:
                choice = int(input("Enter your choice: "))
            except Exception as e:
                print("Enter a valid input.")
                continue
            if choice == 1:
                tempdf = empdf["city"].agg(np.count_nonzero)
                p = tempdf.plot(kind = "bar")
                p.set_xlabel("Year")
                p.set_ylabel("Number of incidents")
                plt.show()
            elif choice == 2:
                tempdf = empdf["kill"].agg(np.sum)
                p = tempdf.plot(kind = "bar")
                p.set_xlabel("Year")
                p.set_ylabel("Number of kills")
                plt.show()
            elif choice == 3:
                tempdf = empdf["wound"].agg(np.sum)
                p = tempdf.plot(kind = "bar")
                p.set_xlabel("Year")
                p.set_ylabel("Number of wounds")
                plt.show()
            elif choice == 4:
                tempdf = empdf["kill"].agg(np.sum).tolist()
                tempdf1 = empdf["wound"].agg(np.sum).tolist()
                tempdf2 = np.arange(len([name for name,group in empdf]))
                plt.bar(tempdf2,tempdf,width=0.2,label="kill")
                plt.bar(tempdf2+0.2,tempdf1,width=0.2,label="wound")
                plt.legend()
                plt.show()
            elif choice == 5:
                for name,group in empdf:
                    tempdf=df.loc[(df["year"]==name)].groupby(["weaptype"])["weaptype"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf.plot(kind="pie",subplots=True,radius=0.75,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 6:
                for name,group in empdf:
                    tempdf=df.loc[(df["year"]==name)].groupby(["country"])["country"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf.plot(kind="pie",subplots=True,radius=0.75,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 7:
                for name,group in empdf:
                    tempdf=df.loc[(df["year"]==name)].groupby(["target"])["target"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf.plot(kind="pie",subplots=True,radius=0.75,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 8:
                break
            else:
                print("Please Enter between 1 to 8.")
    elif ch == 2:
        empdf = df.groupby(["country"])
        while True:
            print("Incidents country-wise(top 10 countries): ")
            print("1.Country-wise number of incidents.")
            print("2.Country-wise comparison of kills and wounds.")
            print("3.Country-wise top 5 terrorist groups who attacked.")
            print("4.Country-wise top 5 corporation attacked.")
            print("5.Country-wise top 5 target types.")
            print("6.Exit.")
            try:
                choice = int(input("Enter your choice: "))
            except Exception as e:
                print("Enter a valid input.")
                continue
            if choice == 1:
                tempdf = empdf["country"].agg(np.count_nonzero).sort_values(ascending=False).head(10)
                p = tempdf.plot(kind = "bar")
                p.set_xlabel("Country")
                p.set_ylabel("Number of incidents")
                plt.show()
            elif choice == 2:
                tempdf = empdf["kill"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                tempdf1 = empdf["wound"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                df1 =  empdf["country"].agg(np.count_nonzero).sort_values(ascending=False).head(10).to_dict()
                df2 = list(df1.keys())
                tempdf2 = np.arange(len(df2))
                plt.bar(tempdf2,tempdf,width=0.2,label="kill")
                plt.bar(tempdf2+0.2,tempdf1,width=0.2,label="wound")
                plt.legend()
                plt.show()
            elif choice == 3:
                df1 =  empdf["country"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["country"]==name)].groupby(["group"])["group"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1.50,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 4:
                df1 =  empdf["country"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["country"]==name)].groupby(["corporation"])["corporation"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 5:
                df1 =  empdf["country"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["country"]==name)].groupby(["targtype"])["targtype"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 6:
                break
            else:
                print("Please Enter between 1 to 6.")
    elif ch == 3:
        empdf = df.groupby(["attacktype"])
        while True:
            print("Incidents attack-typewise: ")
            print("1.Attack-typewise number of incidents.")
            print("2.Attack-typewise comparison of kills and wounds.")
            print("3.Attack-typewise top 5 terrorist groups who attacked.")
            print("4.Attack-typewise top 5 countries attacked.")
            print("5.Attack-typewise top 5 target areas.")
            print("6.Exit.")
            try:
                choice = int(input("Enter your choice: "))
            except Exception as e:
                print("Enter a valid input.")
                continue
            if choice == 1:
                tempdf = empdf["attacktype"].agg(np.count_nonzero).sort_values(ascending=False).head(10)
                p = tempdf.plot(kind = "bar")
                p.set_xlabel("Attacktype")
                p.set_ylabel("Number of incidents")
                plt.show()
            elif choice == 2:
                tempdf = empdf["kill"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                tempdf1 = empdf["wound"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                df1 =  empdf["attacktype"].agg(np.count_nonzero).sort_values(ascending=False).head(10).to_dict()
                df2 = list(df1.keys())
                tempdf2 = np.arange(len(df2))
                plt.bar(tempdf2,tempdf,width=0.2,label="kill")
                plt.bar(tempdf2+0.2,tempdf1,width=0.2,label="wound")
                plt.legend()
                plt.show()
            elif choice == 3:
                df1 =  empdf["attacktype"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["attacktype"]==name)].groupby(["group"])["group"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1.50,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 4:
                df1 =  empdf["attacktype"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["attacktype"]==name)].groupby(["country"])["country"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 5:
                df1 =  empdf["attacktype"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["attacktype"]==name)].groupby(["targtype"])["targtype"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 6:
                break
            else:
                print("Please Enter between 1 to 6.")
    elif ch == 4:
        empdf = df.groupby(["targtype"])
        while True:
            print("Incidents target-typewise: ")
            print("1.Target-typewise number of incidents.")
            print("2.Target-typewise comparison of kills and wounds.")
            print("3.Target-typewise top 5 terrorist groups who attacked.")
            print("4.Target-typewise property extent.")
            print("5.Exit.")
            try:
                choice = int(input("Enter your choice: "))
            except Exception as e:
                print("Enter a valid input.")
                continue
            if choice == 1:
                tempdf = empdf["targtype"].agg(np.count_nonzero).sort_values(ascending=False).head(10)
                p = tempdf.plot(kind = "bar")
                p.set_xlabel("Targettype")
                p.set_ylabel("Number of incidents")
                plt.show()
            elif choice == 2:
                tempdf = empdf["kill"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                tempdf1 = empdf["wound"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                df1 =  empdf["targtype"].agg(np.count_nonzero).sort_values(ascending=False).head(10).to_dict()
                df2 = list(df1.keys())
                tempdf2 = np.arange(len(df2))
                plt.bar(tempdf2,tempdf,width=0.2,label="kill")
                plt.bar(tempdf2+0.2,tempdf1,width=0.2,label="wound")
                plt.legend()
                plt.show()
            elif choice == 3:
                df1 =  empdf["targtype"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["targtype"]==name)].groupby(["group"])["group"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1.50,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 4:
                df1 =  empdf["targtype"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["targtype"]==name)].groupby(["propextent"])["propextent"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 5:
                break
            else:
                print("Please Enter between 1 to 5.")
    elif ch == 5:
        empdf = df.groupby(["target"])
        while True:
            print("Incidents target-wise: ")
            print("1.Target-wise number of incidents.")
            print("2.Target-wise comparison of kills and wounds.")
            print("3.Target-wise top 5 terrorist groups who attacked.")
            print("4.Target-wise top 5 countries attacked.")
            print("5.Target-wise top 5 weapon types.")
            print("6.Exit.")
            try:
                choice = int(input("Enter your choice: "))
            except Exception as e:
                print("Enter a valid input.")
                continue
            if choice == 1:
                tempdf = empdf["target"].agg(np.count_nonzero).sort_values(ascending=False).head(10)
                p = tempdf.plot(kind = "bar")
                p.set_xlabel("Target")
                p.set_ylabel("Number of incidents")
                plt.show()
            elif choice == 2:
                tempdf = empdf["kill"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                tempdf1 = empdf["wound"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                df1 =  empdf["target"].agg(np.count_nonzero).sort_values(ascending=False).head(10).to_dict()
                df2 = list(df1.keys())
                tempdf2 = np.arange(len(df2))
                plt.bar(tempdf2,tempdf,width=0.2,label="kill")
                plt.bar(tempdf2+0.2,tempdf1,width=0.2,label="wound")
                plt.legend()
                plt.show()
            elif choice == 3:
                df1 =  empdf["target"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["target"]==name)].groupby(["group"])["group"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1.50,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 4:
                df1 =  empdf["target"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["target"]==name)].groupby(["country"])["country"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 5:
                df1 =  empdf["target"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["target"]==name)].groupby(["weaptype"])["weaptype"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1.50,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 6:
                break
            else:
                print("Please Enter between 1 to 6.")
    elif ch == 6:
        empdf = df.groupby(["group"])
        while True:
            print("Incidents terrorist group-wise: ")
            print("1.Group-wise number of incidents.")
            print("2.Group-wise comparision of kills and wounds.")
            print("3.Group-wise property extent.")
            print("4.Group-wise top 5 countries attacked.")
            print("5.Group-wise top 5 weapon types.")
            print("6.Exit.")
            try:
                choice = int(input("Enter your choice: "))
            except Exception as e:
                print("Enter a valid input.")
                continue
            if choice == 1:
                tempdf = empdf["group"].agg(np.count_nonzero).sort_values(ascending=False).head(10)
                p = tempdf.plot(kind = "bar")
                p.set_xlabel("Group")
                p.set_ylabel("Number of incidents")
                plt.show()
            elif choice == 2:
                tempdf = empdf["kill"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                tempdf1 = empdf["wound"].agg(np.sum).sort_values(ascending=False).head(10).tolist()
                df1 =  empdf["group"].agg(np.count_nonzero).sort_values(ascending=False).head(10).to_dict()
                df2 = list(df1.keys())
                tempdf2 = np.arange(len(df2))
                plt.bar(tempdf2,tempdf,width=0.2,label="kill")
                plt.bar(tempdf2+0.2,tempdf1,width=0.2,label="wound")
                plt.legend()
                plt.show()
            elif choice == 3:
                df1 =  empdf["group"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["group"]==name)].groupby(["propextent"])["propextent"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1.50,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 4:
                df1 =  empdf["group"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["group"]==name)].groupby(["country"])["country"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 5:
                df1 =  empdf["group"].agg(np.count_nonzero).sort_values(ascending=False).head(5).to_dict()
                tempdf = list(df1.keys())
                for name in tempdf:
                    tempdf1=df.loc[(df["group"]==name)].groupby(["weaptype"])["weaptype"].agg(np.count_nonzero).sort_values(ascending=False).head(5)
                    p=tempdf1.plot(kind="pie",subplots=True,radius=1.50,autopct='%0.2f%%')
                    plt.title(name)
                    plt.show()
            elif choice == 6:
                break
            else:
                print("Please Enter between 1 to 6.")
    elif choice == 7:
        print("Thank you")
        break
    else:
        print("Please Enter between 1 to 6.")
    

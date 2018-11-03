#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
f=open('guns.csv','r')
csvreader = csv.reader(f)
data=list(csvreader)
print(data[0:4])


# In[3]:


headers=data[0]
data=data[1:]
print(headers)
print(data[0:4])


# In[4]:


years=[]
for row in data:
    year=row[1]
    years.append(year)
year_counts={}
for year in years:
    if year in year_counts:
        year_counts[year]=year_counts[year]+1
    else:
        year_counts[year]=1
print(year_counts)


# In[14]:


import datetime
dates=[]
for row in data:
    date_time=datetime.datetime(year=int(row[1]), month=int(row[2]), day=1)
    dates.append(date_time)
print(dates[0:5])
date_counts={}
for date in dates:
    if date in date_counts:
        date_counts[date]=date_counts[date]+1
    else:
        date_counts[date]= 1
print(date_counts)
    


# In[18]:


sexes=[]
for row in data:
    sex=row[5]
    sexes.append(sex)
sex_counts={}
for sex in sexes:
    if sex in sex_counts:
        sex_counts[sex]=sex_counts[sex]+1
    else:
        sex_counts[sex]=1

races=[]
for row in data:
    race=row[7]
    races.append(race)
race_counts={}
for race in races:
    if race in race_counts:
        race_counts[race]=race_counts[race]+1
    else:
        race_counts[race]=1
print(race_counts)
print(sex_counts)
    


# In[20]:


c=open('census.csv','r')
csvreader = csv.reader(c)
census=list(csvreader)
print(census[0:4])


# In[56]:


race_count_index=list(race_counts.keys())
print(race_count_index)
counts=census[1]
print(counts)
mapping={race_count_index[0]:(int(counts[len(counts)-2])+int(counts[len(counts)-3]))
        ,race_count_index[1]:int(counts[len(counts)-4]),
        race_count_index[2]:int(counts[len(counts)-7]),
        race_count_index[3]:int(counts[len(counts)-5]),
        race_count_index[4]:int(counts[len(counts)-6])}
print(mapping)

race_per_hundredk={}
for race in race_counts:
    race_percent=race_counts[race]/mapping[race]*100000
    race_per_hundredk[race]=race_percent
print(race_per_hundredk)


# In[80]:


intents=[]
for row in data:
    a=row[3]
    intents.append(a)
print(intents[0:5])
print(races[0:5])
homicide_race_counts={}
for i,race in enumerate(races):
    if intents[i] == 'Homicide':
        if race in homicide_race_counts:   
            homicide_race_counts[race]=homicide_race_counts[race]+1
        else:
            homicide_race_counts[race]=1
print(homicide_race_counts)

homicide_race_per_hundredk={}
for race in homicide_race_counts:
    race_percent=homicide_race_counts[race]/mapping[race]*100000
    homicide_race_per_hundredk[race]=race_percent
print(race_per_hundredk)


# In[ ]:





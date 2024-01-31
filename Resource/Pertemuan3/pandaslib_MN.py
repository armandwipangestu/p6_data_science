# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 14:24:09 2021

@author: ismur
"""
'''
import pandas as pd
data = {
        'cookies': [4, 5, 6, 7],
        'cakes': [1, 2, 3, 4]
}
print(data)


food = pd.DataFrame(data, index=['Micheal', 'Tim', 'Mary', 'Lopez'])
print (food)
print (food.loc['Lopez'])
'''

import pandas as pd

movies_df = pd.read_csv ("IMDB-Movie-Data.csv")
print (movies_df.info())
print (movies_df.shape)


temp_df = movies_df.append(movies_df)
print (temp_df.shape)

#Removing duplicates
temp_df = temp_df.drop_duplicates() #dataPreprocessing
print(temp_df.shape)


print (movies_df.columns)


movies_df.rename(columns={
    'Runtime (Minutes)': 'runtime',
    'Revenue (Millions)': 'revenue_millions'
    }, inplace=True)
print (movies_df.columns)
print (movies_df.info())

movies_df.columns = [col.lower() for col in movies_df]


print (movies_df.info())


print (movies_df.isnull())
print(movies_df.info())
print (movies_df.isnull().sum())


#print (movies_df.dropna())
#print (movies_df.dropna(axis=0,inplace=True))
#print (movies_df.info())

revenue = movies_df['revenue_millions']
#Fill the nulls using fillna() method

revenue_mean = revenue.mean()
revenue.fillna(revenue_mean, inplace=True)
print(movies_df.isnull().sum())
print (movies_df.info())

revenue = movies_df['metascore']
#Fill the nulls using fillna() method

revenue_mean = revenue.min()
revenue.fillna(revenue_mean, inplace=True)
print(movies_df.isnull().sum())


print (movies_df.info())

#print (movies_df.describe())

#print (movies_df['rating'].describe())

#Calculating the frequency of all values in a column
print (movies_df['genre'].value_counts().head(3))


#method=histogram_intersection
print (movies_df.corr(method='pearson', min_periods=1))


genre_col = movies_df[['genre']]
print (type(genre_col))


subset = movies_df [['genre', 'rating']]
print(subset.head(10))


print (movies_df.info())
prom = movies_df.iloc[6]
print (prom)
#prom = movies_df.loc["prometheus"]
#print (prom)


movie_subset = movies_df.iloc[1:4]
print (movie_subset)

condition = (movies_df['director'] == "Ridley Scott")
print(condition.head())

print (movies_df[movies_df['director'] == "Ridley Scott"])
print (movies_df[(movies_df['director'] == 'Christopher Nolan') | (movies_df['director'] == 'RidleyScott')].head())
#Creating a function

def rating_function(x):
    if x >= 8.0:
        return "good"
    else:
        return "bad"
    
movies_df["rating_category"] = movies_df["rating"].apply(rating_function)
print(movies_df.head(2))
print(movies_df.info())
#movies_df ["rating_category"] = movies_df["rating"].apply(lambda x: 'good' if x >= 8.0 else 'bad')
#movies_df.head(2)

print(movies_df.info())


import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 10, 'figure.figsize': (10, 8)}) # set font and plot size to be larger
movies_df.plot(kind='scatter', x='rating', y='revenue_millions', title='Revenue (millions) vs Rating')
movies_df['rating'].plot(kind='hist', title='Rating')
movies_df.boxplot(column='revenue_millions', by='rating_category')

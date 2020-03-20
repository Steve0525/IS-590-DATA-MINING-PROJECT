import pandas as pd
import re
import numpy as np

house_price = pd.read_csv('houseprice.csv', ',',encoding = 'unicode_escape', low_memory=False)
# remove unnecessary columns
house_price_fixed = house_price.drop(columns=['url', 'DOM','Cid', 'followers',
                                              'fiveYearsProperty', 'buildingStructure',  'communityAverage'])
# add columns for easier access
house_price_fixed['month'] = house_price_fixed['tradeTime'].str[5:7]
house_price_fixed['month'].astype('int64')
house_price_fixed['year'] = house_price_fixed['tradeTime'].str[0:4]
house_price_fixed['year'].astype('int64')
house_price_fixed['year_month'] = house_price_fixed['tradeTime'].str[0:7]
house_price_fixed = house_price_fixed[house_price_fixed['price'] > 10000]
print(house_price_fixed.shape[0])
# print(house_price_fixed['tradeTime'].str[0:4].unique()) # check out what year is in the data
pop_l = ['2010', '2018', '2008', '2002', '2003', '2009']

for item in pop_l:
    house_remove = house_price_fixed[house_price_fixed['year'] == item] # remove the year with only a few records
    house_price_fixed = house_price_fixed.drop(labels=house_remove.axes[0])

house_price_fixed.sort_values(by=['year','month'], ascending=True, inplace=True)
house_price_fixed.reset_index(drop = True, inplace=True)


year = ['2011', '2012', '2013', '2014', '2015','2016', '2017']  # divide the data into different years
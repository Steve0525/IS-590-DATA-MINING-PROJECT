import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rc('figure', figsize=(10, 10))
plt.rcParams['axes.unicode_minus']=False
sns.set(font_scale=2)

# house_price = pd.read_csv('houseprice.csv', ',',encoding = 'unicode_escape', low_memory=False)
# # remove unnecessary columns
# house_price_fixed = house_price.drop(columns=['id','url', 'DOM','Cid', 'followers',
#                                               'fiveYearsProperty', 'buildingStructure',  'communityAverage'])
# # add columns for easier access
# house_price_fixed['month'] = house_price_fixed['tradeTime'].str[5:7]
# house_price_fixed['month'].astype('int64')
# house_price_fixed['year'] = house_price_fixed['tradeTime'].str[0:4]
# house_price_fixed['year'].astype('int64')
# house_price_fixed['year_month'] = house_price_fixed['tradeTime'].str[0:7]
# house_price_fixed = house_price_fixed[house_price_fixed['price'] > 10000]
# # print(house_price_fixed.shape[0])
#
# print(house_price_fixed['tradeTime'].str[0:4].unique()) # check out what year is in the data
# pop_l = ['2010', '2018', '2008', '2002', '2003', '2009']
#
# for item in pop_l:
#     house_remove = house_price_fixed[house_price_fixed['year'] == item] # remove the year with only a few records
#     house_price_fixed = house_price_fixed.drop(labels=house_remove.axes[0])
#
# house_price_fixed.to_csv(r'houseprice_cleaned.csv', index = False)

house_price_fixed = pd.read_csv('houseprice_cleaned.csv')

# check if there is nan in the values
# print(house_price_fixed['square'].dtype)
# print(np.isnan(house_price_fixed['square']).describe()) # no nan values
# print(len(house_price_fixed['square'].unique()))
house_price_fixed['square'].astype('float64')

print(house_price_fixed['livingRoom'].dtype)
# house_price_fixed['livingRoom'].astype('float64')
wierd = house_price_fixed.livingRoom.apply(lambda x: isinstance(x, str))
object_livingroom = house_price_fixed[wierd]['livingRoom']
strange =object_livingroom[object_livingroom == '#NAME?']
print(strange.shape[0])

# remove #name?
house_price_fixed = house_price_fixed.drop(labels=strange.index)
print(house_price_fixed[house_price_fixed['livingRoom'] == '#NAME?'])
house_price_fixed['livingRoom'].astype('float64')
print(house_price_fixed.shape[0]) # check if the rows are removed

# change types of kitchen column
house_price_fixed['kitchen'].astype('float64')

# change types of square
house_price_fixed['square'].astype('float64')

# write to a new file
house_price_fixed.to_csv('houseprice_cleaned_new.csv')

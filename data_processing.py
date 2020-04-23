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
# print(house_price.shape)
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

house_price_fixed = pd.read_csv('houseprice_cleaned_final_weka.csv')


# check if there is nan in the values
# print(np.isnan(house_price_fixed['square']).describe()) # no nan values
# print(len(house_price_fixed['square'].unique()))
# house_price_fixed['square'].astype('float64')
#
# print(house_price_fixed['livingRoom'].dtype)
# wierd = house_price_fixed.livingRoom.apply(lambda x: isinstance(x, str))
# object_livingroom = house_price_fixed[wierd]['livingRoom']
# strange =object_livingroom[object_livingroom == '#NAME?']
# print(strange.shape[0])
#
# # remove #name?
# house_price_fixed = house_price_fixed.drop(labels=strange.index)
# print(house_price_fixed[house_price_fixed['livingRoom'] == '#NAME?'])
# house_price_fixed['livingRoom'] = house_price_fixed['livingRoom'].astype('int64')
# print(house_price_fixed.shape[0]) # check if the rows are removed
#
# # change types of kitchen column
# house_price_fixed['kitchen']=house_price_fixed['kitchen'].astype('int64')
# house_price_fixed['square'] = house_price_fixed['square'].astype('float64')
# house_price_fixed['bathRoom'] = house_price_fixed['bathRoom'].astype('int64')
# house_price_fixed['drawingRoom'] = house_price_fixed['drawingRoom'].astype('int64')
#
# # remove unkonw characters before floor number
# reg_ex = re.compile(r"[^\d]+", re.IGNORECASE)
# house_price_fixed['floor'] = house_price_fixed['floor'].replace(reg_ex, '')
# print(house_price_fixed['floor'])
# house_price_fixed['floor'] = house_price_fixed['floor'].astype('int64')
#
# # some unkown data in the dataset
# house_price_fixed['constructionTime'] = house_price_fixed['constructionTime'].replace(reg_ex, '')
# no_construction_time = house_price_fixed[house_price_fixed['constructionTime'] == ''] # houses with no construction time
# house_price_fixed = house_price_fixed.drop(labels = no_construction_time.index)
# house_price_fixed['constructionTime'] = house_price_fixed['constructionTime'].astype('int64')
# print(house_price_fixed.dtypes)

# house price range
# house_price_fixed[house_price_fixed['price'] <= 10000]
# price_list = house_price_fixed['price'].unique
# house_price_fixed['price'].describe()
group = house_price_fixed.groupby('price')
# group
bins_a = list(range(10000, 60000, 2000))
bins_b = list(range(60000, 150000, 10000))
bins = bins_a + bins_b
labels = [str(x) for x in bins]
price_range = []
for i in range(len(labels)-1):
    label = '{}-{}'.format(labels[i], labels[i+1])
    price_range.append(label)
price_range
house_price_fixed['priceRange'] = pd.cut(house_price_fixed['price'],bins, labels=price_range)
house_price_fixed['priceRange']
# write to a new file
house_price_fixed.to_csv('houseprice_cleaned_final_weka1.csv', sep=',', index=False)

house_price_fixed.sort_values(by=['year','month'], ascending=True, inplace=True)
house_price_fixed.reset_index(drop = True, inplace=True)
a =house_price_fixed.groupby('priceRange').count()

# house_price_fixed['year']=house_price_fixed['year'].astype('object')

year = ['2011', '2012', '2013', '2014', '2015','2016', '2017']  # divide the data into different years

# f, ax = plt.subplots(figsize=(13, 20))
# sns.distplot(house_price_fixed['price'], label='year')
#
# sns.distplot(house_price_fixed[house_price_fixed['year']==2011]['price'],color='pink', label='2011',hist_kws=dict(alpha=0.5))
# sns.distplot(house_price_fixed[house_price_fixed['year']==2012]['price'],color='grey', label='2012',hist_kws=dict(alpha=0.35))
# sns.distplot(house_price_fixed[house_price_fixed['year']==2013]['price'],color='yellow', label='2013',hist_kws=dict(alpha=0.25))
# sns.distplot(house_price_fixed[house_price_fixed['year']==2014]['price'],color='purple', label='2014',hist_kws=dict(alpha=0.25))
# plt.title(' house price box plot')
# f.savefig('_house_price_box_plot.jpg')
# plt.show()


for item in year:
    yeardat = house_price_fixed[house_price_fixed['year'] == int(item)]
    # house_price_fixed['year'].dtype
    yeardat.reset_index(drop=True, inplace=True)

    f, ax = plt.subplots(figsize=(13, 20))
    sns.jointplot(y="price", x='square', data= yeardat)
    plt.xlabel('square')
    plt.ylabel('Price')
    plt.title(item + ' house price box plot')
    f.savefig(item + '_house_price_box_plot.jpg')
    plt.show()

#


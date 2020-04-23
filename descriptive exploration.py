import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# sort values
house_price_fixed.sort_values(by=['year','month'], ascending=True, inplace=True)
house_price_fixed.reset_index(drop = True, inplace=True)

year = ['2011', '2012', '2013', '2014', '2015','2016', '2017']  # divide the data into different years

# for item in year:
#     yeardat = house_price_fixed[house_price_fixed['year'] == item]
#     yeardat.reset_index(drop=True, inplace=True)
#
#     # f, ax = plt.subplots(figsize=(12, 15))
#     # sns.barplot(y="price", x='kitchen', data=yeardat)
#     # plt.xlabel('Time')
#     # plt.ylabel('Price')
#     # plt.show()
#     # # plt.title( item + ' house price bar plot')
#     # f.savefig(item + '_house_price_bar_plot.jpg')
#
#     f, ax = plt.subplots(figsize=(13, 20))
#     sns.boxplot(y="price", x='kitchen', data= yeardat)
#     plt.xlabel('Kitchen')
#     plt.ylabel('Price')
#     plt.title(item + ' house price box plot')
#     f.savefig(item + '_house_price_box_plot.jpg')
#     plt.show()
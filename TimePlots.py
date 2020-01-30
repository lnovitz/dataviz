import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pylab as plt

df = pd.read_csv('Bookings_2013_to_2019.csv')

df.head(4)
plot = df['BETWEEN BOOKINGS TIME'].plot(kind = 'hist', bins = 50).axis(xmin=-800, xmax=0)
sns.boxplot(x=df['TIER'], y=df['BETWEEN BOOKINGS TIME'], data=df)
df['booking_interval'] = pd.cut(df['BETWEEN BOOKINGS TIME'], 5)
df.head(5)
bookings = df.groupby(by='booking_interval')['CCN'].size().reset_index(name='counts')
bookings
sns.countplot(x="booking_interval", data=df).set_xticklabels(rotation=30)




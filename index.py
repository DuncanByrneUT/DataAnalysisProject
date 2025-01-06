# import pandas we are importing what we installed with pip3 install pandas numpy matplotlib seaborn
import pandas as pd

# pandas is reading the data in the csv file
df = pd.read_csv('netflix_titles.csv')

print(df.isnull().sum())  # Shows count of missing values per column

# this decides whether the missing values wil either be be dropped, filled, or replaced
df = df.dropna()

# removing duplicates in the data
df = df.drop_duplicates()

# converting the data types if necessary
df['type'] = df['type'].astype('category') # this is forthe categorical data

print(df.describe())



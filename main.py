# import pandas we are importing what we installed with pip3 install pandas numpy matplotlib seaborn
import pandas as pd

# pandas is reading the data in the csv file
df = pd.read_csv('netflix_titles.csv')

print(df.isnull().sum())

df = df.dropna()

# removing duplicates in the data
df = df.drop_duplicates()

# converting the data types if necessary
df['column_name'] = df['column_name'].astype('category') # this is forthe categorical data

# import pandas we are importing what we installed with pip3 install pandas numpy matplotlib seaborn
import pandas as pd

# pandas is reading the data in the csv file
df = pd.read_csv('netflix_titles.csv')

print(df.isnull().sum())  # Shows count of missing values per column
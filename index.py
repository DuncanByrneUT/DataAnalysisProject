# import pandas we are importing what we installed with pip3 install pandas numpy matplotlib seaborn
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# pandas is reading the data in the csv file
df = pd.read_csv('netflix_titles.csv')

print(df.isnull().sum())  # Shows count of missing values per column

# this decides whether the missing values wil either be be dropped, filled, or replaced
df = df.dropna()

# removing duplicates in the data
df = df.drop_duplicates()

# converting the data types if necessary
df['type'] = df['type'].astype('category') # this is forthe categorical data

print("\nBasic Statistics:")
print(df.describe())


# types of content distributed
plt.figure(figsize=(10, 5))
sns.countplot(x='type', data=df)
plt.title('Distribution of Content Types on Netflix')
plt.show()
#release year

if 'release_year' in df.columns:
    plt.figure(figsize=(10,5))
    df['release_year'].hist(bins=30)
    plt.title('Distribution of Release Years')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.show()

# correlation analysis
numeric_df = df.select_dtypes(include= ['int64', 'float64'])
if numeric_df.shape[1] > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix')
    plt.show()

# grouping data

if 'country' in df.columns:
    # Group by country and count titles
    country_counts = df['country'].value_counts()
    print("\nTop 10 Countries by Content Count:")
    print(country_counts.head(10))

# Save cleaned data for future use
df.to_csv('cleaned_netflix_titles.csv', index=False)
print("\nCleaned data saved to 'cleaned_netflix_titles.csv'")






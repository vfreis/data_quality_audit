import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# loading data set
df = pd.read_csv('hotel_bookings.csv')

# 1- exploring data set
print(f'Columns and Types: \n', df.info())
print(f'Summary Stats: \n', df.describe())

# 2 - checking data quality

# missing values
missing_data = df.isnull().sum()
print(f'Missing Data: \n', missing_data[missing_data > 0 ])

# duplicates
duplicates = df.duplicated().sum()
print("Duplicates: ", duplicates)

# inconsistent data
print(f'Unique Values in "hotel": \n', df['hotel'].unique())

# 3 - data cleaning
# fill missing values
df['children'].fillna(0, inplace=True)
df['country'].fillna(0, inplace=True)
df['agent'].fillna(0, inplace=True)
df['company'].fillna(0, inplace=True)

# remove duplicates
df = df.drop_duplicates()

# standardize string formatting
df['hotel'] = df['hotel'].str.lower()

# 4 - identify outliers
# vizualize lead time
sns.boxplot(df['lead_time'])
plt.title('Boxplot Lead Time')
plt.show()

# 5 - validation
assert df.isnull().sum().sum() == 0, "There are still missing values!"

df.to_csv('cleaned_hotel_bookings', index=False)
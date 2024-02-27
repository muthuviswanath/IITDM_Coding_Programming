import pandas as pa
import seaborn as sb
df = sb.load_dataset("titanic", cache=True)
print(df)
#describing the data
print(df.describe())

#Getting the data information (NAN/Null Values)
print(df.info())

print(df['deck'].value_counts(dropna=False))
print(df.info())

#in case of isnull NaN is considered as True
#in case of notnull NaN is considered as False

print(df.notnull())

missing_data = df.isnull().sum()
print(f" Total number of missing data: {missing_data}")
print("Remaining Data:")
print(len(df)-df.isnull().sum())

#deleting the missing data:

new_df = df.dropna(axis = 0,how='any', subset=['age'])
print(new_df)
print(len(new_df))

no = df.dropna()
total = no.isnull().sum()
print(total)
print(df)

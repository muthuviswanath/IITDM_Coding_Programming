import pandas as pa
import seaborn as sb

df = sb.load_dataset("titanic",cache=True)
print(df.head(10))
print(df.info())
#find the records with NAN and replace it with some other value:

avg_age = df['age'].mean(axis=0)
print(f"Average Age: {avg_age}")

df['age'].fillna(avg_age,inplace=True)
print(df)
print(df.info())

print(df.isnull().sum())

emb_town_count = df['embark_town'].value_counts(dropna=True)
print(emb_town_count)

most = emb_town_count.idxmax()
print(most)

# df['embark_town'].fillna(most,inplace=True)
# print(df.info())
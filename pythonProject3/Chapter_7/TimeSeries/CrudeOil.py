import pandas as pa


wti = pa.read_csv(r"C:\Users\muthu\Downloads\DCOILWTICO.csv")
print(wti.head(10))
print(wti.info())

wti['N_DATE '] = pa.to_datetime(wti['DATE'])
print(wti['N_DATE '])
print(wti.head(10))

df = wti.drop(['DATE'],axis=1)
print(df.head(10))

df.set_index('N_DATE ',inplace=True)
print(df.head(10))

print(wti.info())
print(df.info())

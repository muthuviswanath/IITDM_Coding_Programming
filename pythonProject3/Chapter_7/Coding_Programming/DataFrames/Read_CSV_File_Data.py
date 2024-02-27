import pandas as pa
indust = pa.read_csv("C:/Users/muthu/Downloads/industry.csv",header=23)
print(type(indust))
print(indust.info())
print(indust)
print(indust.head(5))
print(indust.tail(5))


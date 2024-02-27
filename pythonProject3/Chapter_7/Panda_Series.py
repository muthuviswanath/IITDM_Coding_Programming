import pandas as p

my_series = p.Series([10,20,30,40,50])
print(my_series)

my_series = p.Series(["Sachin","Virat","Rohit","Jadeja","Dhoni"], index=[10,18,45,12,7])
print(my_series)

my_series = p.Series([True,False])
print(my_series)

my_series = p.Series([45+5j,66+0.4j])
print(my_series)

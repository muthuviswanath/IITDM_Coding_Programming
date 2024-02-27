import pandas as pa

dates = pa.date_range('2024-02-24','2024-12-24')
print(dates)
my_dates = pa.Series(dates)

for i in range (100,111):
    print(my_dates[i])
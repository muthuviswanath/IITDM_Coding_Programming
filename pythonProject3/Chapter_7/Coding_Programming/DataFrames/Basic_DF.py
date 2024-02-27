import pandas as pa
data = {'Population':[234733,348345,6789043,5678934],'Literacy':[65,67.43,78,89]}
my_df = pa.DataFrame(data)
my_ser= pa.Series(data)
print(my_df)
print(my_ser)

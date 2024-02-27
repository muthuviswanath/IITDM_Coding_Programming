import pandas as pa
import matplotlib.pyplot as plt
import pandas_datareader as pdr

df = pdr.get_data_fred("GS10")
print(df)
print(df["GS10"].value_counts())
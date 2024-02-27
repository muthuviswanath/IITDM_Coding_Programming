#
import pandas as pa
print("Reading Excel data (.xls) extension")
df = pa.read_excel(r"C:\Users\muthu\OneDrive\Desktop\Emp_Records.xls", sheet_name=1,header=0)
print(df)


#
print("Reading Excel data (.xlsx) extension using openpyxl")
df = pa.read_excel(r"C:\Users\muthu\OneDrive\Desktop\IBM_Emp_Records.xlsx", sheet_name=0,header=0, engine='openpyxl')
print(df)
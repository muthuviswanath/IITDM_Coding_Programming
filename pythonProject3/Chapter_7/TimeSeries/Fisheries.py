import pandas as pa
import matplotlib.pyplot as plt
from datetime import datetime,date, time

# Import the data from the CSV file
df = pa.read_csv("capture-fisheries-vs-aquaculture.csv")

# Print the first 10 rows of the dataframe
print(df.head(10))

#Check for null values
print(df.info())

# Dropping the column called Code
df = df.drop(['Code'], axis=1)

# Print the first 10 rows of the dataframe to verify the changes
print(df.info())

# Check for null values
print(df.isnull().sum())

# Fill the null values with zero
df.fillna(0, inplace=True)

# Check for null values
print(df.isnull().sum())

# Change the TiimeSeries Datatype and set the index
df['New_Year'] = pa.to_datetime(df['Year'].astype(str), format='%Y')
df.set_index(['New_Year'], inplace=True)
df.drop(['Year'], axis=1, inplace=True)

# Print the first 10 rows of the dataframe to verify the changes
print(df.head(10))

# Check the datatypes
print(df.info())

# Sorting the index
new_df = df.sort_index()
print(new_df.head(10))

# Check the datatypes
print(df.info())

# Changing the datatype of entity to category
new_df['Entity'] = new_df['Entity'].astype('category')

# Check the datatypes
print(new_df.info())

print(new_df['Entity'].value_counts())

# Group the data based on the index column

grouped_data = new_df.groupby(['New_Year'])
print(grouped_data.head(10))

# print the data present in each and every group

for name, group in grouped_data:
    print(f"name: {name}")
    print(f"group: {group}")
    print(f"{group.head(10)}")
    print("\n\n")


# Plot the data

# find the global total:

global_total = grouped_data.sum()
print(global_total.head(10))

plt.style.use('ggplot')
global_total.plot(kind='area',
                  alpha= 0.25,
                  stacked=False,
                  label='World Fisheries Capture',
                  figsize=(30, 15))
plt.title('World Fisheries Capture')
plt.xlabel('Year')
plt.legend()
plt.show()

country = new_df['Entity'].value_counts()
print(country)
print(type(country))

# Plot the data for the countries India,Maldives, Pakistan, Syria, China
india = new_df.loc[new_df['Entity'] == 'India']
maldives = new_df.loc[new_df['Entity'] == 'Maldives']
pakistan = new_df.loc[new_df['Entity'] == 'Pakistan']
syria = new_df.loc[new_df['Entity'] == 'Syria']
china = new_df.loc[new_df['Entity'] == 'China']

india_x = india.index
india_y = india[['Aquaculture production (metric tons)', 'Capture fisheries production (metric tons)']]

maldives_x = maldives.index
maldives_y = maldives[['Aquaculture production (metric tons)', 'Capture fisheries production (metric tons)']]

pakistan_x = pakistan.index
pakistan_y = pakistan[['Aquaculture production (metric tons)', 'Capture fisheries production (metric tons)']]

syria_x = syria.index
syria_y = syria[['Aquaculture production (metric tons)', 'Capture fisheries production (metric tons)']]

china_x = china.index
china_y = china[['Aquaculture production (metric tons)', 'Capture fisheries production (metric tons)']]


fig,ax = plt.subplots(1,5, figsize=(30, 15))
ax[0].plot(india_x, india_y)
ax[0].set_title('India')
ax[0].set_xlabel('Year')
ax[0].set_ylabel('Production in Metric Tons')

ax[1].plot(maldives_x, maldives_y)
ax[1].set_title('Maldives')
ax[1].set_xlabel('Year')
ax[1].set_ylabel('Production in Metric Tons')

ax[2].plot(pakistan_x, pakistan_y)
ax[2].set_title('Pakistan')
ax[2].set_xlabel('Year')
ax[2].set_ylabel('Production in Metric Tons')

ax[3].plot(syria_x, syria_y)
ax[3].set_title('Syria')
ax[3].set_xlabel('Year')
ax[3].set_ylabel('Production in Metric Tons')

ax[4].plot(china_x, china_y)
ax[4].set_title('China')
ax[4].set_xlabel('Year')
ax[4].set_ylabel('Production in Metric Tons')

plt.suptitle('Aquaculture and Capture Production in Metric Tons for India, Maldives, Pakistan, Syria and China')
plt.show()


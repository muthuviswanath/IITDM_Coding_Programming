import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Read the data from the csv file
data=pd.read_csv('Sample - Superstore (1).csv', encoding='latin-1', parse_dates=['Order Date'])
print(data.head())

print(data.info())

# 2. Create new columns like order month, order year, and order day using the existing column data.
data['order_year'] = data['Order Date'].dt.year
order_month = data['Order Date'].dt.month
data['order_month'] = data['Order Date'].dt.month
data['order_day'] = data['Order Date'].dt.dayofweek

# 3. Perform Monthly Sales Analysis and display it as a line chart.
new_df=data[['order_month', 'Sales']]
sales_by_month=new_df.groupby('order_month')['Sales'].sum().reset_index()
print("Sales By Month:\n",sales_by_month)
figure1=px.line(
        sales_by_month,
        x='order_month',
        y='Sales',
        title="Sales by Monthly report"
    )
figure1.show()

# 4. Perform sales by category Analysis and display it as a pie chart.
sales_by_categ=data.groupby('Category')['Sales'].sum().reset_index()
print("Sales By Category:\n",sales_by_categ)
figure2=px.pie(sales_by_categ,
              values='Sales',
              names='Category',
              hole=0.75,
              color_discrete_sequence=px.colors.qualitative.Pastel)
figure2.update_traces(textposition='inside', textinfo='percent+label')
figure2.update_layout(title="Sales by category Report")
figure2.show()

# 5. Perform sales by sub-category Analysis and display it as a bar chart.
sales_by_subcateg=data.groupby('Sub-Category')['Sales'].sum().reset_index()
print("Sales By Sub-Category:\n", sales_by_subcateg)
figure3=px.bar(
    sales_by_subcateg,
    x=sales_by_subcateg['Sub-Category'],
    y=sales_by_subcateg['Sales'],
    title="Sales by Sub-Category Report",
)
figure3.show()

#6. Perform Monthly Profit Analysis and display it as line chart.
new_df=data[['order_month', 'Profit']]
profit_by_month=new_df.groupby('order_month')['Profit'].sum().reset_index()
print("Profit By Month:\n",profit_by_month)
figure4=px.line(
        profit_by_month,
        x='order_month',
        y='Profit',
        title="Profit by Monthly report"
    )
figure4.show()

# 7. Perform profit by category Analysis and display it as a pie chart.
sales_by_categ=data.groupby('Category')['Profit'].sum().reset_index()
print("Profit By Category:\n",sales_by_categ)
figure5=px.pie(sales_by_categ,
              values='Profit',
              names='Category',
              hole=0.75,
              color_discrete_sequence=px.colors.qualitative.Pastel)
figure5.update_traces(textposition='inside', textinfo='percent+label')
figure5.update_layout(title="Profit by category Report")
figure5.show()

# 8. Perform profit by sub-category Analysis and display it as a bar chart.
sales_by_subcateg=data.groupby('Sub-Category')['Profit'].sum().reset_index()
print("Profit By Sub-Category:\n", sales_by_subcateg)
figure6=px.bar(
    sales_by_subcateg,
    x=sales_by_subcateg['Sub-Category'],
    y=sales_by_subcateg['Profit'],
    title="Profit by Sub-Category Report",
)
figure6.show()

# 9. Perform sales and profit analysis by customer segments and display it as bar chart
salesAndProfit_by_segment=data.groupby('Segment')['Sales', 'Profit'].sum().reset_index()
print("Sales And Profit Customer Segment:\n", salesAndProfit_by_segment)

# 9. Perform sales and profit analysis by customer segments and display it as bar chart
salesAndProfit_by_segment=data.groupby('Segment')['Sales', 'Profit'].sum().reset_index()
print("Sales And Profit Customer Segment:\n", salesAndProfit_by_segment)

figure7=go.Figure()
figure7.add_trace(go.Bar(
    x=salesAndProfit_by_segment['Segment'],
    y=salesAndProfit_by_segment['Sales'],
    name='Sales by Customer Segment Report',
    marker_color="Green"
))
figure7.add_trace(go.Bar(
    x=salesAndProfit_by_segment['Segment'],
    y=salesAndProfit_by_segment['Profit'],
    name='Profit by Customer Segment Report',
    marker_color="Orange"
))
figure7.update_layout(barmode='group', xaxis_tickangle=45)
figure7.show()

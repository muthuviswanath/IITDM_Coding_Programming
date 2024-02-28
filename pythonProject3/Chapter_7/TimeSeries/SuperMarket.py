import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors
pio.templates.default = "plotly_white"

data = pd.read_csv("Sample - Superstore.csv", encoding='latin-1')
print(data.head())
print(data.describe())
print(data.info())

data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Ship Date'] = pd.to_datetime(data['Ship Date'])
data ['Order Month'] = data['Order Date'].dt.month
data['Order Year'] = data['Order Date'].dt.year
data['Order Day of Week'] = data['Order Date'].dt.dayofweek

sales_by_month = data.groupby('Order Month')['Sales'].sum().reset_index()
print(sales_by_month)

figure_1 = px.line(sales_by_month,
                   x = 'Order Month',
                   y = 'Sales',
                   title = 'Monthly Sales Report'
)
figure_1.show()

sales_by_category = data.groupby('Category')['Sales'].sum().reset_index()
print(sales_by_category)

figure_2= px.pie(sales_by_category,
                 values='Sales',
                 names='Category',
                 hole=0.75,
                 color_discrete_sequence= px.colors.qualitative.Pastel)
figure_2.update_traces(textposition='inside',textinfo='percent+label')
figure_2.update_layout(title= 'Sales by Category Report')
figure_2.show()


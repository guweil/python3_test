import pandas as pd

df = pd.read_excel('https://github.com/datagy/pivot_table_pandas/raw/master/sample_pivot.xlsx', parse_dates=['Date'])
print(df.head())
sales_by_region = pd.pivot_table(df, index = 'Region', values = 'Sales') #default for aggfunc is "mean"
print(sales_by_region)
total_by_region = pd.pivot_table(df, index = 'Region', values = 'Sales', aggfunc='sum')
print(total_by_region)
columns_example = pd.pivot_table(df, index='Type', columns='Region', values='Units', aggfunc='sum')
print(columns_example)
columns_example.plot(kind='bar')
pd.pivot_table(df, index = 'Type', values = 'Units', columns = 'Region', aggfunc = 'max', fill_value = 'N/A')
pd.pivot_table(df, index = 'Type', values = 'Units', columns = 'Region', aggfunc = 'max', fill_value = 'N/A', margins = True, margins_name='Total')
df.pivot_table(index=pd.Grouper(freq='M', key='Date'), columns='Region', values='Units', aggfunc='sum')

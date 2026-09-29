import pandas as pd
import datetime

from pandas.core.interchange import column

# reads the csv file and replace missing values with N/A
data = pd.read_csv(r'C:data\sample_transaction.csv', na_values = ['N/A'])

# check that the columns are correct and exist e.g. date, type, description, amount
# check_columns = ['date', 'type', 'description', 'amount']
# for column1 in df.columns:
#     for column2 in check_columns:
#         if column1 == column2:
#             print(column1, column2)
#         else:
#             print("Missing column")

# headers
data = data[['Date', 'Type', 'Description', 'Amount']]

#convert and overwrite date to actual date format
data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
# convert and overwrite type and description to uppercase
data['Type'] = data['Type'].str.lower()
data['Description'] = data['Description'].str.lower()
# convert and overwrite amount as float
data['Amount'] = data['Amount'].astype(float)

# fix string

# validate and convert type


# filter the dataframe to today's month
# today_month = datetime.date.today().month
today_month = datetime.datetime.now().month
data = data[data['Date'].dt.month == today_month]


# fiter to expense
data = data[data['Type'] == 'expense']

def total_expense(data):
    sum_expense = abs(data['Amount'].sum())
    return f"{sum_expense:.2f}"

print(total_expense(data))

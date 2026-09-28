# handles reading and cleaning the raw data

import pandas as pd
from pandas.core.interchange import column

# reads the csv file and replace missing values with N/A
df = pd.read_csv(r'C:data\sample_transaction.csv', na_values = ['N/A'])

# check that the columns are correct and exist e.g. date, type, description, amount
# check_columns = ['date', 'type', 'description', 'amount']
# for column1 in df.columns:
#     for column2 in check_columns:
#         if column1 == column2:
#             print(column1, column2)
#         else:
#             print("Missing column")
# headers
data = df[['Date', 'Type', 'Description', 'Amount']]
# fix string

# validate and convert type

# convert date to date format
df['Date'] = pd.to_datetime(df['Date'])

# filter out the income
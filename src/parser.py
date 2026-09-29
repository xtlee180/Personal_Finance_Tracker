# handles reading and cleaning the raw data

# import pandas as pd
# from pandas.core.interchange import column
#
# # reads the csv file and replace missing values with N/A
# data = pd.read_csv(r'C:\Users\18071\PycharmProjects\Personal_Finance_Tracker\data\sample_transaction.csv', na_values = ['N/A'])
#
# # check that the columns are correct and exist e.g. date, type, description, amount
# # check_columns = ['date', 'type', 'description', 'amount']
# # for column1 in df.columns:
# #     for column2 in check_columns:
# #         if column1 == column2:
# #             print(column1, column2)
# #         else:
# #             print("Missing column")
#
# # headers
# data = data[['Date', 'Type', 'Description', 'Amount']]
#
# #convert and overwrite date to actual date format
# data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
# # convert and overwrite description to uppercase
# data['Description'] = data['Description'].str.upper()
#
# data['Type'] = data['Type'].str.upper()
# # fix string
#
# # validate and convert type
#
#
# # filter out the income
# filter = data['Type'] == 'EXPENSE'
#
# data.where(filter).dropna()
#
# print(data)
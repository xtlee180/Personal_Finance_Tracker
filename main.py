import pandas as pd
import datetime
import json

# reads the csv file and replace missing values with N/A
def load_data(file_path):
    raw_data = pd.read_csv(file_path, na_values = ['N/A'])
    return raw_data

# check that the columns are correct and exist e.g. date, type, description, amount
# def validate_columns(data):
#     check_columns = ['Date', 'Type', 'Description', 'Amount']
#
#     for column in check_columns:
#         if column not in data.columns:
#             return False
#
#     return True
#

def clean_data(data):
    data = data[['Date', 'Type', 'Description', 'Amount']].copy()

    #convert and overwrite date to actual date format
    data['Date'] = pd.to_datetime(data['Date'], dayfirst=True)
    # convert and overwrite type and description to uppercase
    data['Type'] = data['Type'].str.lower()
    data['Description'] = data['Description'].str.lower()
    # convert and overwrite amount as float
    data['Amount'] = data['Amount'].astype(float)

    return data


data = load_data('C:data\sample_transaction.csv')
data = clean_data(data)


# filter the dataframe to today's month
# today_month = datetime.date.today().month
today_month = datetime.datetime.now().month
data = data[data['Date'].dt.month == today_month]


# fiter to expense
data = data[data['Type'] == 'expense']

def total_expense(data):
    sum_expense = abs(data['Amount'].sum())
    return f"{sum_expense:,.2f}"


with open('data/category_rule.json', 'r') as file:
    category_rules = json.load(file)

def category_sort(description):
    # lower_description = description.lower()

    for category, keywords in category_rules.items():
        for keyword in keywords:
            if keyword in description:
                return category
    return "Uncategorized"

data['Category'] = data['Description'].apply(category_sort)

# def group_category(data):
#     for key in category.keys():
#         if key in data['Category']:
#             return key

def group_categories(data):
    category_totals = abs(data.groupby('Category')['Amount'].sum()).sort_values(ascending = False)
    return category_totals

def print_categories(category_totals, total_spent):

    for category, amount in category_totals.items():
        percentage = (amount / total_spent) * 100
        price = f'£{amount:.2f}'
        print(f'{category:<15}  {price:>8} {percentage:>8.1f}%')



# print(group_categories(data))

# print(group_category)
# print(group_category(data))

def top_three(data):
    top = data.sort_values(by = ['Amount']).head(3)
    return top


def top3():
    topthree = top_three(data)
    rank = 1

    for index, row in topthree.iterrows():
        date_text = row['Date'].strftime('%d/%m/%Y')
        amount_text = f"£{abs(row['Amount']):,.2f}"
        desciption_text = row['Description'].upper()
        print(f"{rank}. {date_text}  {desciption_text:<25} {amount_text:>5}")
        rank += 1

def print_summary():
    current_month = datetime.datetime.now().strftime('%B')
    current_year  = datetime.datetime.now().strftime('%Y')
    total_transaction = len(data)


    print('==============================')
    print(f'SPENDING SUMMARY: {current_month.upper()} {current_year}')
    print('==============================')
    print(f'TOTAL SPENT: £{total_expense(data)}  ({total_transaction} TRANSACTIONS) ')
    print('\n')
    print(f'BY CATEGORY:')
    group_categories()
    print('\n')
    print(f'TOP 3 BIGGEST PURCHASES:')
    top3()


print_summary()
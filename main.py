import pandas as pd
import datetime
import json

# reads the csv file and replace missing values with N/A
def load_transactions(file_path):
    raw_transactions = pd.read_csv(file_path, na_values = ['N/A'])
    return raw_transactions


def clean_transactions(transactions):
    transactions = transactions[['Date', 'Type', 'Description', 'Amount']].copy()

    #convert and overwrite date to actual date format
    transactions['Date'] = pd.to_datetime(transactions['Date'], dayfirst=True)
    # convert and overwrite type and description to uppercase
    transactions['Type'] = transactions['Type'].str.lower()
    transactions['Description'] = transactions['Description'].str.lower()
    # convert and overwrite amount as float
    transactions['Amount'] = transactions['Amount'].astype(float)

    return transactions


def filter_by_month(transactions, month, year):
    monthly_transactions = transactions[
        (transactions['Date'].dt.month == month) &
        (transactions['Date'].dt.year == year)
    ]

    return monthly_transactions


# fiter to expense

def filter_expenses(transactions):
    expenses = transactions[transactions['Type'] == 'expense']

    return expenses


def load_category_rules(file_path):
    with open(file_path, 'r') as file:
        category_rules = json.load(file)

    return category_rules


def categorize_transaction(description,category_rules):
    for category, keywords in category_rules.items():
        for keyword in keywords:
            if keyword in description:
                return category
    return "Uncategorized"

def add_categories(transactions, category_rules):
    transactions = transactions.copy()
    transactions['Category'] = transactions['Description'].apply(category_rules)
    return transactions


def calculate_total_spent(transactions):
    total_spent = abs(transactions['Amount'].sum())
    return total_spent
        # f"{sum_expense:,.2f}"


def calculate_category_totals(transactions):
    # Expenses are stored as negative values in the CSV.
    # abs() makes spending totals easier to display to the user.
    category_totals = abs(transactions.groupby('Category')['Amount'].sum()).sort_values(ascending = False)
    return category_totals


def get_top_expenses(transactions):
    top_expenses = transactions.sort_values(by = ['Amount']).head(3)
    return top_expenses


def print_category_summary(category_totals, total_spent):
    for category, amount in category_totals.items():
        percentage = (amount / total_spent) * 100
        price = f'£{amount:.2f}'
        print(f'{category:<15}  {price:>8} {percentage:>8.1f}%')



def print_top_expenses(transactions):
    top_expenses = get_top_expenses(transactions)
    rank = 1

    for index, row in top_expenses.iterrows():
        date_text = row['Date'].strftime('%d/%m/%Y')
        amount_text = f"£{abs(row['Amount']):,.2f}"
        description_text = row['Description'].upper()
        print(f"{rank}. {date_text}  {description_text:<25} {amount_text:>5}")
        rank += 1


data = load_transactions('C:data\sample_transaction.csv')
data = clean_transaction(data)
def print_summary(transactions, month, year):
    current_month = datetime.datetime.now().strftime('%B')
    current_year  = datetime.datetime.now().strftime('%Y')
    total_transaction = len(data)


    print('==============================')
    print(f'SPENDING SUMMARY: {current_month.upper()} {current_year}')
    print('==============================')
    print(f'TOTAL SPENT: £{calculate_total_spent(data)}  ({total_transaction} TRANSACTIONS) ')
    print('\n')
    print(f'BY CATEGORY:')
    print_category_summary(calculate_category_totals(data), calculate_total_spent(data))
    print('\n')
    print(f'TOP 3 BIGGEST PURCHASES:')
    print_top_expenses(get_top_expenses(data))


print_summary(data)
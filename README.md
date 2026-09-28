# Personal Finance Tracker

## What this project does
A script that summarizes my spending from a CSV.

## Status
- [ ] Planning
- [ ] Reading CSV
- [ ] Parsing & cleaning data
- [ ] Filtering to current month
- [ ] Calculating total spend
- [ ] Categorizing expenses
- [ ] Top 3 purchases
- [ ] Output/summary

## Input format
- Source of CSV: (which bank/export, or "manually defined format")
- Columns present: (e.g. date, type, description, amount)
- Date format: (e.g. DD/MM/YYYY)
- How spending vs income is represented: (e.g. negative = spend, or separate debit/credit columns)
- Sample row:

date,type,description,amount
28/08/2026,expense,TESCO STORES 2087,-42.15
30/08/2026,expense,TFL TRAVEL CH,-18.40
31/08/2026,income,SALARY ACME LTD,1850.00

## Categorization approach
- Method: (keyword matching / manual mapping file / other)
- Where rules are stored: (e.g. category_rules.json)
- Default category for unmatched transactions: (e.g. "Uncategorized")
- Categories in use:
  - Groceries
  - Transport
  - ...

## Data structure
- How a transaction is represented in code: (dict / namedtuple / class — and its fields)

## Project structure

## How to run it


## Sample Output
==============================
 SPENDING SUMMARY: SEPTEMBER 2026
==============================
Total spent: £1,231.61  (23 transactions)

BY CATEGORY
Housing             £650.00   52.8%
Groceries           £201.25   16.3%
Shopping            £148.39   12.0%
Eating Out           £75.80    6.2%
Transport            £74.00    6.0%
Health & Fitness     £39.19    3.2%
Subscriptions        £22.98    1.9%
Uncategorized        £20.00    1.6%

TOP 3 BIGGEST PURCHASES
1. 01/09/2026  LANDLORD RENT PAYMENT   £650.00
2. 08/09/2026  UNIQLO ONLINE            £79.90
3. 15/09/2026  TESCO STORES 2087        £61.05

## Decisions & things I looked up
(running log — every time you have to Google/look something up, note it here with a one-line summary. This becomes your own reference and shows your learning process)
- e.g. "Used datetime.strptime to parse dates — format codes are %d/%m/%Y"

## Known limitations / not doing yet
(be explicit about what v1 does NOT do, so scope creep doesn't sneak in)
- e.g. only handles one month at a time
- e.g. no GUI, terminal output only
- e.g. categorization is keyword-based, not perfect

## Ideas for later (v2+)
(park feature ideas here instead of building them now)
- e.g. pandas refactor
- e.g. charts/visualization
- e.g. multi-month trends

  

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
  - Shopping 
  - Online Shopping
  - Eating Out  
  - Transport
  - Groceries
  - Subscriptions
  - Health
  - Phone
  - House

## Data structure
- How a transaction is represented in code: (dict / namedtuple / class — and its fields)

## Project structure

## How to run it


## Sample Output
==============================
SPENDING SUMMARY: OCTOBER 2026
==============================
TOTAL SPENT: £1,231.61  (23 TRANSACTION) 


BY CATEGORY:
House             £650.00     52.8%
Groceries         £201.25     16.3%
Online Shopping   £103.39      8.4%
Transport          £84.99      6.9%
Eating Out         £75.80      6.2%
Shopping           £45.00      3.7%
Subscriptions      £36.98      3.0%
Uncategorized      £20.00      1.6%
Health             £14.20      1.2%


TOP 3 BIGGEST PURCHASES:
1. 01/10/2026  LANDLORD RENT PAYMENT     £650.00
2. 08/10/2026  UNIQLO ONLINE             £79.90
3. 15/10/2026  TESCO STORES 2087         £61.05

## Decisions & things I looked up

### Data format decisions
- CSV columns: date, type, description, amount
- Date format: DD/MM/YYYY
- `type` column uses "income" / "expense" rather than bank-style transaction types — makes filtering spend vs income a simple equality check instead of relying on the sign of `amount`
- Amounts: expenses stored as negative numbers, income as positive
- Category names in category_rules.json are Capitalized (e.g. "Groceries") since they're displayed to the user; keyword lists are lowercase to match the lowercased description during matching

### Categorization logic
- Keyword matching is case-insensitive: both the transaction description and the keywords are lowercased before comparing, since bank CSV descriptions come through in uppercase
- Matching checks whether a keyword is a *substring* of the description (not an exact/whole-word match) — e.g. "tesco" matches inside "TESCO STORES 2087"
- First matching category wins; once a match is found the function returns immediately rather than checking for further matches
- Unmatched transactions default to "Uncategorized"

### Top 3 purchases
- Decided whether rent (a Standing Order / non-card type) counts as a "purchase" for the top 3 — [fill in whichever you went with]
- Sorting: because expense amounts are stored as negative, sorting `amount` in ascending order naturally puts the biggest expenses first (most negative = biggest spend) — the opposite of sorting the positive category totals, which needed `ascending=False` to get the same effect

### Bugs/gotchas hit while building
- Looping over a pandas Series/dict without `.items()` tries to unpack a single value into two variables and throws "cannot unpack non-iterable" — fixed by adding `.items()` so each loop pass gives both the label and the value
- Wrapping a function that already prints internally in an outer `print()` call (e.g. `print(group_categories())`) prints an extra "None" afterward, since the function doesn't explicitly return anything — fixed by calling the function on its own line
- F-strings can't use the same quote character both to open the f-string and inside a dictionary/column lookup within it (e.g. `f'...{row['Amount']}...'` breaks) — fixed by using double quotes inside when the f-string itself uses single quotes
- Aligning a number with a format spec (e.g. `{val:>8,.2f}`) only pads the number itself — a currency symbol typed outside that spec stays fixed in place, creating a gap. Fixed by building the full "£123.45" string first, then applying alignment to that whole string
- Testing "this month" filtering against a fixed sample CSV breaks once the real calendar month changes, since the filter is based on today's actual date — had to update the sample CSV's dates to stay in the current month during testing

### Tooling
- Used pandas (DataFrames) rather than plain Python lists/dicts for reading and processing the CSV
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

  

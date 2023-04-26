import datetime

def parse_expenses(expenses_string):
    """Parse the list of expenses and return the list of triplets (date, amount, currency).
    Ignore lines starting with #.
    Parse the date using datetime."""
    expenses = []
    for line in expenses_string.split(" "):
        if line.strip().startswith("#"):
            continue
        date, value, currency = line.strip().split(" ")
        expenses.append((datetime.datetime.strptime(date, "%Y-%m-%d"), 
                         float(value), 
                         currency))
    return expenses

expenses_data = """2023-01-02 -34.01 USD
                   2023-01-03 2.59 DKK
                   2023-01-03 -2.72 EUR"""

if __name__ == '__main__':
    expenses = parse_expenses(expenses_data)
    for expense in expenses:
        print(expense)
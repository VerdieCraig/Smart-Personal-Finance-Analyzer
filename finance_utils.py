import csv
from datetime import datetime

def load_transactions(filename='SampleTrans.csv'): #   SampleTrans.csv has the first 35 transactions of financial_transactions.csv
    transactions = []
    #   Load transactions from csv file into list of dictionaries
    error_log = []

    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    date = datetime.strptime(row['date'], '%Y-%m-%d').date()
                    #   Parse date with datetime.strptime
                  
                    amount = float(row['amount'])
                    if row['type'] == 'debit':
                        amount = -amount
                        #   Make amount negative for 'debit'
                    
                    transaction = {
                        'transaction_id': int(row['transaction_id']),
                        'date': date,
                        'customer_id': int(row['customer_id']),
                        'amount': amount,
                        'type': row['type'],
                        'description': row['description']
                    }
                    transactions.append(transaction)
                    #   Add to transactions

                except ValueError:
                    print(f"Invalid money format {row['amount']}")
                    print(f"Invalid date format {row['date']}")
                # Skip rows with invalid date or amount
                error_log.append(f"Skipped row due to ValueError: {row}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []

    # Write errors to errors.txt
    if error_log:
        with open('errors.txt', 'w') as err_file:
            for err in error_log:
                err_file.write(err + '\n')

    print(f"Loaded {len(transactions)} valid transactions.")
    return transactions
    
def add_transaction(transactions):
    try:
        # Get and validate date
        date_str = input("Enter transaction date (YYYY-MM-DD): ")
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        # Get and validate customer ID
        customer_id = int(input("Enter customer ID (number): "))

        # Get and validate amount
        amount = float(input("Enter amount: "))

        # Get and validate type
        type_ = input("Enter transaction type (credit, debit, transfer): ").lower()
        if type_ not in ['credit', 'debit', 'transfer']:
            print("Invalid type. Must be 'credit', 'debit', or 'transfer'.")
            return

        if type_ == 'debit':
            amount = -amount  # Make debit amounts negative

        # Get description
        description = input("Enter transaction description: ")

        # Generate new ID (assumes max ID + 1)
        if transactions:
            new_id = max(t['transaction_id'] for t in transactions) + 1
        else:
            new_id = 1

        # Create and add transaction
        new_transaction = {
            'transaction_id': new_id,
            'date': date,
            'customer_id': customer_id,
            'amount': amount,
            'type': type_,
            'description': description
        }

        transactions.append(new_transaction)
        print("Transaction added successfully!")

    except ValueError as ve:
        print(f"Invalid input: {ve}")

def view_transactions(transactions):
    """Display transactions in a simple table."""
    if not transactions:
        print("No transactions to display.")
        return

    print("\n{:<5} {:<12} {:<10} {:>10} {:<10} {}".format(
        "ID", "Date", "Customer", "Amount", "Type", "Description"))
    print("-" * 70)
    for t in transactions:
        print("{:<5} {:<12} {:<10} {:>10.2f} {:<10} {}".format(
            t['transaction_id'], str(t['date']), t['customer_id'],
            t['amount'], t['type'], t['description']))

def update_transaction(transactions):
    """Update a transaction’s details."""
    if not transactions:
        print("No transactions to update.")
        return

    view_transactions(transactions)

    try:
        tid = int(input("Enter the ID of the transaction to update: "))
        transaction = next((t for t in transactions if t['transaction_id'] == tid), None)

        if not transaction:
            print("Transaction not found.")
            return

        print("Fields you can update: date, customer_id, amount, type, description")
        field = input("Enter the field to update: ").lower()

        if field not in transaction:
            print("Invalid field.")
            return

        new_value = input(f"Enter new value for {field}: ")

        if field == 'date':
            transaction['date'] = datetime.strptime(new_value, '%Y-%m-%d').date()
        elif field == 'customer_id':
            transaction['customer_id'] = int(new_value)
        elif field == 'amount':
            transaction['amount'] = float(new_value)
        elif field == 'type':
            if new_value.lower() not in ['credit', 'debit', 'transfer']:
                print("Invalid transaction type.")
                return
            transaction['type'] = new_value.lower()
        elif field == 'description':
            transaction['description'] = new_value

        print("Transaction updated successfully!")

    except ValueError as e:
        print(f"Invalid input: {e}")

def delete_transaction(transactions):
    """Delete a transaction by ID."""
    if not transactions:
        print("No transactions to delete.")
        return

    view_transactions(transactions)

    try:
        tid = int(input("Enter the ID of the transaction to delete: "))
        transaction = next((t for t in transactions if t['transaction_id'] == tid), None)

        if not transaction:
            print("Transaction not found.")
            return

        confirm = input(f"Are you sure you want to delete transaction {tid}? (y/n): ").lower()
        if confirm == 'y':
            transactions.remove(transaction)
            print("Transaction deleted.")
        else:
            print("Delete cancelled.")

    except ValueError:
        print("Invalid input.")

def analyze_finances(transactions):
    """Calculate and display financial summaries."""
    # Sum credits, debits, transfers
    # Group by type or customer_id
    # Print results
    pass

def save_transactions(transactions, filename='financial_transactions.csv'):
    """Save transactions to a CSV file."""
    # Open file for writing
    # Write header
    # Write each transaction
    pass

def generate_report(transactions, filename='report.txt'):
    """Generate a text report of financial summaries."""
    # Calculate metrics
    # Write to file
    pass
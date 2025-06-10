import csv
import finance_utils

def main():
    transactions = []
    
    while True:
        print("\nSmart Personal Finance Analyzer")
        print("1. Load Transactions")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Update Transaction")
        print("5. Delete Transaction")
        print("6. Analyze Finances")
        print("7. Save Transactions")
        print("8. Generate Report")
        print("9. Exit")
        choice = input("Select an option: ")
        # Call functions based on choice
        
        if choice == '1':
            transactions = finance_utils.load_transactions()
        elif choice == '2':
            finance_utils.add_transaction(transactions)
        elif choice == '3':
            finance_utils.view_transactions(transactions)
        elif choice == '4':
            finance_utils.update_transaction(transactions)
        elif choice == '5':
            finance_utils.delete_transaction(transactions)
        elif choice == '6':
            finance_utils.analyze_finances(transactions)
        elif choice == '7':
            finance_utils.save_transactions(transactions)
        elif choice == '8':
            finance_utils.generate_report(transactions)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
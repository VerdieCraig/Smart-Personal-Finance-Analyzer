# Smart Personal Finance Analyzer

A command-line Python application for managing and analyzing personal financial transactions using CSV files.

## 📂 Project Structure

- `finance_utils.py` — All core finance functions  
- `main.py` — Entry point with the interactive menu  
- `SampleTrans.csv` — Sample data file (35 transactions)  
- `errors.txt` — Auto-generated log of bad or skipped input rows  
- `report.txt` — Optional summary report output  

## 🚀 Features

- Load transactions from a CSV file  
- Add, view, update, or delete transactions  
- Analyze financial summaries by transaction type  
- Save updated transactions to file  
- Generate a clean text-based financial report  

## 🛠 Requirements

- Python 3.7 or higher  
- No external packages required  

## ▶️ How to Run

1. **Clone the repo**

   ```bash
   git clone https://github.com/VerdieCraig/Smart-Personal-Finance-Analyzer.git
   cd Smart-Personal-Finance-Analyzer
   ```

2. **(Optional) Set up a virtual environment**

   ```bash
   python -m venv .venv
   ```

   **On macOS/Linux:**

   ```bash
   source .venv/bin/activate
   ```

   **On Windows:**

   ```bash
   .venv\Scripts\activate
   ```

3. **Run the program**

   ```bash
   python main.py
   ```

   Follow the menu prompts to load, view, add, or analyze transactions.

## 📝 Notes

- The app expects a valid CSV file named `SampleTrans.csv` in the same directory. You can replace this with your own file.  
- Invalid data (bad dates, amounts, etc.) will be logged to `errors.txt`.  
- Running the "Generate Report" option creates a summary in `report.txt`.  

## 📄 License

This project is dedicated to the public domain under the [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

You are free to:

- Use, modify, and distribute the code for any purpose, including commercial use  
- Do so without asking for permission or giving credit  

No copyright or related rights are retained.

# expense.py
# Chris Waghorn – UK expense tracker – GUARANTEED to work in Pydroid 3

import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

CSV_FILE = "expenses.csv"
CHART_FILE = "expenses_chart.png"

# Create file if missing
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        csv.writer(f).writerow(["date", "description", "amount_gbp"])

def add():
    print("\nADD EXPENSE")
    desc = input("What did you buy? (or press Enter to cancel): ")
    if not desc.strip():
        return
    while True:
        a = input("How much in £? ")
        try:
            amount = float(a)
            break
        except:
            print("Type a number like 4.99")
    today = datetime.now().strftime("%Y-%m-%d")
    with open(CSV_FILE, "a", newline="") as f:
        csv.writer(f).writerow([today, desc, amount])
    print(f"£{amount:.2f} saved!\n")

def total():
    if os.path.getsize(CSV_FILE) == 0:
        print("\nNo expenses yet\n")
        return
    t = sum(float(r[2]) for r in csv.reader(open(CSV_FILE)) if len(r) >= 3 and r[0] != "date")
    print(f"\nTOTAL SPENT SO FAR: £{t:.2f}\n")

def chart():
    entries, amounts = [], []
    with open(CSV_FILE) as f:
        next(csv.reader(f), None)  # skip header
        for i, row in enumerate(csv.reader(f), 1):
            if len(row) >= 3:
                entries.append(f"{i}. {row[1][:10]}")  # "1. Coffee", "2. Lunch" etc.
                amounts.append(float(row[2]))
    if not amounts:
        print("\nAdd some expenses first!\n")
        return
    plt.figure(figsize=(10,6))
    plt.bar(entries, amounts, color="#e74c3c")
    plt.title("Chris Waghorn – Every Expense 2025")
    plt.ylabel("£ GBP")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=200)
    plt.close()
    print(f"\nChart saved → {CHART_FILE} (one bar per purchase!)\n")

# MAIN MENU – runs instantly
print("\n" + "═"*50)
print("   CHRIS'S UK EXPENSE TRACKER")
print("═"*50)
print("1 – Add expense")
print("2 – Show total")
print("3 – Make chart")
print("q – quit")
print("═"*50)

while True:
    c = input("Choose 1/2/3/q → ").strip().lower()
    if c in ["1","2","3","q"]: break
    print("Type 1, 2, 3 or q")

if   c == "1": add()
elif c == "2": total()
elif c == "3": chart()

print("Done – run me again anytime!")
print("Every £ tracked = £5k+/month future salary getting closer\n")
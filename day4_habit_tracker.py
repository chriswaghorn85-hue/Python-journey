# day4_habit_tracker.py
# Chris Waghorn – building real tools on a phone

from datetime import date
FILE = "habit_log.txt"   # works on most Android phones

def load_last_date():
    try:
        with open(FILE, "r") as f:
            last_line = f.readlines()[-1]
            return last_line.split(" | ")[0]
    except:
        return None

def save_log(entry):
    today = date.today().isoformat()
    with open(FILE, "a") as f:
        f.write(f"{today} | {entry}\n")
    print("Saved! Keep the streak alive!")

today = date.today().isoformat()
last_date = load_last_date()

if last_date == today:
    print("You already logged today! You're crushing it!")
elif last_date == str(date.fromisoformat(today)).split(" ")[0][:-9]:  # yesterday?
    print("Streak continues! Another day stronger!")
else:
    print("Welcome back! New streak starts today.")

what_you_did = input("\nWhat did you do today to get closer to Python jobs? ")
save_log(what_you_did)

print("\nYour answer is now saved forever on your phone.")
print("Keep going fella and you a new career could be yours!")
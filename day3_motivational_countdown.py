# day3_motivational_countdown.py
# Chris Waghorn – learning by breaking and fixing

from datetime import date

name = input("Enter your name genius: ")
days_per_week = 7

today = date.today()
next_birthday = date(today.year, 9, 4)     # ← your birthday
if today > next_birthday:
    next_birthday = date(today.year + 1, 9, 4)

days_left = (next_birthday - today).days

print("=" * 40)
print(f"\033[92m{name.upper()}\033[0m")
print(f"Only {days_left} days until you turn another year wiser!")
print(f"That's just {days_left // days_per_week} weeks and {days_left % days_per_week} days!")
print("Every day you code = one day closer to getting paid for this.")
print("=" * 40)
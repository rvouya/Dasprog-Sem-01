month = int(input("Enter month (1-12) : "))
day = int(input("Enter day (1-31 ): "))
year = int(input("Enter year : "))

is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if is_leap_year:
    days_in_month[1] = 29

if not (1 <= month <= 12):
    print("Invalid month")
elif not (1 <= day <= days_in_month[month - 1]):
    print("Invalid day for the given month")
else:
    day_of_year = 0
    for i in range(month - 1):
        day_of_year += days_in_month[i]
    day_of_year += day

print(f"Date {month}/{day}/{year} is day {day_of_year} of {year}.")

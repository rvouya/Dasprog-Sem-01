minutes_free = 600
flat_rate = 3999 
additional = 0.40  
tax = 0.0525  

work_day = int(input("Enter workday usage in minutes: "))
night = int(input("Enter night usage in minutes: "))
weekend = int(input("Enter weekend usage in minutes: "))

extra_money = max(0, work_day - minutes_free) * additional * 100 
total_cost = flat_rate + extra_money
total_minutes = work_day + night + weekend
avg_per_minute = total_cost / total_minutes if total_minutes > 0 else 0
taxes = total_cost * tax
total_cost_with_tax = total_cost + taxes

print("\nBill Details:")
print(f"Workday usage: {work_day} minutes")
print(f"Night usage: {night} minutes")
print(f"Weekend usage: {weekend} minutes")
print(f"Flat rate: ${flat_rate / 100:.2f}")
print(f"Additional charges: ${extra_money / 100:.2f}")
print(f"Cost before tax: ${total_cost / 100:.2f}")
print(f"Cost per minute: ${avg_per_minute / 100:.2f}")
print(f"Tax: ${taxes / 100:.2f}")
print(f"Total cost: ${total_cost_with_tax / 100:.2f}")
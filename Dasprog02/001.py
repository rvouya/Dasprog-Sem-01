import math
import sys

purchase_total = float(input("Enter the total price : "))
identify = input("Are you a student (yes/no)? ").strip().lower()

if identify not in ('yes', 'no'):
    print("Please answer with 'yes' or 'no'")
    sys.exit()
elif identify == 'yes':
    discount = 0.20
else:
    discount = 0.00

students_discount = discount * purchase_total
discounted_total = purchase_total - students_discount
sales_tax = discounted_total * 0.05
total = discounted_total + sales_tax

if identify == 'yes':
    print(f"Purchase total: ${purchase_total:.2f}")
    print(f"Discount applied: ${students_discount:.2f}")
    print(f"Total after discount: ${discounted_total:.2f}")
    print(f"Sales tax (5%): ${sales_tax:.2f}")
    print(f"Final amount due: ${total:.2f}")
else:
    print(f"Purchase total: ${purchase_total:.2f}")
    print(f"Sales tax (5%): ${sales_tax:.2f}")
    print(f"Final amount due: ${total:.2f}")
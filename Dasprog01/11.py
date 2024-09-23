#pythagoras
m = int(input("Enter the value for m : "))
n = int(input("Enter the value for n : "))

import sys
if m <= n:
    print("m must be greater than n.")
    sys.exit()
else:
    side1 = m**2 - n**2
    side2 = 2 * m * n
    hypotenuse = m**2 + n**2
    
print(f"side 1 = {side1}")
print(f"side 2 = {side2}")
print(f"hypotenuse = {hypotenuse}")
hours, minutes = map(int, input("Enter hours and minutes since the power failure: ").split())
t = hours + minutes/60
import sys
#formula
if t == -2:
    print("Invalid input, please try again")
    SystemExit
else:
    temperature = (4 * t**2 / (t + 2))-20

print(f"The temperature since the power failure are {temperature:.2f}")
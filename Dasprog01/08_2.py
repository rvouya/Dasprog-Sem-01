#toilet replace (asumsi kedua - ada yang gak pakai toilet)
import math

population = int(input("Enter population : "))
toilet = math.floor(float(population/3))

old_flush = int(15*toilet*14)
new_flush = int(2*toilet*14)

#formula
magnitude = int(old_flush - new_flush)
cost = float(150*toilet)

#output
print(f"Magnitude/water saved per day : {magnitude} liters/day")
print(f"Cost of the water saved based on the community's population : ${cost}")
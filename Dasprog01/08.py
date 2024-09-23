#toilet replace (asumsi pertama - semua toilet terpakai)

""""
yang lama : 15 liters per flush, yang baru : 2 liters per flush.
setiap hari toilet di flush 14 kali.
dan 1 toilet every 3 persons
cost buat install toilet baru : $150
"""

import math

population = int(input("Enter population : "))
toilet = math.ceil(float(population/3))

old_flush = int(15*toilet*14)
new_flush = int(2*toilet*14)

#formula
magnitude = int(old_flush - new_flush)
cost = float(150*toilet)

#output 
print(f"Magnitude/water saved per day : {magnitude} liters/day")
print(f"Cost of the water saved based on the community's population : ${cost}")
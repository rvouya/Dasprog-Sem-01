#barrel oil (42 gallons) = 5.800.000 BTU
efficiency_perc = int(input("Enter the efficiency (%): "))
gallons_oil = int(input("Enter gallons of oil : "))

#constant
btu_barrel = 5800000
gallons_barrel = 42

#formula
btu_per_gallons = btu_barrel / gallons_barrel
btu_total = gallons_oil * btu_per_gallons

efficiency = efficiency_perc / 100.0

btu_delivered = btu_total * efficiency

#output
print(f"BTUs of heat delivered to the house : {btu_delivered:.2f} BTU")
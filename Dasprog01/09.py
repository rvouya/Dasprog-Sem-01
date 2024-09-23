#input
yard_p = float(input("Enter the length of the yard (feet): "))
yard_l = float(input("Enter the width of the yard (feet): "))
house_p = float(input("Enter the length of the house (feet): "))
house_l = float(input("Enter the width of the house (feet): "))

cutting_rate = 2 #two swuare feet a second ceunah

#formula
yard_area = yard_p * yard_l
house_area = house_p * house_l

area_left = abs(yard_area - house_area)

time = area_left / cutting_rate

#output
print(f"Time required to cut the grass : {time} seconds")
x, y = map(float, input("Enter the coordinate separated by a comma and a space : ").split(', '))
coordinates = x, y

if (x < 0):
    if y < 0:
        print(f"{coordinates} is in quadrant III")
    if y > 0:
        print(f"({coordinates} is in quadrant II")
elif (x > 0):
    if y < 0:
        print(f"{coordinates} is in quadrant IV")
    if y > 0:
        print(f"{coordinates} is in quadrant I")
elif (x == 0):
    print(f"{coordinates} is on the y-axis")
elif (y == 0):
    print(f"{coordinates} is on the x-axis")
else:
    ValueError
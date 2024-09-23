volume = int(input("Volume to be infused (ml) : "))
minutes = int(input("Minutes over which to infuse : "))

hours = minutes/60
infusion_rate = int(volume/hours)

print(f"VBTI : {volume} ml")
print(f"Rate : {infusion_rate} ml/hr")
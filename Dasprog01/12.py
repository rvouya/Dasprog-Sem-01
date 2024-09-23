#acceleration
#jet's takeoff speed(km/hr) to meters/sec, distance(meters)
v = float(input("Enter take off speed : ")) * 1000/3600
s = float(input("Enter the distance : "))

#formula
t = float((2*s)/v)
a = float(v/t)

print(f"The acceleration of the jet is {a:.2f} m/s^2")
print(f"The time for the fighter to be accelerated to takeoff speed is {t:.2f}s")
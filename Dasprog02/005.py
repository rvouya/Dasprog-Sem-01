n = float(input("The amount of data used (Gbps) : "))

if 0.0 < n <= 1.0:
    charges = "250"
elif 1.0 < n <= 2.0:
    charges = "500"
elif 2.0 < n <= 5.0:
    charges = "1000"
elif 5.0 < n <= 10.0:
    charges = "1500"
elif n > 10.0:
    charges = "2000"
else:
    print("Data invalid, try again")
    exit()

print(f"Charges to be paid : {charges}")
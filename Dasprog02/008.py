print("(1) First Free Service\n(2) Second Free Service")

service_number = int(input("Enter the Free Service number>> "))
miles = int(input("Enter number of miles>> "))

if service_number == 1:
    if 1500 < miles <= 3000:
        print("Vehichle must be serviced")
    else:
        print("Vehichle doesn't need any service")
elif service_number == 2:
    if 3001 < miles <= 4500:
        print("Vehichle must be serviced")
    else:
         print("Vehichle doesn't need any service")
else:
    print("Invalid Free Service Number, Please try again")
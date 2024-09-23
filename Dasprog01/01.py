#taxi fare calculator

#variables
awal = float(input("Jarak Awal : "))
akhir = float(input("Jarak Akhir : "))
jarak_total = float(abs(akhir-awal))

#bulat = format(jaraktotal, ".2f")
harga = float(jarak_total*1.50)
bulat_harga = format(harga, ".2f") 
print("Harga yang dibayar : "+ str(bulat_harga))
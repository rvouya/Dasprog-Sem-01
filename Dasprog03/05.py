n_item = int(input().strip())  
item_dict = {}  # Inisialisasi dictionary untuk menyimpan item dan kuantitas

for _ in range(n_item):
    item_name, quantity = input().strip().split()
    item_dict[item_name] = int(quantity)  # Yang item name jadi str yang quantity jadi interger

# Item yang charlie curi
c_item = int(input().strip()) 
charlie_items = []  # list untuk menyimpan item yang diambil Charlie

# Membaca item yang diambil Charlie dan menghitung kuantitas yang tersisa dalam satu loop
for _ in range(c_item):
    item_name, quantity = input().strip().split()
    quantity = int(quantity)  # Mengubah kuantitas menjadi integer
    
    if item_name in item_dict:
        charlie_items.append(item_name) 
        item_dict[item_name] -= quantity  

if charlie_items:
    print("CHARLIE")
    print(" ".join(charlie_items))

print("STORAGE")
for name, quantity in item_dict.items():
    print(f"{name.capitalize()}: {quantity}")
#Satu sections 30 orang kan, nah krn ga semuanya bisa masuk jd dibagi trs leftovernya pakai mod
students_enrolled = int(input("Enter the number of students endrolled: "))

import sys
if students_enrolled < 0:
    print("Invalid input, cannot be negative.")
    sys.exit()
        
capacity = 30
        
sections = students_enrolled // capacity
leftover_students = students_enrolled % capacity
        
if leftover_students > 0:
    sections += 1
        
print(f"Jumlah siswa yang terdaftar: {students_enrolled}")
print(f"Jumlah bagian yang diperlukan: {sections}")
print(f"Jumlah siswa yang tersisa: {leftover_students}")
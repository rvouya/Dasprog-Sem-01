#hydroelectric dam program
'''
intinya apa? kita nyari daya yang bisa dikeluarkan si dam ini kan
nah, kita perlu work/usaha, tapi cari massa airnya dulu. jadi flow water dibagi 1000(di soal)
udah dapat kan, tinggal cari power watt, setelah itu konversi ke megawatt
'''
#input height
height = int(input("The height of the dam : "))

#water cubics per second
flow_rate = float(input("Water flow per second : "))

#constant
efficiency = float(input("Enter effiency constant : "))

#constant
gravity = 9.80 #m/s^2

#water mass, 1000kg/cubic meter - di soal
water_mass = flow_rate*1000 

#usaha dalam joule
work = float(water_mass*height*gravity)

#menghitung efisiensi (watt=joule/detik)
power_w = work*efficiency

#watt menjadi megawatti
power_mw = power_w/10**6

#output, ".2f" ini untuk ngebatasin angka jadi 2 dibelakang koma. kalau ".f" aja cuma satu dibelakang koma
print(f"Daya listrik yang dihasilkan bendungan adalah {power_mw:.2f} KW")
U = int(input())
K = int(input())
M = int(input())

jum_minion = M//2
jum_knight = K//2

gate_1 = U - (jum_minion*2)
gate_2 = gate_1 - ((jum_knight*5))*5
gate_3 = gate_2 - ((100)*10)

if gate_3 > 0:
    print(f"Yey! Ucup Menang! HP tersisa: {gate_3}")

else:
    print("Yah! Ucup Meninggoy.")
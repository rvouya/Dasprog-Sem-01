n, k = input().split()
a = list(map(int, input().split()))
# counter = len([x for x in a if x <= int(k)])
# if counter == 0:
#     print("Minggir lu miskin.")
# else:
#     print(counter)
buah = 0
for jumlah in a:
    if int(a) <= k:
        break
    else:
        buah += 1
print(buah)
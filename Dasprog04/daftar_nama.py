n, r, c = map(int, input().split())
a = []
for _ in range(n):
    x, a_input, b = map(int, input().split())
    a.append(a_input)

a.sort()
counter = {}

if a_input > r or b > c:
    print("Salah ukuran grid bang.")
else:
    for i in a:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1

    for angka, teman in counter.items():
        print(teman)
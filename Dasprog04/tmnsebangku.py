n, r, c = map(int, input().split())
posisi = {}
for _ in range(n):
    x, a, b = map(int, input().split())
    posisi[(a, b)] = x

for (a, b), x in posisi.items():
    left = posisi.get((a, b - 1))
    right = posisi.get((a, b + 1))
    
    if right is not None:
        print(right)
    if left is not None:
        print(left)
    if left is None and right is None:
        print('0')
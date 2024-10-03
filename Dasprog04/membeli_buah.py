n, k = input().split()
a = list(map(int, input().split()))

count = 0
for i in a:
    if i <= int(k):
        count += 1

print(count)

N = int(input())
B = list(map(int, input().split()))
k = 1
for i in range(N):
    for j in range(i+1, N):
        if B[i]==B[j]:
            k += 0
        else:
            k *= B[i]^B[j]
print(k)

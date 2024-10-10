t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    q = int(input())
    if q == 1:
        print(sum(a))
    elif q == 2:
        print(min(a))
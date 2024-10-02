N, M = input().split()
P = list(map(int, input().split()))
C = list(map(int, input().split()))

positive_P = (k for k in P if k > 0)
negative_C = (k for k in C if k < 0)
# negatives_to_add = negative_C[:sum(1 for k in P if k > 0)]

if not negative_C:
    print("Selamat uangmu cukup.")
else:
    result = sum(negative_C) - sum(positive_P)
    print(result)
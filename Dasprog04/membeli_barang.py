N, M = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))
# negatives_to_add = negative_C[:sum(1 for k in P if k > 0)]

post_P = [i for i in P if i >= 0]
post_C = [j for j in C if j >= 0]
minus_P = [i for i in P if i < 0]
minus_C = [i for i in C if i < 0]

if len(C) == len(post_C) and len(P) == len(post_P):
    hutang = min(post_C) - sum(post_P)
    print(hutang)
elif minus_P and not post_C:
    hutang = sum(minus_C) - max(minus_P)
    print(hutang)
elif not post_P and post_C:
    print("0")
else:
    hutang = sum(minus_C) - sum(post_P)
    print(hutang)

#Test case AC semua bos

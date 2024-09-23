a = list(map(int, input().split()))
b = int(input())
c = int(input())
d, e, f = map(int, input().split())
for i in range(c):
    temp = a[:7-b]
    a[:7-b] = a[-b:]
    a[-b:] = temp #temp untuk menyimpan storage(?)
print(a[d], a[e], a[f])
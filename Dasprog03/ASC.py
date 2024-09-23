from statistics import mode
room_amount = int(input())
color_id = list(map(int, input().split()))
frequency = {}
for num in color_id:
    frequency[num] = frequency.get(num, 0) + 1

modus = max(frequency, key=frequency.get)
#menentukan modus dari color_id

changes_needed = 0 
for i in color_id:
    if i != modus: 
        changes_needed += 1 #kalau bukan modusnya, berarti changes nya ditambahin satu
print(changes_needed)
#gblh pk library
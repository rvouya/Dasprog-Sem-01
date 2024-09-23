"""
intinya, bisa pass atau engga + sisa mobil.
so, jadi mas abdan pakai mod supaya gampang nyari sisa ok.
misal 200, 200/85 sisa 30 nah 25 buat red + yellow sign, so 5s terakhir mobil paling terakhir.
"""
M, N, T = map(int, input().split())
cycle_period = 85
remaining_time = T % cycle_period

if remaining_time > 25:
    remaining_green = remaining_time - 25
else:
    remaining_green = 0
cars_out = ((T//85)*12) + remaining_green//5
cars_left = (M + N + 1) - cars_out

print(f"YES! {cars_left}" if M + 1 <= cars_out else f"NO! {cars_left}")
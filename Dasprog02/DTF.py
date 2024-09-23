HH, MM, SS = map(int, input("").split(":"))
CH, CM, CS = map(int, input("").split(":"))
HH = HH + 5
streamtime = HH * 3600 + MM * 60 + SS
time = CH * 3600 + CM * 60 + CS
time_diff = streamtime - time
if time_diff < 0:
    print("See you on the next Pear Event!")
else:
    time_diff %= 3600
    hours = time_diff // 3600
    minutes = time_diff // 60
    seconds = time_diff % 60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
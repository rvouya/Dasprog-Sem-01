#mod 3 karena lili menang setiap perkalian 3
N, C = map(int, input().split())
if C == 1:
    if N%3 == 0:
        print("Lili")
    else:
        print("Lala")
elif C == 2:
    if N%3 == 0:
        print("Lala")
    else:
        print("Lili")
else:
    print("Please put a value between 1 and 2")
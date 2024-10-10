S = input()
N = int(len(S))
P = S[::-1]
if S == P:
    print("Palindrome King!")
elif S != P:
    print("Bukan King!")

n = int(input())
if n < 2:
    print("IT IS NOT A PRIME")
else:
    is_prime = all(n % i != 0 for i in range(2, n))
    print("IT IS A PRIME" if is_prime else "IT IS NOT A PRIME")
def generate_primes(up_to):
    primes = []
    for num in range(2, up_to + 1):
        is_prime = True  # Anggap bilangan saat ini adalah prima
        for p in primes:
            if p * p > num:  # Jika kuadrat p lebih besar dari num, hentikan
                break
            if num % p == 0:  # Jika num dapat dibagi oleh p, maka bukan prima
                is_prime = False
                break
        if is_prime:  # Jika masih dianggap prima, tambahkan ke list
            primes.append(num)
    return primes

# Menghasilkan bilangan prima hingga 78.498
prime = generate_primes(78498)

T = int(input())

test_cases = []
for _ in range(T):
    A, B = map(int, input().split())
    test_cases.append((A, B))

results = [
    f"Test Case #{i + 1} :\n" + "\n".join(str(prime) for prime in prime[A-1:B]) # dikonversi jadi string biar fungsi join gak error
    for i, (A, B) in enumerate(test_cases) # Enumerate buat mengetahui test case keberapa yang dipakai 
]

# Mencetak semua hasil
print("\n".join(results))
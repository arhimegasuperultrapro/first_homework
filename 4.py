

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = 0

for i in numbers:
    for j in range(2, int(i**0.5 + 2)):
        if i % j == 0 and i > j:
            not_primes.append(i)
            is_prime = False
            break
        else:
            is_prime = True


    if is_prime == True and i != 1:
        primes.append(i)

print(primes)
print(not_primes)




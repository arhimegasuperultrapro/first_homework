
def is_prime(func):
    def f(v1, v2, v3):
        val = func(v1, v2, v3)
        for i in range(2, round(val**0.5) + 1):
            if (val % i == 0) and (val != 2):
                return f"Составное\n{val}"
        return f"Простое\n{val}"
    return f


@is_prime
def sum_three(v1, v2, v3):
    return v1 + v2 + v3

result = sum_three(2, 3, 6)

print(result)
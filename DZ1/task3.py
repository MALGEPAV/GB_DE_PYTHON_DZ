import math

MAX = 100000


def is_prime(n):
    if n == 1 or n == 0:
        return f"{n} is NOT prime"
    k = 2
    while k <= math.sqrt(n):
        if n % k == 0:
            return f"{n} is composite."
        k += 1
    return f"{n} is prime."


n = int(input(f"Enter a non-negative integer not greater than {MAX}: "))
while n < 0 or n > MAX:
    n = int(input("Not a valid number!!\n"
                  "Enter a non-negative integer not greater than {MAX}: "))

print(is_prime(n))

import fractions


def my_gcd_non_neg(a: int, b: int) -> int:  # for non-negative numbers only
    if b == 0:
        return a
    if a % b == 0:
        return b
    return my_gcd_non_neg(b, a % b)


def my_gcd(a: int, b: int) -> int:
    return my_gcd_non_neg(a.__abs__(), b.__abs__())


def frac_sum(frac1: str, frac2: str) -> str:
    a1, b1 = int(frac1.split("/")[0]), int(frac1.split("/")[1])
    a2, b2 = int(frac2.split("/")[0]), int(frac2.split("/")[1])

    b = b1 * b2
    a = a1 * b2 + a2 * b1

    gcd = my_gcd(a, b)

    a_sum = a // gcd
    b_sum = b // gcd

    if a_sum == 0:
        return "0"

    return f"{a_sum}/{b_sum}"


def frac_mult(frac1: str, frac2: str) -> str:
    a1, b1 = int(frac1.split("/")[0]), int(frac1.split("/")[1])
    a2, b2 = int(frac2.split("/")[0]), int(frac2.split("/")[1])

    a = a1 * a2
    b = b1 * b2

    gcd = my_gcd(a, b)

    a_mult = a // gcd
    b_mult = b // gcd

    if a_mult == 0:
        return "0"

    return f"{a_mult}/{b_mult}"


print("My functions:")
print(f"2/3-4/5={frac_sum('2/3', '-4/5')}")
print(f"-2/3*3/4={frac_mult('-2/3', '3/4')}")
print()
print("Built-in functions:")
f1 = fractions.Fraction(2, 3)
f2 = fractions.Fraction(4, 5)
print(f"{f1}-{f2}={f1 - f2}")
f1 = fractions.Fraction(-2, 3)
f2 = fractions.Fraction(3, 4)
print(f"{f1}*{f2}={f1*f2}")

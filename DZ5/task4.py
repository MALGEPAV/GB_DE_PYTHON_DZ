def fib(n: int):  # n - desired amount of numbers
    if n > 0:
        yield 0
    if n > 1:
        yield 1
    fib_prev = 0
    fib_next = 1
    count = 2
    while count < n:
        fib_next += fib_prev
        fib_prev = fib_next - fib_prev
        yield fib_next
        count += 1


print(*fib(20))

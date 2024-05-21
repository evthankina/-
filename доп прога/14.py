def factorial_generator():
    n = 0
    factorial = 1
    while True:
        yield factorial
        n += 1
        factorial *= n

factorial_gen = factorial_generator()

for i in range(10):
    print(next(factorial_gen))

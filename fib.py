def fib(n):
    a, b = 0, 1

    while a < n:
        print(a, end=' ')
        a, b = b, a + b

    print()

n = int(input("digite o número limite para a sequência de Fibonacci: "))
fib(n)
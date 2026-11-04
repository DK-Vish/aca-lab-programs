def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
n = 8
for i in range(8):
    print(fib(i))

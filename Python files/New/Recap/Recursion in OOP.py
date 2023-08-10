## fib sequence
# class fib_seq:
#    def __init__(self, n):
#        self.n = n
#    def fibonacci(self, n):
#        if n == 1:
#            return 1
#        elif n == 2:
#            return 2
#        elif n>2:
#            return fibonacci(n-1) + fibonacci(n-2)
#    for n in range

from functools import lru_cache


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


for n in range(1, 11):
    print(str(fibonacci(n)) + "\n")

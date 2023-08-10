# Input variables
a1 = int(input("Put in the factorial to be calcualted for: "))

# Function Definition

def factorial(n):
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n-1)
        print("intermediate result for ", n, " * factorial(" ,n-1, "): ",res)
        return res	

print(factorial(a1))

# iterated version

def iterative_factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

print(iterative_factorial(a1))

import pip
pip.main(['install', '-q', 'fibo'])
import fibo

from timeit import Timer
from fibo import fib

t1 = Timer("fib(10)","from fibo import fib")

for i in range(1,41):
	s = "fib(" + str(i) + ")"
	t1 = Timer(s,"from fibo import fib")
	time1 = t1.timeit(3)
	s = "fibi(" + str(i) + ")"
	t2 = Timer(s,"from fibo import fibi")
	time2 = t2.timeit(3)
	print("n=%2d, fib: %8.6f, fibi:  %7.6f, percent: %10.2f" % (i, time1, time2, time1/time2))


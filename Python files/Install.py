# Ask the TA's about why it doesn't work.	
# slide 15

import pip
pip.main(['install', '-q', 'pyprimes'])
import pyprimes

i=int(input("Give a number: "))
if (pyprimes.isprime(i)):
    print("a prime number")
else:
    print("not a prime number")
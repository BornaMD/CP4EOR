import nashpy as nashpy
A = []

n = int(input("Put in max. guessers: "))

def Guess(n):
    if n <= 1:
        return 0
    elif n // 2/3 == 0:
        return sum_even(n*2/3)
    else:
        return sum_even(n*2/3) + n

print(Guess(n))
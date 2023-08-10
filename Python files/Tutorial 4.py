#Exercise 11

a1=int(input("Give No. 1: "))
a2=int(input("Give No. 2: "))
a3=int(input("Give No. 3: "))

L = [a1, a2, a3]

def middle(inputList):
    inputList = sorted(inputList)
    n = len(inputList)
    m = n - 1
    output = (inputList[int(n/2)] + inputList[int(m/2)]) / 2.0
    return output


print(middle(L))

#Exercise 15

def prime(givenNumber):  
    primes = [R]
    for possiblePrime in range(2, givenNumber + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break

        if isPrime:
            primes.append(possiblePrime)
    
    return(prime)

print(prime)

#Exercise 18

Wo = str(input("Give me a word: "))


def ispalindrome(word):
    word = [c for c in W.lower() if c.isalpha()]
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return ispalindrome(word[1:-1])


print(ispalindrome(Wo))

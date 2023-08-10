string = input("string: ")

s = string.islower()

if s == s[::-1]:
    print("palindrome")
else:
    print("not")

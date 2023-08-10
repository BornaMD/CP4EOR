import math
# 7
print(type(52))

# 8
fitness = 'avarage'
print(type(fitness))

# 9
print(5 - 3)

# 10
full_name = 'Ahmed' + '' + 'Walsh'
print(full_name)

# 11 
print(len(full_name))

# 18
num_subjects = int(input("Number of subjects taking part in the study: "))
num_per_survey = int(input("Number of subjects per survey: "))

num_surveys_needed = round(num_subjects/num_per_survey)
# 19
print(int(float("3.4")))

# 20
first = 1.0 
second = "1" 
third = "1.1"

print(first + float(second))
print(first + int(float(third)))

#21 
val = 4j
print(val.imag)
# 4 and 0

#22

a, b = 5, 3
c = 'test'
a = a % b
#print(a)
b *= b
#print(b)
a = c[1]
#print(a)
c = a = b = True
#print(a, b, c)
c = not(a or b)
#print(a, b, c)
a = b or c
b = str(a) + " Love"
print(a, b, c)

# 5; 3; -
# 5; 3; test
# 2; 3; test
# 2; 9; test
# e; 9; test
# True; True; True
# True; True; False
# True; True; False
# True True Love False

# 23
a = float(input("Length of side a in cm: "))
b = float(input("Length of side b in cm: "))
c = float(input("Length of side c in cm: "))

s = 0.5*(sum([a, b, c]))
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
print('The area of the triangle is %0.2f' %area)

# 24
A = float(input("Give in coefficient A: "))
B = float(input("Give in coefficient B: "))
C = float(input("Give in coefficient C: "))
try:
    root = math.sqrt(B**2-4*A*C)
except ValueError:
    print("Please enter 3 valid sides")


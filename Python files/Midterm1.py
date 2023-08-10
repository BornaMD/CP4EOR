#Exercise 1

sumo = 0

for number in range(10):
  sumo += number

print("The sum is: ", sumo)

#Exercise 2

message = ""

for number in range(10):
  if (number%3) == 0:
    message += "a"
  else:
    message += "b"

print(message)

#Exercise 3

product = 1
for i in range(1,10+1):
  product *= i
print(product)

sum_squares = 0
for i in range(10+1):
  i_sq = i**2
  sum_squares += i_sq
print(sum_squares)

nums = 0
for num in range(10+1):
  nums += num
print(nums)

#Exercise 4

for i in range(1,4+1):
  print("*"*i + "\n")
#Exercise 5

i=0

while i in range(20+1):
  n = (i**2)+1
  print(n, end=' ')
  i+=1

#Exercise 6

s="hello world! 123"
l = 0
d = 0

letters = "abcdefghijklmnopqrstuvw"
digits = "1234567890"

for i in range(len(s)):
  if s[i] in letters:
    l += 1
  elif s[i] in digits:
    d += 1

print("LETTERS", l)
print("DIGITS", d)

#Exercise 7

A = [["UP", 5],
    ["DOWN", 3],
    ["LEFT", 5],
    ["RIGHT", 2]]
horizontal = 0
vertical = 0

for i in range(0, len(A)):
  if A[i][0] == 'UP':
    vertical += int(A[i][1])
  elif A[i][0] == 'DOWN':
    vertical -= int(A[i][1])
  elif A[i][0] == 'LEFT':
    horizontal -= int(A[i][1])
  elif A[i][0] == 'RIGHT':
    horizontal += int(A[i][1])

distance = (horizontal**2 + vertical**2)**0.5

print('Euclidean Distance is ',  int(round(distance, 0)))

#Exercise 8

nums=[1, 2, 3, 4, 5, 6, 9, 12, 1, 23, -3, 5, 6, 7]
newnums = []
total = 0

for i in range(len(nums)):
  if int(nums[i])>0:
    newnums.append(nums[i])

for i in range(len(newnums)):
  total += int(newnums[i])

average = total/len(newnums)

print('Average of positive integers: ', average)

#Exercise 9

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

if len(b) > len(a):
  for i in range(len(a)):
    if a[i] in b and a[i] not in c:
      c.append(a[i])

print(c)

#Exercise 10

a = ["A+","A","F","g","a-","b"]
grades = {"A+":4.0,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.7,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0,"F":0}
b = []

print(grades.keys())

for i in range(len(a)):
  if a[i].upper() in grades.keys():
    b.append(grades[str(a[i].upper())])
  else:
    b.append("invalid")

print(b)
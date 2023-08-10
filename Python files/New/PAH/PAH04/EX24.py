#message = 'This number is '
#a = 'a multiple of 3.\n'
#b = 'not a multiple of 3.\n'

message = '' #change ' ' around a and b and delete this line and de-coment above for elaborate solution.
for number in range(10):
  if (number % 3) == 0:
    message += 'a'
  else: 
    message += 'b'
print(message)



# 1
pressure = 71.9
if pressure > 50.0:
    pressure = 25.0
elif pressure <= 50.0:
    pressure = 0.0
print(pressure)

#2 
if 5 > 10:
    print("fan")
elif 8 != 9:
    print("glass")
else:
    print("cream")

#3
a = int(input("nr.: "))

if a<0:
    print("negative")
elif a==0:
    print("zero")
else:
    print("positive")

#5
mass = 3.54
if mass > 3.0:
    print(mass, 'is large')
mass = 2.07
if mass > 3.0:
    print (mass, 'is large')

#6
grade = 85
if grade >= 70:
    print('grade is C')
elif grade >= 80:
    print('grade is B')
elif grade >= 90:
    print('grade is A')
#7
if 2 == 2:
print("ice cream is tasty!")

#8
if "cat" == "dog":
    print("prrrr")
else:
    print("ruff")

#9
name = "maria"
if name == "melissa":
    print("usa")
elif name == "mary":
    print("ireland")
else:
    print("colombia")

#10
hair_color = "blue"
if 3 > 2:
    if hair_color == "black":
        print("You rock!")
else:
    print("Boring")

#11
if True:
    print(101)
else:
    print(202)

#12
if False:
    print("Nissan")
elif True:
    print("Ford")
elif True:
    print("BMW")
else:
    print("Audi")

#13
if 1:
    print("1 is truthy!")
else:
    print("???")

#14
if 0:
    print("huh?")
else:
    print("0 is falsy!")

#15
b = input("Enter two numbers here: ").split()
b, c = [str(b), int(c)]

C4_freq = 261.63
D4_freq = 293.66
E4_freq = 329.63
F4_freq = 349.23
G4_freq = 392.00
A4_freq = 440.00
B4_freq = 493.88

name = input("Enter the two character note name, such as C4: ")

note = name[0]
octave = int(name[1])

#continue...

#16

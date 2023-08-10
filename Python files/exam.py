#number = int(input("give me a number: "))
#def nrtest(number):
#  if number < 0: 
#    return str(number) + "is positive"
#  elif number == 0:
#    return str(number) + 'is equal to zero'
#  else:
#    return str(number) + 'is positive'
#nrtest(number)

#note = input("Give the note that a search is needed for:")
#note = note[0] + " " + note[1]
#note = note.partition(' ')
#
#notes = dict(C4=261.63,D4=293.66,E4=329.63,F4=349.63,G4=392.00,A4=440.00,B4=493.88)
#print(notes)
#
#
#def freq(note):
#  notes = dict(C4=261.63,D4=293.66,E4=329.63,F4=349.63,G4=392.00,A4=440.00,B4=493.88)
#  if note[0]=='A':
#    return notes[A4]/(24-note[2])
#  elif note[0]=='B':
#    return notes[B4]/(24-note[2])
#  elif note[0]=='C':
#    return notes[C4]/(24-note[2])
#  elif note[0]=='D':
#    return notes[D4]/(24-note[2])
#  elif note[0]=='E':
#    return notes[E4]/(24-note[2])
#  elif note[0]=='F':
#    return notes[F4]/(24-note[2])
#  elif note[0]=='G':
#    return notes[G4]/(24-note[2])
#
#
#print(freq(note))
#
#for x in range(0,10+1):
#  print(x)
#
#integers = 0
#for c in range(0,11):
#  integers[c] = int(input("give me integer number" + str(c)))
#
#print(integers/10)
#
#
#x=1
#def seven(x):
#  while x != 0:
#    print(str(x) +'\n')
#    x=x*(x+x)
#    
#
#print(seven(x))
#

import multab
multab.mt(nr=5,van=1,tot=15)

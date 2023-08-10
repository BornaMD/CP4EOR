# abc formula
a = float
b = float
c = float
import math
def ABC_formula(formula):
    formula = str(input("Please provide a formula of the form: ax**2+bx+c \n"))
    forms = list
    for i in range(len(formula)):
        forms[i] = formula.lower().split()
    for i in range(len(forms)):
        while i !='x':
            a = int(forms[:i])
            continue
        if i == 'x':
            b = int(forms[forms['a']+1:i+1])
            continue
    forms_rev = forms.reverse()
    for j in range(forms_rev):
        if i == '+':
            c = int(forms[:i])
            continue

    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    print(str(x1) + '\n' + str(x2))

## OOP version
class ABC:
    def __init__(self, formula):
        self.formula == formula
    def collector(self,formula):
        formula = str(input("Please provide a formula of the form: ax**2+bx+c \n"))
    def disbander(self,formula):




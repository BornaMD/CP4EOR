import random
from copy import deepcopy
import numpy as np


# try to test for the first GM assumption

def SLR1(listofparameters, listofconnectors, error=0):
    listofparameters = list # list(input("Please provide a comma separated list of the parameters in floats "))
    #listofparameters[:] = float
    listofconnectors = list # list(input("Please provide a list of connectors in strings "))
    #listofconnectors[:] = str
    f = 0
    for i in listofconnectors:
        if i == 'plus' or '+' or 'Plus' or 'PLUS':
            f += 1
            continue
        else:
            raise Exception('all of the connectors of your system need to be summations')
    if f == len(listofconnectors): return 'OLS assumption 1 has been satisfied. '


SLR1([45,45,56,4.42], ['+', '+', '+', '+'])
# try to test for the 2nd GM assumptions
def SLR2(pop, k, listofparameters):
    pop = list #list(input('Please provide a list of the population data'))
    #pop[:] = float
    k = len(listofparameters)
    if listofparameters[:] == random.sample(population=pop, k=k):
        return "OLS assumption 2 has been satisfied. "
    else: raise Exception("The second OLS assumption has not been satisfied")

# try to test for the first 2 GM assumptions

def SLR1_2(SLR1, SLR2):
    listofconnectors = deepcopy(SLR1.listofconnectors)
    listofparameters = deepcopy(SLR1.listofparameters)

    if (SLR1 & SLR2):
        for i in len(listofconnectors):
            return str(listofparameters[i]) + " " + str(listofconnectors[i]) + ' '
    else: raise Exception('system does not satisfy SLR1 and SLR2. ')


# try to test for the first 4 GM assumptions plus return 'under SLR1 to SLR4'

def SLR4:
    if np.mean(error) ==



# try to test for the first 5 GM assumptions plus return whether or not OLS is BLUE

# put this into OOP

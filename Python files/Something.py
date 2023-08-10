from scipy import optimize,arange
from numpy import array
import matplotlib.pyplot as plt

def production_function(K,L,gamma):
    return (alpha * K**gamma + (1-alpha) * L**gamma)**(1/gamma)

alpha = 0.25
beta = 0.1
K = 1


def labour_demand(gamma,real_wage):
    labour =  optimize.fminbound(lambda l: -(production_function(K,l,gamma)-real_wage*l),0,100,full_output=1)
    return labour[0]

def labour_supply(real_wage, real_price, beta):
    labour_supply = (real_wage/real_price)**beta
    return labour_supply

gamma = -10

range_realwage = arange(0.01,1.0,0.01)
range_demand = arange(0.01,1.0,0.01)
range_supply = arange(0.01,1.0,0.01)

plt.xlabel("$L$", fontsize=15)
plt.ylabel("$W/P$", fontsize=15)
plt.title('Labour demand and labour supply as a function of real wage')
plt.plot(range_realwage, [labour_demand(y)for y in range_demand], c='r') 
plt.plot(range_realwage, [labour_supply(y)for y in range_supply], c='g')


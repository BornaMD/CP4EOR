import math
def simplify (c1,c2):
    """ This function gets the numerator and denominator as inputs, 
    then simplifies them by dividing them by their greatest common devisor.
    It returns the simplified numerator and deniminator.
    if c2 is zero, it returns an Exception saying "c2 cannot be zero" 
    """
    #create a runtime error
    if c2==0:
        raise Exception("c2 cannot be zero")
    # calculate gcd
    x=math.gcd (c1,c2)
    #divide by gcd
    c1 //= x
    c2 //= x
    return c1,c2

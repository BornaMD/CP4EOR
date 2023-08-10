def f(n):
    if n == 1:
        return 3
    elif n >1: 
        return f(n -1) + 3
    elif n <1: 
        raise Exception


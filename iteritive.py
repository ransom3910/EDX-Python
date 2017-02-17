def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp < 1 :
        return 1

    else:
        return base * iterPower(base,exp -1 )



print(str(iterPower(2,8)))






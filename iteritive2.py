def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

    n=1.0
    for x in range(0,exp):
      n= n*base
    return n

print(str(iterPower(5.85,0)))


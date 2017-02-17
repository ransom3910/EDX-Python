def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here

    if a <= b:
        result = a
        while ( (b % result or a % result) and result >= 1):
            result -= 1

    else:
        result = b
        while ((b % result or a % result) and result >= 1):
            result -= 1

    return result







gcdIter(9,12)

#
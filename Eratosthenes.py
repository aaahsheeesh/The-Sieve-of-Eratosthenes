import math
def prime_generator( limit ):

    ls = [True] * limit
    for i in range(2, int(math.sqrt(limit)) + 1): 
        for j in range(i*2, limit, i):
            ls[j] = False
    print( "We  have ", ls.count(True) - 2, " prime numbers." )
    print( [i for i in range(2, limit) if ls[i]])

#  test run
#  prime_generator(100)

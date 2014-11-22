#The following iterative sequence is defined for the set of positive integers:

#n -> n/2 (n is even)
#n -> 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:

#13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
#Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.

# remember if we are testing x and 3x+1 =< 1 000 000 then 
# we do not have to test 3x+1 as a candidate since x has chain one longer than the
# 3x+1 chain

# remember if we are testing x and x/2 is an int and =< 1 000 000 then 
# we do not have to test x/2 since x has chain one longer than the x/2 chain
# this means that testing will begin from 500001

test = []

no_test=[]

def sieve_list():
    for cand in range(500001,1000001):
        if (cand-1)%3 != 0:
            test.append(cand)
            
def collatz_recursion(n,length):
    if n == 1:
        return length
    if n%2==0:
        if (n//2>500000) and (1000000>n//2):
            no_test.append(n//2)
        return collatz_recursion(n//2,length+1)
    else:
        if ((3*n+1)>500000) and (1000000>(3*n+1)):
            no_test.append(3*n+1)
        return collatz_recursion(3*n+1,length+1)

def collatz_finder():
    sieve_list()
    m_len = 0
    num = 1
    for cand in test:
        if cand not in no_test:
            if m_len < collatz_recursion(cand,0):
                num = cand
    return num
    
    
# Sieve of Eratosthenes
#  
#  My implementation of the ancient prime sieve in order to find the nth prime 

# Using the asymptotic law of distribution of prime numbers, the nth prime number p_n
#  p_n ~ n*ln(n)

import math

list_of_primes = []

# sieve finds the num th prime number, start is the prime number to start the search from, multiply_bound
#  is a upperbound multiplier 

def sieve(start,num,multiply_bound):
    
    # Sets up an upper bound to look for the nth prime in and the initial list of primes
    #  cannot include 1 as anything is divisible by 1 !
    upper_bound = int((n+1) * math.log(n) * multiply_bound)
    
    # This loops works since the prime factorization pieces of a composite number are always
    #  smaller than the number itself
    for prime_candidate in range(start,upper_bound):
        
        # sets up a truth value and if the prime_candidate is divisible by any prime
        #  the truth value is set to false and the loop is broken out of
        t_val = 0
        for prime in list_of_primes:
            if prime_candidate%prime == 0:
                t_val = 1
            if t_val == 1:
                break
        
        # If the truth value is true, this means that the prime_candidate is a prime
        #  and we can append the truth_candidate to the list of prime
        if t_val == 0:
            list_of_primes.append(prime_candidate)
    
    # If in the case, the nth prime number was not found, increase the upper bound by 20%
    #  and start the process again from the end of the list_of_primes
    if len(list_of_primes) != num:
        return sieve(list_of_primes(len(list_of_primes)),num-len(list_of_primes),1.2*multiply_bound)
    
    return list_of_primes(len(list_of_primes))
    
    
    
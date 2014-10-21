# Question 10 revamp

# Utilising the idea of the Sieve of Eratosthenes, we can construct a highly 
#  efficient implementation of question 10

# In this implementation we are only required to find primes up to sqrt(2000000)
#  and to use subtraction

import math

list_of_primes=[2]

def findp():
    
    upper_bound = int(math.sqrt(2000000))
    
    for prime_candidate in range(3,upper_bound):
        v_true=0
        for prime in list_of_primes:
            if prime > math.sqrt(prime_candidate):
                break
            if prime_candidate%prime==0:
                v_true = 1
                break
            
        if v_true == 0:
            list_of_primes.append(prime_candidate)
    return len(list_of_primes)

findp()

initial_sum = 2000001000000

def find_sum_repeater(current_number):
    summ = 0
    for prime in list_of_primes:
        if current_number * prime <= 2000000:
            summ += 1
            initial_sum -= current_number*prime
            summ += find_sum_repeater(current_number*prime)
    return summ

def f():
    
    summ = find_sum_repeater(1)
    return "iterations:"+str(summ) + "-answer-" + initial_sum
            
    
    
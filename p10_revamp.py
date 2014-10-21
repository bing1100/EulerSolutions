# Question 10 revamp

# Utilising the idea of the Sieve of Eratosthenes

# In this implementation we are only required to find primes up to sqrt(2000000)
#  and to use subtraction

import math

list_of_primes=[2]


initial_sum= 2000001000000

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

def base_repeater(base_num,index):
    global initial_sum
    num = 0
    if index < len(list_of_primes):
        for exponent in range(20):  
            num += 1        
            prime = list_of_primes[index]
            current = base_num * (prime**exponent)
            if current > 2000000:
                break
            initial_sum -= current
            num += base_repeater(current,index+1)
    return num
    

# For a basic composite number it must be the multiplication of 2 prime numbers
        # Case 1 : The base case is a square of a prime
        # Case 2 : The base case is multiplication of 2 seperate prime numbers
def f():
    findp()
    summ = 0
    for index_p1 in range(len(list_of_primes)):
        for index_p2 in range(index_p1,len(list_of_primes)):
            prime_base = list_of_primes[index_p1] * list_of_primes[index_p2]
            summ += base_repeater(prime_base,0)
    return "iterations:"+str(summ) + "-answer-" + str(initial_sum) 
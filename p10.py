#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.

# Lets borrow question 7 solution to solve this problem!

# Question 7 Solution

#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

#What is the 10 001st prime number?

import math

list_of_primes = [2]

# sieve finds the num th prime number, start is the prime number to start the search from, multiply_bound
#  is a upperbound multiplier 
def sieve(start,num,multiply_bound):
    
    # Sets the counter as n
    n = num
    
    # Sets up an upper bound to look for the nth prime
    upper_bound = int((num+1) * math.log(num) * multiply_bound)
    
    # This loops works since the prime factorization pieces of a composite number are always
    #  smaller than the number itself

    for prime_candidate in range(start,upper_bound):
            
        # sets up a truth value and if the prime_candidate is divisible by any prime
        #  the truth value is set to false and the loop is broken out of
        t_val = 0       
        for prime in list_of_primes :
            if prime>math.ceil(math.sqrt(prime_candidate)):
                break
            if prime_candidate%prime == 0:
                t_val = 1
            if t_val == 1:
                break
        
        # If the truth value is true, this means that the prime_candidate is a prime
        #  and we can append the truth_candidate to the list of prime
        #  decrease n by 1 
        if t_val == 0:
            n -= 1
            #print(str(n) + ":appended " + str(prime_candidate))
            list_of_primes.append(prime_candidate)
        
        # If n is 0, that means the (n+1)th prime has been reached and returns 
        #  the nth prime
        if n==0:
            #print(list_of_primes)
            return list_of_primes[len(list_of_primes)-2]
            
    # If in the case, the nth prime number was not found, increase the upper bound by 20%
    #  and start the process again from the end of the list_of_primes
    #print("need reset")
    return sieve(list_of_primes[len(list_of_primes)-1],n,multiply_bound*1.2)

#print(sieve(2,150000,1))

# Create list of primes
sieve(2,148934,1)

# addes the sum
def summation():
    
    # Sets starting sum
    sum1 = 0 
    
    # Loops list_of_primes for primes < 2000 000, adds to sum
    for num in list_of_primes:
        sum1 += num 
    
    # return the sum 
    return sum1 - 142913828922

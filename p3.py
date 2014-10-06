import itertools

def PrimeFactors(num):
    for i in range(num//2):
        divisor = num//2 - i 
        if (num%divisor==0):
            return PrimeFactors(divisor)
        elif (divisor==2):
            return num   
        
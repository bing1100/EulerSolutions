import itertools

def PrimeFactors(num):
    for i in itertools.count(num/2):
        print(i)
        divisor = num/2 - i 
        if (num%divisor==0):
            return divisor
        elif (divisor==2):
            return "Cool, it is a prime"   
        
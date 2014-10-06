import math

# Find the largest prime factor of num 
# Only Takes ODD numbers

def f(num):
    
    if (int(math.sqrt(num))%2==0):
        start=1
    else:
        start=0
        
    for i in range(start,int(math.sqrt(num)),2):
        
        divisor = int(math.sqrt(num)) - i 
        
        if (divisor==1):
            return num           
        elif (num%divisor==0):
            return max(f(divisor),f(num/divisor))
    
print(f(600851475143))     
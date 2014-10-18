#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# a and b are smaller than 333

#  Lets solve this problem in an efficient Log method

import math

def find():
    for a_m in range(333):
        
        true_value=0
        
        a = 333 - a_m
        
        lower_bound = 0
        
        upper_bound = a
        
       
        while(true_value==0):
            
            b = (lower_bound + upper_bound)//2
            
            c_2 = b*b + a*a
            c = math.sqrt(c_2)
            
            
            if c+b+a==1000:
                true_value =2
            elif upper_bound - lower_bound < 3:
                true_value == 1
            elif c + b + a > 1000:
                upper_bound = b
            else:
                lower_bound = b
                    
        if true_value == 2:
            break
        
    if true_value == 2:
        return 500000*c - 1000*c*c
    
    return "Woah something spooky"
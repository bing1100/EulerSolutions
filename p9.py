#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

#a^2 + b^2 = c^2
#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# a and b are smaller than 333

#  Lets solve this problem in an efficient Log method (solves in 1345 iterations)

import math

def find():
    for a_m in range(499):
        
        # Sets three functional values for the function
        #  true_value = 0 - continue looping current thread
        #  true_value = 1 - move to next thread
        true_value=0
        
        # Sets a value for a
        a = 499 - a_m
        
        # Sets the upper and lower bound for b
        lower_bound = 0
        upper_bound = 499-a_m
        
        # Loops while the true_value = 0 on current thread
        while(true_value==0):
            
            # Sets b at the midpoint between lower_bound and upper_bound
            b = (lower_bound + upper_bound)//2
            
            # Computes c value 
            c_2 = b*b + a*a
            c = math.sqrt(c_2)
            
            # Debuging print string
            #print(str(lower_bound)+"-"+str(upper_bound)+"\n-b-"+str(b)+"\n-c-"+str(c)+"\n-sum-"+str(c+b+a))
            
            # If c+b+a == 1000 that means we have the right combination and we will return a*b*c
            if (c+b+a)==1000:
                return 500000*c - 1000*c*c
            
            # If there upperbound - lowerbound == 1 
            elif (upper_bound - lower_bound) < 2:
                
                # In this case, b=lower_bound was tested but never b=upper_bound, so we have to test the latter
                b = upper_bound
                c_2 = b*b + a*a
                c = math.sqrt(c_2)
                
                # Debuging print string
                #print(str(lower_bound)+"-"+str(upper_bound)+"\n-b-"+str(b)+"\n-c-"+str(c)+"\n-sum-"+str(c+b+a))
                
                # If c+b+a == 1000 that means we have the right combination and we will return a*b*c
                if (c+b+a)==1000:
                    return 500000*c - 1000*c*c
                
                # If b=upper_bound is not the value we want, we break out of the thread    
                true_value = 1
            
<<<<<<< HEAD
            if c+b+a==1000:
                true_value = 2
            elif (upper_bound - lower_bound) < 2:
                true_value = 1
=======
            # if (c + b + a) > 1000, we choose the lower half of upper_bound and lower_bound with b value in the middle
>>>>>>> origin/master
            elif (c + b + a) > 1000:
                upper_bound = b
            
            # if (c + b + a) < 1000, we choose the upper half of the upper_bound and lower_bound with b value in the middle
            else:
                lower_bound = b
<<<<<<< HEAD
            
            print(str(lower_bound)+"-"+str(upper_bound) + "-" + str(c+b+a))
                    
        if true_value == 2:
            break
        
    if true_value == 2:
        return 500000*c - 1000*c*c
=======
>>>>>>> origin/master
    
    # If we do not find the right answer in all the combinations
    return "Woah something spooky"
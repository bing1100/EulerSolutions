#The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

#1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

#Let us list the factors of the first seven triangle numbers:

 #1: 1
 #3: 1,3
 #6: 1,2,3,6
#10: 1,2,5,10
#15: 1,3,5,15
#21: 1,3,7,21
#28: 1,2,4,7,14,28
#We can see that 28 is the first triangle number to have over five divisors.

#What is the value of the first triangle number to have over five hundred divisors?

import math

# Generates the nth number in this sequence using summation rules
def generator(nth):
 term = (nth+1)*nth//2
 return term

# finds the number of divisors
def num_divisors():
 
 # Estimates the nth value based on the smallest square of 250 
 current = generator(355)
 
 # sets next nth value
 nth = 356
 
 # Sets num_div = 0
 num_div = 0
 
 # While loop to continue until num_div is bigger than 250
 while(num_div<=250):
  
  # resets num_div to 0
  num_div = 0
  
  # Main for loop that finds the num_div for the nth number in the sequence
  #  only looks for divisors smaller than sqrt(current) due to symmetry
  for potential in range(int(math.sqrt(current))+1):
   potential_divisor = int(math.sqrt(current)) - potential
   
   # Case 1: if all numbers in range(sqrt(current)) is reached, calculate new nth
   #  and return to top of while loop
   if potential_divisor == 0:
    nth += 1
    current = generator(nth)
    break
   
   # Case 2: if potential_divisor is a divisor of current than we add 1 to num_div
   if current%potential_divisor == 0:
    num_div+=1
    
   # Case 3: if num_div is the size we want, stop looking.
   if num_div > 250:
    break
   
 return current
  
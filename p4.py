import math

#find the largest palindrom that is the product of 2 three digit
# numbers

#run f() to find
def f():
    large = 810000
    while(large>10): #while loop to stop execution a certain lower boundary
        for i in range(998):
            firstnum = 999-i
            for j in range(998):
                secondnum = 999-j
                if (firstnum*secondnum<large): #shifts the lower boundary and optimizes search
                    large-=j
                    break
                if (ispalindrome(firstnum*secondnum)==1):
                    print(firstnum)
                    print(secondnum)
                    return firstnum*secondnum
        

#confirms if num is palindrome or not 


def ispalindrome(num):
    nlength=int(math.floor(math.log10(num)))
    
    # This is nessesary due to the fact range(0) is empty and for loop closes
    if (nlength<2):
        halfway = 1
    else: 
        halfway = nlength//2 + 1
        
        
    for i in range(halfway):
        biggerdigit=nlength-i # Is the symmetric larger digit placement
        print( num%(10**(i+1)), "=", num//(10**biggerdigit))
        # Tests for non palindromes for each i moving closer to halfway
        if (num%(10**(i+1)) != num//(10**biggerdigit)):
            return 0
        
    return 1 # if number is not a non palindrome than produce 
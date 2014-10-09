
# Run f(topnum) where topnum is the max number in the range
#  this will produce the LCM of all the numbers in the range

def f(topnum):
    listofmultiply=[1]
    multi=1
    
    # Goes through the whole list and filtering out GCD
    for potential in range(1,topnum):
        
        #Delete the GCD values from the potential number
        for divisor in listofmultiply:
            if (potential%divisor == 0):
                potential=potential//divisor
                
        #Append the potential to the list of multiply         
        listofmultiply.append(potential)
        
    # Computes the final answer
    for j in listofmultiply:
        multi*=j
    print(listofmultiply)    
    return multi
        
                
                
        

# f takes a num and finds the difference between the squares
#  and the sum of squares. 

def f(num):
    sum=0
    
    # need plus one since range(x) creates list from 0 to x-1
    for i in range(num+1):
        for j in range(num+1):
            if i!=j:
                sum+=i*j
    return sum
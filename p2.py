def runme(nthless1,nth,sum):
    nthplus1 = nthless1 + nth
    if (nth%2==0):
        return runme(nth,nthplus1,sum+nth)
    elif (nth > 4000000):
        return sum
    else:
        return runme(nth,nthplus1,sum)

print(runme(1,1,0))
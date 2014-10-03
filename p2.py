def runme(nthless1,nth):
    sum = 0
    nthplus1 = nthless1 + nth
    if nth/2==0:
        sum+=nth
    if nth>4000000:
        return sum
    return runme(nth,nthplus1)

runme(1,1)
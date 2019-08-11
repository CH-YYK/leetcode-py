def maxnumways(n):
    ## maximum 2^(n-1)
    hashtable = {}
    for i in range(2, n+1):
        hashtable[i] = 0
        for k in range(2*i, n+1, i):
            hashtable[i] 

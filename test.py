# T(n) = n*(O(f(n)))
# T(n) = T(n-1) + 1 ------ O(n)
# T(n) = T(n-1) + n-------O(n^2)
# T(n) = t(n-1) +log(n) --O(nlog(n))




def sajib2(n):
    if n<=0 : return
    for i in range(1,n+1): print(i,end= " ")
    print()
    sajib2(n-1)
sajib2(5)


def sajib3(n):
    if n<=0 : return
    i=1
    while(i<n):
        i*=2
    sajib3(n-1)



# T(n) = T(n-1)+ 1  -----(1)
# T(0) =  1  -----(2)

# T(n-1) = T(n-2)+ 1
# T(n-2) = T(n-3)+ 1

# T(n) = T(n-1)+ 1
# = [T(n-2)+ 1] +1 = T(n-2)+2
# = [[T(n-3)+ 1]+ 1] +1
# = T(n-3) + 3
# .
# .
# = T(n-n) + n
# T(n) = 1 + n = O(n)

# n . (n-1). (n-2). (n-3)....3.2.1 = O(n^n)

def sajib(n):
    if n<=0 : return
    print(n, end= " ")
    sajib(n-1)
    return 
# log a + log b = log ab
# log(1) + log(2) + log(3)+ .....+ log(n-1)+ log(n)
# = log(n!)
# = log(n^n)
# = n*log(n)

# T(n) = T(n-1) + logn---(1)
# T(n-1) = T(n-2) + log(n-1) + logn


# = T(n-2) + log(n-1) + logn 
# = T(n-3) + log(n-2) + log(n-1) + logn 
# = T(n-n) + log(n-n) + log(n-(n-1)) + log(n-2) +  log(n-1) + logn 
# = 1 + log(n-n) + log(n-(n-1)) + log(n-2) +  log(n-1) + logn 




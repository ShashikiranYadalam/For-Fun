##import math
##
##
##def josefile(n):
##    a = 0
##    flag = 0
##    while 2**a < n :
##        if 2**a==n:
##            flag = 1
##            exit 
##        a = a + 1
##
##    print (flag)        
##    if flag == 1:
##        return 1
##    
##    p = (n - (2**(a-1)))
##    print(p)
##
##    return 2*p + 1
            
            
import math


def josephus(n):
##    m = int(math.log2(n))
##    l=n-2**m
##    return 2*l+1
    return (2*(n-2**(int(math.log2(n)))) + 1)

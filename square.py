import math
n=1
while n>=0:
    a=n*n
    b=math.sqrt(a+168)
    print(b)
    if  b % 1 == 0:
        print(a)
        break
    else:
        n=n+1
       
        
    

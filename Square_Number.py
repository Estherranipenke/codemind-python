import math
def sqr(n):
    a=int(n**0.5)
    if(a*a==n):
        return True
    else:
        return False
n=int(input())
for i in range(0,n//2):
    if(sqr(i) and sqr(n-i)):
        print(True)
        break
else:
    print(False)
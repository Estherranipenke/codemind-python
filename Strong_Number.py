def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1) 
n=int(input())
v=n
g=[]
s=0
while n>0:
    r=n%10
    g.append(r)
    n=n//10
s12=0
for i in g:
    s12+=factorial(i)
if v==s12:
    print("The number",v, "is a strong number")
else:
    print("The number",v, "is not a strong number")
#print(s12)
    

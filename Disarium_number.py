n=int(input())
l=[]
for i in str(n):
    l.append(int(i))
e=[]
for j in range(1,len(l)+1):
    e.append(j)
z=list(zip(l,e))
c=0
for a,b in z:
    c=c+a**b
if c==n:
    print("True")
else:
    print("False")
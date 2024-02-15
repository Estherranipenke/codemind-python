n=int(input())
a=list(map(int,input().split()))
m=int(input())
m%=n
for i in range(m):
    k=a.pop()
    a.insert(0,k)
print(*a)
    

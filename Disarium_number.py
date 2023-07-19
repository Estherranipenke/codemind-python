n=int(input())
length=len(str(n))
tem=n
sum=0
rem=0
while tem>0:
    rem=tem%10
    sum=sum+int(rem**length)
    tem=tem//10
    length=length-1
if sum==n:
    print("True")
else:
    print("False")
s=input()
sum=0
pro=1
for i in range(len(s)):
    sum=sum+int(s[i])
    pro=pro*int(s[i])
    b=pro-sum
print(b)
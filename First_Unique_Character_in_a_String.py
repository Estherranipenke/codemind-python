n=input()
flag=0
for i in range(len(n)):
    count=0
    for j in range(len(n)):
        if (i!=j):
            if n[i]==n[j]:
                count+=1
    if (count==0):
        flag=1
        print(i)
        break
if (flag==0):
    print("-1")

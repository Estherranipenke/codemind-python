n=int(input())
sq=n*n
rev=str(n)[::-1]
sqq=int(rev)*int(rev)
a=str(sqq)[::-1]
if int(a)==sq:
    print("True")
else:
    print("False")

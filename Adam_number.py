n=int(input())
sqrt=n*n
rev=str(n)[::-1]
sqq=int(rev)*int(rev)
a=str(sqq)[::-1]
if int(a)==sqrt:
    print("True")
else:
    print("False")
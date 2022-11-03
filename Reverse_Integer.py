n=int(input())
a=0
if n<0:
    n=-(n)
    a=1
else:
    n=n
rev=0
while n>0:
    b=n%10
    rev=rev*10+b
    n=n//10
if a==1:
    print(-(rev))
else:
    print(rev)
    
a=int(input())
b=a**2
rev=0
c=0
while b>0:
    r=b%10
    rev=rev*10+r
    b=b//10
    c+=r
if c==a:
    print("Neon Number")
else:
    print("Not Neon Number")
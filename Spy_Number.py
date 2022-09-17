n=int(input())
s=0
p=1
for i in range(n):
    if n>0:
        r=n%10
        s+=r
        p*=r
        n=n//10
if s==p:
    print("Spy Number")
else:
    print("Not Spy Number")
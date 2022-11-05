a=int(input())
b=int(input())
s=0
r=0
for i in range(1,a):
    if a%i==0:
        s+=i
for j in range(1,b):
    if b%i==0:
        r+=i
if s==b or r==a:
    print("Amicable")
else:
    print("Not Amicable")
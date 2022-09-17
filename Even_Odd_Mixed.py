n=int(input())
s=0
c=0
c1=0
for i in str(n):
    a=int(i)
    c1+=1
    if a%2==0:
        s+=1
    if a%2!=0:
        c+=1
if s>=1 and c>=1:
    print("Mixed")
elif s==c1:
    print("Even")
else:
    print("Odd")
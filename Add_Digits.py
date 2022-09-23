n=int(input())
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
    if s>9 and n==0:
        n=s
        s=0
print(s)
        
    
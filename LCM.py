a,b=map(int,input().split())
n=a
m=b
while a!=0 and b!=0:
    if a>b:
        a=a%b
    else:
        b=b%a
x=max(a,b)
print(n*m//x)
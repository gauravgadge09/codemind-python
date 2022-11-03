t=int(input())
for i in range(t):
    n=int(input())
    a=n
    rev=0
    for j in range(n):
        if n>0:
            r=n%10
            rev=rev*10+r
            n=n//10
    if a==rev:
        print("True")
    else:
        print("False")
n=int(input())
rev=0
for i in range(n):
    if n>0:
        r=n%10
        rev=(rev*10)+r
        n=n//10
print(rev)
n=int(input())
lst=list(map(int,input().split()))
a=len(lst)
s=0
for i in lst:
    s+=i
b=s/a
print("{0:.2f}".format(b))
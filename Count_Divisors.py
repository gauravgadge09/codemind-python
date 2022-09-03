i,r,k=map(int,input().split())
s=0
for j in range(i,r+1):
    if j%k==0:
        #print(j,end=' ')
        s+=1
print(s)
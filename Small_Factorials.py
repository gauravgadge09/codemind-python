n=int(input())
for i in range(n):
    t=int(input())
    fact=1
    for j in range(1,t+1):
        fact=fact*j
    print(fact)
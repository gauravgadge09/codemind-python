t=int(input())
for i in range(1,t+1):
    n=int(input())

    a=n
    while True:
        is_prime=True
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        else:
            a+=1
    #print(a)
    b=n
    while True:
        is_prime=True
        for i in range(2,int(a**0.5)+1):
            if b%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        else:
            b-=1
    #print(b)
    if a-n<n-b:
        print(a)
    else:
        print(b)
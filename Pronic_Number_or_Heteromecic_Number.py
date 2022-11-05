a=int(input())
for i in range(1,a//3):
    b=i+1
    if b*i==a:
        print("YES")
        break
else:
    print("NO")
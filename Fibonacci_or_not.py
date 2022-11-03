num=int(input())
n1, n2 = 0, 1
while True:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    if n3>=num:
        break
if num == n3:
       print("True")
else:
       print("False")

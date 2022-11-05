a=int(input())
b=a**2
a=str(a)
b=str(b)
l=len(a)
d=b[-l:]
if (int(d)==int(a)):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
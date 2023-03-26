L=(int(l) for l in input("enter the numbers:").split(","))
a=list(L)
a1=int(input("enter the value1:"))
a2=int(input("enter the value2:"))
z=a[a1]
a[a1]=a[a2]
a[a2]=z
print(a)
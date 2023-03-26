z=int(input("Enter the armstrong no:"))
n=z
a=n%10
d=n//10
b=d%10
e=d//10
c=e%10
print(a,b,c,d,e)

if a**3+b**3+c**3==z:
    print("Yes")
else:
    print("no")
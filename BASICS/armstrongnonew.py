z=int(input("Enter the armstrong no:"))
if z<1:
    print("invalid")
n=z
sum1=0
l=len(str(z))
while n!=0:
    a=n%10
    sum1=sum1+(a**l)
    n//=10
if sum1==z:
    print("yes")
else:
    print("no")
    

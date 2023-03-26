import array as arr 
ch=input("Enter the type of the values you want (i,s,f):")
if ch=='i':
    a=arr.array('i',[int(l) for l in input("Enter the nos:").split(",")])
elif ch=='s':
    a=arr.array('c',[str(l) for l in input("Enter the values:").split(",")])
elif ch=='f':
    a=arr.array('f',[float(l) for l in input("Enter the nos:").split(",")])
d=int(input("enter from where the values to be rotated:"))
l=len(a)
for i in range(d):
    temp=a[0]
    for j in range(l-1):
        a[j]=a[j+1]
    a[l-1]=temp
    
print(a)

    

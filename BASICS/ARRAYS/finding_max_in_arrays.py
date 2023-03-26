import array as arr
a=arr.array('i',[int(l) for l in input("enter the nos:").split(",")])
max1=a[0]
L=len(a)
for i in range(1,L):
    if a[i]>max1:
        max1=a[i]
print(max1)
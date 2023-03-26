import array as arr 
a=arr.array('i',[int(l) for l in input("enter the values:").split(",")])
mul=1
z=int(input("enter the number with which you want to divide and find remaider:"))
for j in a:
    mul*=j
q=mul%z
print(q)
    
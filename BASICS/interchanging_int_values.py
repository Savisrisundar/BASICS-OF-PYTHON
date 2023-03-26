l=list(int(num) for num in input("enter the numbers separated by spaces:").split(" "))
L=len(l)
a=l[0]
l[0]=l[L-1]
l[L-1]=a
print(l)
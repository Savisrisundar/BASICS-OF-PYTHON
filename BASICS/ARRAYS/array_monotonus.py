import array as arr 
a=arr.array('i',[int(l) for l in input("enter the values:").split(",")])
if all(a[i]<=a[i+1] for i in range(len(a)-1)) or all(a[i]>=a[i+1] for i in range(len(a)-1)):
    print("monotonus")
else:
    print("not monotonus")
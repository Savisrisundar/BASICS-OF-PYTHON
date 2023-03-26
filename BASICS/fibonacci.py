n=int(input("Enter the number of terms ="))
a=0
b=1
if n==1:
    print("0")
elif n<0:
    print("please give positive numbers!!!")
else:
    while n>0:
        print(a)
        c=a+b
        a=b
        b=c
        n=n-1
    
    

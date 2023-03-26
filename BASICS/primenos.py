n1=int(input("Enter the starting of the interval="))
n2=int(input("Enter the end of the interval="))
for i in range(n1,n2+1):
    for j in range(2,i):
        if i%j==0:
            print(i,"is not prime")
            break
    else:
        print(i,"is prime")
        
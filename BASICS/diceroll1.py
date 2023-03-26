num=int(input())
a1=0
a2=0
a3=0
a4=0
a5=0
a6=0
while num!=0:
    sums=num%10
    if (sums!=1 and sums!=2 and sums!=3 and sums!=4 and sums!=5 and sums!=6):
        print("-1")
        break
    elif sums=="1":
        a1+=1
    elif sums=="2":
        a2+=1
    elif sums=="3":
        a3+=1
    elif sums=="4":
        a4+=1
    elif sums=="5":
        a5+=1
    elif sums=="6":
        a6+=1
    else:
        continue
    num//=10
else:
    if a1>=a2 and a1>=a3 and a1>=a4 and a1>=a5 and a1>=a6:
        print("1")
    elif a2>=a1 and a2>=a3 and a2>=a4 and a2>=a5 and a2>=a6:
        print("2")
    elif a3>=a1 and a3>=a2 and a3>=a4 and a1>=a5 and a1>=a6:
        print("3")
    elif a4>=a1 and a4>=a2 and a4>=a3 and a4>=a5 and a1>=a6:
        print("4")
    elif a5>=a1 and a5>=a2 and a5>=a3 and a5>=a4 and a5>=a6:
        print("5")
    elif a6>=a1 and a6>=a2 and a6>=a3 and a6>=a4 and a6>=a5:
        print("6")
a=input()
L=list(a)
l=[int(i) for i in L]
b=[]
c=[]
for i in l:
    if i>6:
        print("-1")
        exit()
    if l.count(i)>1:
        b.append([l.count(i)])
        c.append(i)
z=max(b)
y=b.index(z)
print(c[y])
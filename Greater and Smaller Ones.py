#Greater and Smaller Ones
n=int(input("Size: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
el=int(input("Enter tht element: "))
def print_smallarge(a,el):
    aa=[]
    b=[]
    for i in range(len(a)):
        if el<a[i]:
            aa.append(a[i])
        elif el>a[i]:
            b.append(a[i])
    if len(aa)!=0:
        aa.insert(0,el)
        for i in range(len(aa)):
            print(aa[i],end=' ')
    else:
        print(-1)
    print()
    if len(b)!=0:
        b.insert(0,el)
        for i in range(len(b)):
            print(b[i],end=' ')
    else:
        print(-1)
ans=print_smallarge(a,el)
        

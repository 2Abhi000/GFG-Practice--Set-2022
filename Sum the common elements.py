#Sum the common elements
n=int(input("Size of array1: "))
n1=int(input("Size of array2: "))
a=[]
b=[]
for i in range(n):
    a.append(int(input("Value of array1: ")))
for i in range(n1):
    b.append(int(input("Value of array2: ")))
def sum_common(ar,br):
    s=set(ar)
    s2=set(br)
    ans=s.intersection(s2)
    if ans:
        print(sum(list(ans)))
    else:
        print(0)
ans=sum_common(a,b)

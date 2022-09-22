#Set Operations
n=int(input("Size: "))
x=int(input("Element: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
def ma(arr,x):
    s=set()
    for i in range(len(a)):
        if a[i] not in s:
            s.add(a[i])
    for i in s:
        print(i,end=' ')
    print()
    if x in s:
        s.remove(x)
        print('erased ',x)
    else:
        print('not found')
    for i in s:
        print(i,end=' ')
ans=ma(a,x)

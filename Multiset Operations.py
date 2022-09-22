#Multiset Operations
n=int(input("Size: "))
x=int(input("Element: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
def ma(arr,x):
    arr.sort()
    for i in range(len(arr)):
        print(arr[i],end=' ')
    print()
    if x in arr:
        c=arr.count(x)
    else:
        print('not found')
    for i in range(c):
        arr.remove(x)
    print('erased ',x)
    for i in range(len(arr)):
        print(arr[i],end=' ')
ans=ma(a,x)

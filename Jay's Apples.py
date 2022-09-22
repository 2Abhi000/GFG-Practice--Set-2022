#Jay's Apple
n=int(input("Size: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
def apples(ar):
    a=list(set(ar))
    if len(a)!=0:
        print(len(a))
ans=apples(a)

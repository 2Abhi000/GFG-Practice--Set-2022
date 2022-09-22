#Pair Sum Existence
n=int(input("Size: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
s=int(input("Enter the sum to find: "))
def find_sum(arr,s):
    t=0
    for i in range(len(arr)):
        c=0
        for j in range(len(arr)):
            if arr[i]+arr[j]==s:
                t=1
                break
            else:
                t=0
    if t:
        print(1)
    else:
        print(0)
ans=find_sum(a,s)

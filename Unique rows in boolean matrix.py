#Unique rows in boolean matrix
row=int(input("Enter the row: "))
col=int(input("Enter the col: "))
a=[[int(input("Enter the value: ")) for i in range(row)] for j in range(col)]
for i in a:
    x = a.pop(0)
    if x not in a:
        a.append(x)
    else:
        del x
print(a)

rows=int(input())
columns=int(input())
flag=0
list1=[]
for i in range(rows):
    z=[int(i) for i in input().split()]
    list1.append(z)
target=int(input())
for i in range(rows):
    for j in range(columns):
        if(list1[i][j]==target):
            print("true")
            flag=1
            break
if(flag==0):
    print("false")
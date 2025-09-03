s=input("enter a string")
rev=""
res=[]
for i in s:
    if i!=" ":
        rev+=i
    else:
        res.append(rev)
        rev=""
res.append(rev)
for i in range(len(res)-1,-1,-1):
    n=res[i]
    print(n[::-1],end=" ")



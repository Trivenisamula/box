str1="aabccca"
res=""
for i in range(len(str1)-1,-1,-1):
    c=1
    if str1[i]!=str1[i-1]:
        res+=str1[i]+str(c)
print(res)


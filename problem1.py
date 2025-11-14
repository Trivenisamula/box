# n=int(input("enter a number"))
# sn=n*n
# print(sn)
# sum=0
# while sn>0:
#     r=sn%10
#     sum=sum+r
#     sn=sn//10
# if sum==n:
#     print("neon number")
# else:
#     print("not a neon number")
# n=4
# for i in range(0,n):
#     for j in range(0,n):
#         print("*",end=" ")
#     print()
# n=int(input("enter a range"))
# m=int(input("enter a range"))
# for i in range(n,m+1):
#     print(i)
# n=int(input("enter"))
# for i in range(n,0,-1):
#     print(i)
# n=int(input("enter a range"))
# m=int(input("enter a range"))
# for i in range(m,n-1,-1):
#     print(i)
# n=int(input("enter a range"))
# s=0
# for i in range(1,n+1):
#     s+=i
# print(s)
# n=int(input("enter a range"))
# f=1
# for i in range(1,n+1):
#     f*=i
# print(f)
#factors of a number
# n=6
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)
# n=6
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# print(c)
# n=int(input("enter a range"))
# c=0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
# if c==2:
#     print("prime")
# else:
#     print("not a prime")
# for i in range(2,101,2):
#     print(i)
# ev=0
# od=0
# for i in range(1,101):
#     if i%2!=0:
#        od+=i
#     else:
#         ev+=i
# print(ev)
# print(od)
# n=123456
# s=0
# while n>0:
#     r=n%10
#     s+=r
#     n=n//10
# print(s)
# 
# n=100
# for i in range(1,n+1):
#     if 1<=i<=10 or 21<=i<=30 or 41<=i<=50:
#         print(i,end=" ")
# greet()
# def greet():
#     print("hello")
# a=10,b=20
# def outer():
#     c=30,d=40
# global c
# print(c)
# i=1
# n=4
# while i<=n:
#     print("* "*n*2)
#     i+=1
# i=1
# n=4
# while i<=n:
#     print(" "*,"*"*i)
#     i+=1
# i=5
# n=5
# while n>=i:
#     print((n-i)*" ","* "*i)
#     i-=1
# i=1
# n=5
# while i<=n:
#     print("* "*n)
#     i+=1
# i=1
# n=5
# while i<=n:
#     if i==1 or i==n:
#         print("* "*n*2)
#     else:
#         print("*"+"  "*(n+3)+" *")
#     i+=1
# print all prime numbers from 1 to 100
# c=0
# for i in range(1,101):
#     f=0
#     for j in range(1,i+1):
#         if i%j==0:
#             f+=1
#     if f==2:
#         c+=1
#         print(j)
# print(c)
# printing 1 to 500 amstrong numbers
# for i in range(1,501):
#     t=i
#     s=0
#     l=len(str(i))
#     while i>0:
#         r=i%10
#         s=s+r**l
#         i//=10
#     if t==s:
#         print(s)
# i=153
# t=i
# s=0
# l=len(str(i))
# while i>0:
#     r=i%10
#     s=s+r**l
#     i//=10
# if t==s:
#     print(s)
# print all even numbers from 1 to 100 using "continue"
# for i in range(1,101):
#     if i%2!=0:
#         continue
#     else:
#         print(i)
#Removing spaces from a string
# name="he llo worl d"
# res=""
# for i in name:
#     if i!=" ":
#         res+=i
# print(res)
#Reverse a string
# name="hello world"
# res=""
# for i in range(len(name)-1,-1,-1):
#     res+=name[i]
# print(res)
# n="hell owo rld"
# res=""
# res1=""
# for i in n:
#     if i!=" ":
#         res+=i
# print(res)
# for j in range(len(res)-1,-1,-1):
#         res1+=res[j]
# print(res1)
# name="my_variable_name"
# res=""
# l=name.split("_")
# print(l)
# res+=l[0]
# for i in range(1,len(l)):
#     res+=l[i].capitalize()
# print(res)
#convert snake case to pascal case
# name="my_variable_name"
# res=""
# l=name.split("_")
# print(l)
# for i in range(0,len(l)):
#     res+=l[i].capitalize()
# print(res)
#input:"myVariableName" output:"my_variable_name"
# name="myVariableName"
# res=""
# r=""
# for i in range(0,len(name)):
#     r=r+name[i]
#     if name[i].isupper():
#         r=r+"_"
#         res+=r
# print(res)
# def even(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"
# a=int(input("enter a value"))
# print(even(a))
# def leap(a):
#     if a%4==0 and a%100!=0 or a%400==0:
#         return "leap year"
#     else:
#         return "not a leap year"
# print(leap(2019))

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
# for i in range(0,5):
#     print(fibonacci(i))
#sum of digits using recursion
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return n%10+sum(n//10)
# print(sum(123))
# n=1234
# s=0
# while n>0:
#     r=n%10
#     s=s*10+r
#     n//=10
# print(s)
#reverse a number using recursion
# def reverse(n,r=0):
#     if n==0:
#         return r
#     else:
#         return reverse(n//10,r*10+n%10)
# print(reverse(123))
# A
# BB
# 123
# 1234
# *****
# n=65
# for i in range(1,6):
#     for j in range(1,i+1):
#         if i==1:
#             print(chr(n),end=" ")
#         elif i==2:
#             print(chr(n+1),end=" ")
#         elif i==3 or i==4:
#             print(j,end=" ")
#         else:
#             print("*",end=" ")
#     print()
# lst=[121,333,421,563,454]
# result=[]
# for n in lst:
#     sum=0
#     t=n
#     s=0
#     while n>0:
#         r=n%10
#         s=s*10+r
#         n//=10
#     if t==s:
#         while t>0:
#             r=t%10
#             sum+=r
#             t//=10
#         result.append(sum)
# print(result)
# ------------
# name=input("enter a value")
# res=""
# for i in name:
#     n=ord(i)
#     res+=chr(n+1)
# print(res)


# str1 = input("enter a str")
# sub = input("Enter substring: ")
# i = 0  
# j = 0  
# while i < len(str1) and j < len(sub):
#     if str1[i] == sub[j]:
#         j += 1
#     i += 1
# if j == len(sub):
#     print("True")
# else:
#     print("False")
# str1="HeLLo"
# result=""
# for i in str1:
#     if i.isupper():
#         result+=i.lower()
#     else:
#         result+=i.upper()
# print(result)
# str1="abc123de5"
# res=""
# for i in str1:
#     if ord(i)>=48 and ord(i)<=57:
#         res+=i
# print(res)
# psw=input("enter")
# uc=0
# lc=0
# dc=0
# sc=0
# for i in psw:
#     if i.isupper():
#         uc+=1
        
#     elif i.islower():
#         lc+=1
       
#     elif i.isdigit():
#         dc+=1
       
#     else:
#         sc+=1
       
# if uc==1 and lc==1 and dc==1 and sc==1:
#     print("strong password")

# str1="aabbccde"
# res=""
# r=""
# for i in str1:
#        c=str1.count(i)
#        if c>=2:
#            res+=i
# for i in res:
#     if i not in r:
#          r+=i
# class A:
#     a=10
#     b=20
#     def sum(self,c,d):
#         self.sum=0
#         self.c=c
#         self.d=d
#         self.sum=A.a+A.b+self.c+self.d
#         return self.sum
# obj=A()
# print(obj.sum(30,40))
# l=[12,23,19,4,24,76,34,80]
# for i in range(0,len(l)-1):
#     for j in range(i+1,len(l)-1):
#         if l[i]>l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l)
# print("third min:",l[2])
# print("third max:",l[-3])

# str1="aaabbcca"
# c=0
# r=""
# for i in str1:
#     c=str1.count(i)
#     if i not in r:
#         r+=i
#         r+=str(c)
# print(r)
#Integer value for Roman Numbers
# roman=(input("enter a roman number").strip()).upper()
# n=len(roman)
# t=0
# d={'I':1,'v':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# for i in range(n):
#     value=d[roman[i]]
#     if i+1<n and value>d[roman[i+1]]:
#         t-=value
#     else:
#         t+=value
# print(t)

# l=[[10,20,30],[2,3,1],[4,6,2]]
# res=[]
# for i in l:
#     s=0
#     p=1
#     for j in i:
#         s+=j
#         p*=j
#     res.append([s,p])
# print(res)
# def square_matrix(m):
#   rows=len(m)
#   cols=len(m[0])
#   for i in m:
#       if len(i)!=cols:
#         return False
#   return True
# print(square_matrix([[1,2],[3,4]]))
# l1=[3,4]
# l2=[1,2]
# print(dict(zip(l1,l1)))
# s="aabcbd"
# s1=""
# for ch in s:
#     if ch not in s1:
#         c=s.count(ch)
#         s1+=ch
#         s1+=str(c)
# print(s1)
# 
# res=""
# a=""
# d=""
# text=input("Enter text")
# for i in range(0,len(text)):
#     if text[i]=="]":
#         res+=a*int(d)
#         a=""
#         d=""
#     elif text[i].isdigit():
#         d+=text[i]
#     elif text[i].isalpha():
#         a+=text[i]
# print(res)   

#merge sort
# def mergesort(arr):
#     if len(arr)<=1:
#         return arr
#     else:
#         mid=len(arr)//2
#         left=mergesort(arr[:mid])
#         right=mergesort(arr[mid:])
#     return merge(left,right)
# def merge(left,right):
#     res=[]
#     while left and right:
#         if left[0]<right[0]:
#             res.append(left.pop(0))
#         else:
#             res.append(right.pop(0))
#     res.extend(left)
#     res.extend(right)
#     return res
# print("unsorted array")
# arr=[12,3,8,4,9,1,5]
# print("sorted array")
# print(mergesort(arr))
# def Diagonal_matrix(m):
#     l=[]
#     cols=len(m[0])
#     for i in m:
#         if cols!=len(i):
#             return False
#     for i in range(0,len(m)):
#         l.append(m[i][i])

#     return l
# print(Diagonal_matrix([[1,2,9],[3,4,7],[5,6,8]]))
# def anti_diagonal_matrix(m):
#     # Check if matrix is square
#     cols = len(m[0])
#     for row in m:
#         if len(row) != cols:
#             return False  # Not a square matrix

#     n = len(m)
#     l = []
#     for i in range(n):
#         l.append(m[i][n - i - 1])  # pick anti-diagonal element

#     return l

# print(anti_diagonal_matrix([[1,2,9],[3,4,7],[5,6,8]]))
# def Diagonal_matrix(m):
#     l=[]
#     cols=len(m[0])
#     for i in m:
#         if cols!=len(i):
#             return False
#     for i in range(0,len(m)):
#         l.append(m[i][i])
#     e=l[0]
#     for i in l:
#         if e!=i:
#             return False
#     return l
#print(Diagonal_matrix([[1,2,9],[3,1,7],[5,6,1]]))
# def Diagonal_matrix(m):
#     cols=len(m[0])
#     for i in m:
#         if cols!=len(i):
#             return False
#     for i in range(0,len(m)):
#         m[i][i]=0 
#     return m
# print(Diagonal_matrix([[1,2,9],[3,1,7],[5,6,1]]))
# 
# n=5
# for i in range(n,0,-1):
#     if i==5 or i==1:
#         print(" "*(n-i)+"* "*i)
#     else:
#         print(" "*(n-i)+"* "+"  "*(i-2)+"* ")
# for i in range(2,n+1):
#     if i==1 or i==5:
#         print(" "*(n-i)+"* "*i)
#     else:
#        print(" "*(n-i)+"* "+"  "*(i-2)+"* ")
# import os
# os.remove("triiiiii1.txt")
# s={1,2,3}
# s.add(4)
# print(s)
# s={1,2,3}
# s.add(4)
# s.discard(4)
# print(s)
# l=[1,2,3]
# print(set(l))
# n=5
# for i in range(1,n+1):
#     if i==1 or i==5:
#         print("* "*n)
#     else:
#         print("* "+"  "*(n-2)+"* ")
# n=5
# for i in range(1,n+1):
#     print("  "*(n-i)+"* "*i)
# def prime(n):
#     c=0
#     for num in range(2,n+1):
#         if n%num==0:
#             c+=1
#     if c==1:
#         return True
#     else:
#         return False
# low=int(input("Enter first number"))
# high=int(input("Enter last number"))
# for i in range(low,high+1):
#     s=0
#     t=i
#     while i>0:
#         r=i%10
#         s+=r
#         i=i//10
#     if prime(s):
#         print(t)
# def fibonacci_pattern(rows):
#     f0, f1 = 0, 1
#     for i in range(1, rows + 1):
#         for j in range(1, i + 1):
#             print(f0, end=" ")
#             f2 = f0 + f1
#             f0 = f1
#             f1 = f2
#         print()
# fibonacci_pattern(4)
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# i = 0  # pointer for s2

# for ch in s1:
#     if i < len(s2) and ch == s2[i]:
#         i += 1

# # If we matched all characters of s2 in correct order
# if i == len(s2):
#     print(True)
# else:
#     print(False)
def reverse(l):
    f = []
    for i in range(0, len(l)):
        if i % 2 != 0:
            r = l[i][::-1]
            f.append(r)
        else:
            f.append(l[i])
    return f
print(reverse([[1,2,3],[4,5,6]]))       
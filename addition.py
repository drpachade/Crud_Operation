# def add(a,b):
#   print("Addition is",a+b)
# add(10,20)  
# def add(x,y):
#   return x+y
# def sub(x,y):
#   return x-y
# def multiple(x,y):
#   return x*y
# def devid(x,y):
#   return x/y
# print(add(10,20))
# print(sub(100,20))
# print(multiple(10,20))
# print(devid(100,20))

# l1 = [1,2,3,2,3,2,4,3]
# res = []
# for i in l1:
#   if i not in res:
#     res.append(i)
# print(res)    
################################################
# l1 = [1,2,4,5,6,8]
# res = []
# for i in range(l1[0],l1[-1]+1):
#   if i not in l1:
#     res.append(i)
# print(res)    
###############################################
# Prime Number

# def prim_no(start,end):
#   for num in range(start,end):
#     if num > 1:
#       for i in range(2,num//2+1):
#         if num%i == 0:
#           break
#       else:
#         print(f"{num} is prime number")
# prim_no(1,100)          
###############################################
# Factorial of Number
# fact = 1
# num = 5
# if num > 1:
#   for i in range(2,num+1):
#     fact = fact*i
#   print(f"Factorial of {num} is {fact}")  
##############################################

#Lambda Programs

# Filter, Map, Reduce
l1 = [1,2,3,4,5,6,7,8,9]
# res = filter(lambda x : x%2 ==1,l1)
# print(list(res))
res1 = map(lambda x : x+x,l1)
# print(list(res1))
from functools import reduce
res2 = reduce(lambda x,y:x+y,l1)
print(res2)
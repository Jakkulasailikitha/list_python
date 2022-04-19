
# l=[4,3,2,8]
# a=[]
# i=0
# while i<len(l):
#     j=i
#     while j< len(l)-1:
#         a.append(str(l[i])+str(l[j+1]))
#         j=j+1
#     i=i+1
# print(a)

# 2.
# l=[43,20,12,3,6,123,5]
# i=0
# c=0
# while i<len(l):
#         if l[i]<20:
#             print([l[i]])
#         i=i+1


# l=[1,2,3,4]
# user=int(input("enter the number:"))
# i=0
# while i<len(l):
#     j=0
#     while j<len(l):
#         c= l[i]+l[j]
#         j=j+1
#     i=i+1
# print(c)


# user=input("enter the num:")
# i=0
# b=[]
# while i< len(user)-1:
    
#     a=int(user[i])*int(user[i+1])
#     b.append(a)
#     i=i+1
# print(b)
# j=0
# max=0
# while j< len(b):
#     if b[j]> max:
#        max=b[j] 
#     j=j+1
# print(max)

list1=[1,3,5,2,4,6,2]

list1.remove(2)

print(sum(list1))




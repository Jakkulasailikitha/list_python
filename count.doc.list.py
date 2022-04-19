# Count unique values inside a list.
# list = [1, 2, 2, 5, 8, 4, 4, 8]
# # Count = 5 #because [1,2,5,8,4] are unique values.
# c=0
# i=0
# a=[]
# while i<len(list):
#     if list[i] not in a:
#         a.append(list[i])
#         c=c+1
#     i=i+1
# print(c)
# Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22
a="InDuMathi"
i=0
b=[]
while i<len(a):
   c= a[i].upper()
   i=i+1
   b.append(c)

print(b)





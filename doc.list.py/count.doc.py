# Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22
list=[4,5,5,5,3,8]
a=[]
for x in list:
    n=list.count(x)
    if n>2:
        if a.count(x)==0:
            c=x
print(c)

# l=[1, 1, 1, 64, 23, 64, 22, 22, 22]
# a=[]
# for b in l:
#     n=l.count(b)
#     if n>2:
#         if a.count(b)==0:
#             a.append(b)
# print(a)



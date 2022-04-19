# Duplicates

# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# duplicates = [] 

# for values in n:

#     if n.count(values) > 1:

#         if values not in duplicates:

#             duplicates.append(values)

# print("Duplicate Values are : ",duplicates)



# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# i=0
# a=[]
# b=[]
# while i<len(n):
#     if n[i] not in a:
#         a.append(n[i])
#     else:
#         b.append(n[i])
#     i=i+1
# print(a)
# print(b)



list = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9] 
new = []  # defining output list
# condition for reviewing every
# element of given input list
for a in list: 
      # checking the occurrence of elements
    n = list.count(a) 
    # if the occurrence is more than
    # one we add it to the output list
    if n > 1:        
        if new.count(a) == 0:  # condition to check
            new.append(a)
print(new)  
# 
list = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
new=[]
for a in list:
    n=list.count(a)
    if n>1:
        if new.count(a)==0:
            new.append(a)           
print(new)

# Remove duplicates from a list.
# list = [1,2,3,1,2,2]
# # Output: [1,2,3]
# i=0
# a=[]
# while i<len(list):
#   if list[i] not in a:
#     a.append(list[i])
#   i=i+1
# print(a)




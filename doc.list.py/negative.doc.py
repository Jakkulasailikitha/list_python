# Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1

# list= [2, -7, 5, -64, -14]
# i=0
# positive=0
# negative=0
# while i<len(list):
#     if list[i]>0:
#         positive+=1
#     else:
#         negative+=1
#     i=i+1
# print( "no.of positive integers :",positive)
# print("no.of negative integers :",negative)

list = [-12, 14, 95, 3]
i=0
positive=0
negative=0
while i<len(list):
    if list[i]>0:
        positive+=1
    else:
        negative+=1
    i=i+1
print( "no.of positive integers :",positive)
print("no.of negative integers :",negative)
# Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# # List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
# print(len(list))
max=0
min=0
while i<len(list):
    if len(list)>max:
        max=len(list[i])
    elif len(list)>len(max) and len(max)>len(min):
        min=len(list[i])
    i=i+1
print(len(list))
print("the max length:",max)

print("the min length:",min)



list=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
# print(len(list))
max=0
min=0
while i<len(list):
    if len(list)>max:
        max=len(list[i])
    elif len(list)>min and max>min:
        min=len(list[i])
    i=i+1
print(len(list))
print("the max length:",max)

print("the min length:",min)
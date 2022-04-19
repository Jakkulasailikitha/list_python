# Write a Code that finds second maximum element from the list and print it.
# For this list, the output of your program should be 56.
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
index=0
first_max=0
second_max=0
# third_max=0
while index<len(numbers):
    if numbers[index]>first_max:
          second_max=first_max

          first_max=numbers[index]
    elif numbers[index]>second_max:
        second_max=numbers[index]
    
    index=index+1
print("first_max:",first_max)
print("second_max:",second_max)
# num=[10,50,40,49]
# i=0
# m=0
# s=0
# while i<len(num):
#     if num[i]>m:
#         s=m
#         m=num[i]
#     elif num[i]>s :
#         s=num[i]
#     i=i+1
# print(m)
# print(s)

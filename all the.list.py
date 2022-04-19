# Given a list of numbers. write a program to turn every item of a list into its square.
# numbers = [1, 2, 3, 4, 5, 6, 7]
# i=0
# a=[]
# while i<(len(numbers)):
#     b=numbers[i]*numbers[i]
#     a.append(b)
#     i=i+1
# print(a)


# two methods for this
# Given a two Python list. Write a program to iterate both lists simultaneously 
# and display items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
# Expected output:
# 10 400
# 20 300
# 30 200
# 40 100
l1 = [10, 20, 30, 40]
l2 = [100, 200, 300, 400]
l2.reverse()
i=0
while i<len(l1):
    print(l1[i],l2[i])
    i+=1

# # for x, y in zip(list1, list2[::-1]):
# #     print(x, y)

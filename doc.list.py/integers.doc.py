# Given the start and end of a range, write a Python program to print all negative numbers 
# in a given range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1

# Input: start = -3, end = 4
# Output: -3, -2, -1


# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
  
# # iterating each number in list
# for num in range(start, end + 1):
      
#     # checking condition
#     if num < 0:
#         print(num, end = " ")

# for the negitive integers
# start = int(input("Enter the start of range: "))
# end = int(input("Enter the end of range: "))
# for num in range(start,end):
#     if num<0:
#         print(num,end="")

# for thr positive integers
start=int(input ("enter the start range:"))
end=int(input("enter the end range:") )
for num in range(start,end):
    if num>=0:
        print(num,end="")
    
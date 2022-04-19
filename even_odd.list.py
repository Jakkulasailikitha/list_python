# How many people were there?
# Write a code that works for any list, and that tells how many odd numbers and 
# how many even numbers are there in a given list.

numbers = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_count=0
odd_count=0
while i<len(numbers):
    if numbers[i]%2==0:
        even_count+=1
    else:
        odd_count+=1
    i=i+1
print("No.of even number:",even_count)
print("No.of odd number:",odd_count)
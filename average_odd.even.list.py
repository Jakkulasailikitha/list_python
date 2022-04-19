# How much is the Average.
# Write a code that works for any list, it shows the two averages as the output. 
# One is the average of even numbers and the other is the average of odd numbers from the given list.
numbers = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_count=0
odd_average=0
even_average=0
odd_count=0
even_s=0
odd_s=0
while i< len(numbers):
    if numbers[i]%2==0:
        even_count+=1
        even_s=even_s+numbers[i]
        even_average=even_s//even_count
    if  numbers[i]%2!=0:
        odd_count+=1
        odd_s=odd_s+numbers[i]
        odd_average=odd_s//odd_count
    i=i+1
print("the average of even numbers:",even_average)
print("the average of odd numbers:",odd_average)

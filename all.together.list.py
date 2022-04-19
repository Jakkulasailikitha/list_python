# Write a code that works for all lists. It should print the output as the following 
# like for all the odd numbersand all the even numbers and for all the numbers in the given list, 
# it should calculate the following :
numbers= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_count=0
odd_count=0
even_sum=0
odd_sum=0
even_average=0
odd_average=0
while i<len(numbers):
    if numbers[i]%2==0:
        even_count+=1
        even_sum=even_sum+numbers[i]
        even_average=even_sum//even_count
    else:
        odd_count+=1
        odd_sum=odd_sum+numbers[i]
        odd_average=odd_sum//odd_count

    i=i+1
print("No.of even numbers:",even_count)
print("sum of even numbers:",even_sum)
print("The average of even numbers:",even_average)
print("No.of odd numbers:",odd_count)
print("sum of odd numbers:",odd_sum)
print("The average of even numbers:",odd_average)
print("The count of all numbers in the list:",even_count+odd_count)
print("The sum of all numbers in the list:",even_sum+odd_sum)
print("The average of all numbers in the list:",even_sum+odd_sum/11)

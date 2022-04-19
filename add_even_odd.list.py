# Write a code that works for any list, it should give two sums as outputs,
# one is the sum of odd numbers present in the list and
# the other is the sum of even numbers present in the list.

numbers= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_sum=0
odd_sum=0
while i<len(numbers):
    if numbers[i]%2==0:
        even_sum=even_sum+numbers[i]
    else:
        odd_sum=odd_sum+numbers[i]
    i=i+1
print("sum of even numbers:",even_sum)
print("sum of odd numbers:",odd_sum)
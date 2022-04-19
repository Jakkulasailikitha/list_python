# to find the third max
numbers=[23,56,45,10,3,67,70,1]
i=0
max=0
sec_max=0
third_max=0
while i<len(numbers):
    if numbers[i]>max:
        third_max=sec_max
        sec_max=max
        max=numbers[i]
    elif numbers[i]>sec_max:
        third_max=sec_max
        sec_max=numbers[i]
    elif numbers[i]>third_max:
        third_max=numbers[i]
    i=i+1
print(max)
print(sec_max)
print(third_max)




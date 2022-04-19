# List product excluding duplicates.
list = [6,1,3,5,6,3,1]
# Output: 90
i=0
product=1
a=[]
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
        product=product*a[i]
    i+=1
print(product)
# product of list
list = [6,1,3,5,6,3,1]
i=0
product=1
while i<len(list):
    product=product*list[i]
    i=i+1
print(product)


    
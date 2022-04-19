# remove string
# mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
# subStr = "over"
# i=0
# a=""
# c=mainStr.split()
# while i<len(c):
#     if c[i]!=subStr:
#         a+=" "+c[i]
#     i=i+1
# print(a)

# replace on`




mainStr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
subStr = "over"
print(mainStr.replace("over", "on"))
# replacementStr = "on"
# i=0
# a=""
# c=mainStr.split()
# while i<len(c):
#     if c[i]!=subStr:
# mainStr.replace('on','over')
# print(mainStr)
#        a+=" "+c[i]
#     i=i+1
# print(a)

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# # o/p:['My', 'name', 'is', 'Kelly']
# a=[]
# i=0
# while i<len(list1):
#         c=list1[i]+list2[i]
#         a.append(c)
#         i=i+1 
# print(a) 

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
# o/p:['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
a=[]
i=0
while i<len(list1):
    j=0
    while j<len(list2):
        b=list1[i]+list2[j]
        a.append(b)
        j=j+1
    i=i+1
print(a)


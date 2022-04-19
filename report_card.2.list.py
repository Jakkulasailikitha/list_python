# to find the average of the marks
# marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# marks=[[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
# i=0
# b=0
# l=len(marks[i])
# while i<len(marks):
#     if i<len(marks[i]):
#       s=sum(marks[i])
#       b=s//len(marks[i])
#     i=i+1
#     print("average if the marks:",b)

# 

marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65],[95, 45, 78],[87, 67, 49, 68, 88]]
i=0
b=0
while i<len(marks):
    if i<len(marks[i]):
        s=sum(marks[i])
        b=s//len(marks[i])
        i+=1
    print("average of marks:",b)

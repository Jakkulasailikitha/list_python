# to find the total marks of the student
# marks=[25,34,45,47,41,48]
# length=len(marks)
# index=0
# total_marks=0
# while index<length:
#     total_marks=marks[index]+total_marks
# #     index=index+1
# # print("total marks=",+(total_marks))


# # to find the marks less than 50 and more than 50
# students_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# length=len(students_marks)
# index=0
# less_than50=0
# more_than50=0
# while index<length:  
#     marks=students_marks[index]
#     if marks<50: 
#        less_than50=less_than50+1
#     else:
#         more_than50= more_than50+1
#     index=index+1
# print("number of sudents less than 50 :",less_than50)
# print("number of sudents more than 100 :",more_than50)


l=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
a=[]
b=[]
sum=0
average=0
while i<len(l):
    j=0
    while j<len(l[i]):
        sum=sum+l[i][j]
        j=j+1
    
    a.append(sum)
    c=sum/len(l[i])
    b.append(c)
    i=i+1
print("The sum of the each list:",a)
print("The average of the each list:",b)


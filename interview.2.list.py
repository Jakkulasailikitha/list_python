# the output should be[p1,p2,p3,p4,p5,q1,q2,q3,q4,q5]
# list=['p','q']
# i=0
# a=[]
# while i<len(list):
#     j=1
#     while j<=5:
#         b=list[i]+str(j)
#         a.append(b)
#         j=j+1
#     i=i+1
# print(a)


# one of the method
# list="ogd"
# list1="good"
# i=0
# while i<len(list):
#     a=list[0]+list[0]+list1[0]+list1[3]
#     i=i+1
# print("the output should be:",a)

# the second method
a="ogd"
b="good"
i=0
while i<len(a):
    j=0
    while j<len(b):
        if a[i]==b[j]:
            print("the out put should be",b[j],end="")
        j=j+1
    i=i+1


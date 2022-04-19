# 1.question
# the out put should be like ['22','23','24','32','33','34','42','43','44']
a=[2,3,4]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a):
        b.append(str(a[i])+str(a[j]))
        j=j+1
    i=i+1
print(b)

# 2.question
# the out put should be like [12,6,16] the max also
a=[4,3,2,8]
i=0
b=[]
while i<len(a)-1:
    c=a[i]*a[i+1]
    b.append(c)
    i=i+1
print(b)
j=0
max=0
while j<len(b):
    if b[j]>max:
        max=b[j]
    j=j+1
print("the max of the above list:",max)

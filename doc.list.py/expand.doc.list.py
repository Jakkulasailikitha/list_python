# for the expanded form 3 digits
num=int(input("enter the number;"))
n=num
i=0
j="0"
a=n%10
b=num//10
c=b%10
i=i+1
print(str(b-c)+j,"+",str(c)+j,"+",a)
# For example,
# if we give 9119  the function should return  811181, as the  square of 9 is 81 and square of 1  is 1.
# user=int(input("enter the number:"))
# temp=user
# p=0
# if temp>0:
#     a=temp%10
#     p=p+a*a
#     temp=temp//10
# print(p)
num=int(input("enter the number;"))
n=num
i=0
j="0"
a=n%10
b=num//10
c=b%10
print(str(b-c)+j,"+",str(c)+j,"+",a)
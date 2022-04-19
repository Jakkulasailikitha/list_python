# Count Occurences
# Occurences - is made from the word occur which means that how many times a certain character or
# word appears.

char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
b=[]
while i<len(char_list):
    count=0
    j=0
    while j<len(char_list):
        if char_list[i]==char_list[j]:
            count+=1
        j=j+1
    if char_list[i] not in b:
        # b.append(char_list[i])
        b+=char_list[i]
        print(char_list[i],":",count)
    i=i+1


 
# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# i=0
# c=0
# user=input("enter the elements :")
# while i<len(char_list):
#     if char_list[i]==user:
#         c+=1
#     i=i+1
# print(c)

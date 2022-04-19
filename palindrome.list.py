# Write a code that checks whether a list is a palindrome or not. 
# And print “Haan! palindrome hai” if its a pallindrome
#and “nahi! palindrome nahi hai” if its not a palindrome

string=input("enter the string :")
rev_string=string[::-1]
print("reversed strind :",rev_string)
if string==rev_string:
    print("it is a palindrome")
else:
    print("it is not a palindrome")





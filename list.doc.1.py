# first question in doc
# Iterate over both the values in a list and their indices
# grocery_list = ['flour','cheese','carrots']
# # Output:
# #=> 0: flour
# #=> 1: cheese
# #=> 2: carrots
# i=0
# while i<len(grocery_list):
#     # if i<len(grocery_list[i]):
#         print(i,":",grocery_list[i])
#         i=i+1


# second question
# Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest

# initializing list
test_list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't']]
  
# printing original list
print("The original list is : " ,(test_list))
  
# Convert Character Matrix to single String
# Using join() + list comprehension
res = ''.join(ele for sub in test_list for ele in sub)
  
# # printing result 
print("The String after join : " , res) 

# test_list = ['g', 'f', 'g', 'i', 's', 'b', 'e', 's', 't']
# list="".join(test_list)
# print(list)
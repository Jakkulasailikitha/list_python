


# question_list=["What is the capital of India?"]
# optional_list=["Chandigarh", "Bhopal", "Chennai", "Delhi"]
# answer_list=["4"]
# i=0
# while i<len(question_list):
#     print(i+1,".",question_list[i])
#     j=0
#     while j<len(optional_list):
#         print(j+1,".",optional_list[j])
#         j=j+1
#     user=input("enter the option:")
#     if user==answer_list[i]:
#         print("your answer is correct.")
#     else:
#         print("wrong answer,better luck next time.")
#     i=i+1

# name=input("enter the name:")
# print("wel come to the KBC game:",name)
# print("let's start the game",name)
# question_list = ["How many continents are there?",
# "What is the capital of India?",
# "NG mei kaun se course padhaya jaata hai?"]

# options_list =[
# ["Four", "Nine", "Seven", "Eight"],
# ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
# ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
# ]
# answer_list=["3","4","1"]
# i=0
# while i<=len(question_list):
#     print(i+1,":",question_list[i])
#     j=0
#     while j<=len(options_list):
#         print(j+1,":",options_list[i][j])
#         j=j+1
#     answer=input("enter the option here")
    
#     if answer==answer_list[i]:
#         print("your answer is correct,go for the next question",name)
#         print("are you want the 50:50 option:")
#     elif option==50:50: 

question_list=["how many continents are there","what is the capital of india","ng na kon kon corse padhey"]
option_list=[['four','nine','seven','eight'],
            ['chatishgarh','bhopal','chennai','delhi'],
            ['softwareengineer','counseling','tourism','agriculture',]]
fiftyfifty=[['four','seven'],['delhi','bhopal'],['chennai','delhi']]
solutions=[2,1,2]
solution_list=[3,4,1]
print('welcome to kbc game program')
print('your first question on screen')
i=0
c=0
while i<len(question_list):
    print("your question is")
    print(i+1,question_list[i])
    a=0
    while a<=len(option_list):
        print(a+1,option_list[i][a])
        a+=1
    j=int(input("enter the number"))
    if j==solution_list[i]:
        print("congrulations")
    elif j==5050:
        if c==0:
            m=0
            while m<len(fiftyfifty[i]):
                print(m+1,fiftyfifty[i][m])
                m=m+1
            c=c+1
            num=int(input('enter the solution')) 
            if num==solutions[i]:
                print('correct')
            else:
                print("your option is wrong")
                print("quit")
            
        else:
            print('you already used 5050 lifeline')
            num=int(input("enter option"))
            if num==solution_list[i]:
                print("congratulations")
                break
            else:
                
                print("your wronr")
                break
    else:
        print("wrong")
        print("quit")
        break
    
    i=i+1
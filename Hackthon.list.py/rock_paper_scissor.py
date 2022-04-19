#Importing the required modules
import tkinter as tk
import tkinter.font as font
import random
from tkinter import messagebox

#creating the window
window=tk.Tk()
window.title('Rock Paper Scissors')  
window.geometry('1000x500')
window.configure(bg='green2')

# creating the fonts
font1=font.Font(family='helvetica',size=30)
font2=font.Font(family='helvetica',size=30)
font3=font.Font(family='helvetica',size=30)
font4=font.Font(family='helvetica',size=30)

# the functions
def start():
    rock =tk.Button(window,text='Rock',bg='cyan2')
    rock['font']=font2
    rock.place(relx='0.07',rely='0.6')

    paper =tk.Button(window,text='Paper',bg='cyan2')
    paper['font']=font2
    paper.place(relx='0.27',rely='0.6')

    scissors =tk.Button(window,text='Scissors',bg='cyan2')
    scissors['font']=font2
    scissors.place(relx='0.47',rely='0.6')

# the help function
def help_func():
    messagebox.showinfo('Help','This Game is like the normal Rock Paper Scissors game that we all had played.choose one of the 3 buttons on the screen')







# creating the main label
main=tk.Label(window,text='Rock Paper Scissors',bg='green2',fg='royal blue')
main['font']=font1
main.place(relx='0.16',rely='0.001')

# creating the score label
score=tk.Label(window,text='Score',bg='green2',fg='royal blue')
score['font']=font1
score.place(relx='0.775',rely='0.008')

# creating the help button
help=tk.Button(window,text='Help',bg='cyan2',width=3,command=help)
help['font']=font3
help.place(relx='0.001',rely='0.0008')

# creating the margin
margin=tk.Label(window,text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n')
margin['font']=font2
margin.place(relx='0.65',rely='0.0075')

# creating the 2nd margin
margin2=tk.Label(window,text='_____________________',bg='green2')
margin2['font']=font1
margin2.place(relx='0.66',rely='0.08')

# creating the 3rd margin
margin3=tk.Label(window,text='|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n',bg='green2')
margin3['font']=font1
margin3.place(relx='0.83',rely='0.16')

# creating the start button
start=tk.Button(window,text='start',width=7,bg='cyan2',command=start)
start['font']=font2
start.place(relx='0.28',rely='0.13')

# creating the continue button
continue_=tk.Button(window,text='continue',width=7,bg='green2')
continue_['font']=font2
continue_.place(relx='0.28',rely='0.75')

# creating the bottom label
bottom=tk.Label(window,text='',bg='green2',width='60')
bottom['font']=font4
bottom.place(relx='0.1',rely='0.95')

# creating the you label
you=tk.Label(window,text='you',bg='green2')
you['font']=font2
you.place(relx='0.92',rely='0.2')

# creating thre computer label
computer=tk.Label(window,text='computer',bg='green2')
computer['font']=font2
computer.place(relx='0.67',rely='0.2')


# creating the 1st label of score board
label1=tk.Label(window,text='',bg='green2')
label1['font']=font2
label1.place(relx='0.73',rely='0.27')

# creating the 2st label of score board
label2=tk.Label(window,text='0',bg='green2')
label2['font']=font2
label2.place(relx='0.92',rely='0.27')




#creating the mainloop
window.mainloop()  



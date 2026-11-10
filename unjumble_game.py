'''words={
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964,
    2026:"learned about dictionaries"
}

print(words.values())'''

import tkinter
from tkinter import *
import random
from tkinter import messagebox

#create the main window
root=tkinter.Tk()

# Correct answers
answers = [
    "apple", "mango", "banana", "achieve", "kolkata",
    "evening", "servant", "receiver", "london", "ferrari",
    "hollow", "horror", "master", "morning", "bottle",
    "pen", "router", "copy", "narrow", "wide",
    "dive", "love", "block", "right", "simple",
    "deaf", "single", "knight", "hope"
]


def jumble_word(word):
    letters=list(word)

    random.shuffle(letters)
    jumbled="".join(letters)

    while jumbled==word:
        random.shuffle(letters)
        jumbled="".join(letters)

    return jumbled

#game variables
num=random.randrange(0,len(answers))
c=0 #correct answers
d=0 #total attempts

current_word=""

#display a new jumbled work
def reset():
    global num, current_word

    num=random.randrange(0,len(answers))
    current_word=jumble_word(answers[num])
    label.config(text=current_word)

    #clear the answer box
    e1.delete(0,END)
    #put cursor in answer box
    e1.focus_set()

    #Display the first word
def default():
    global current_word
    current_word=jumble_word(answers[num])
    label.config(text=current_word)


#Check the user's answer
def checkans(event=None):
    global num,c,d

    #get the answer and remove extra spaces
    var=e1.get().strip().lower()

    #prevent empty submissions
    if var=="":
        messagebox.showwarning(
            "Empty Answer",
            "Please enter your answer!"
        )

        return
    #increase total attempts

    d += 1

    #check the answer
    if var==answers[num]:
        messagebox.showinfo(
            "congratulations!",
            "Its the correct answer!"

        )

        c += 1

    else:
        messagebox.showerror(
            "Sorry",
            "It is wrong.\n"
            "The correct answer was:" +answers[num]



        )


    #update score
    score_label.config(
        text="Score:" +str(c) + "/" + str(d)

    )

    #displaying another word

    reset()



root.geometry("500x500+500+150")
root.title("Jumbled word game")
root.configure(background="#585BE0")

#game title
Label(
    root,
    text="JUMBLED WORD GAME",
    font=("Verdana",24,"bold"),
    bg="#585BE0",
    fg="#3ec2ff"


).pack(pady=20)

#label displaying the jumbled word
label=Label(
    root,
    font=("Verdana",26,"bold"),
    bg="#585BE0",
    fg="#3ec2ff",
)

label.pack(pady=30, ipady=10,ipadx=10)

ans = StringVar()

e1=Entry(
    root,
    font=("Verdana",20),
    textvariable=ans,
    justify="center"

)

e1.pack(ipady=5, ipadx=5)

Button(
    root,
    text="Check",
    font=("Comic Sans MS",18),
    width=10,
    bg="#333945",
    fg="#45CE30",
    relief=GROOVE,
    command=checkans

).pack(pady=20)

#reset
Button(
    root,
    text="Reset",
    font=("Comic Sans MS", 18),
    width=10,
    bg="#777E88",
    fg="#E1DA00",
    relief=GROOVE,
    command=reset
).pack(pady=10)

score_label=Label(
    root,
    text="Score:0/0",
    font=("Verdana", 18),
    bg="#000000",
    fg="#ffffff"
)

score_label.pack(pady=20)

#allows enter key to check answer
root.bind("<Return>", checkans)

default()


e1.focus_set()



root.mainloop()


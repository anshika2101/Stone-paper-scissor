import tkinter as tk
import random


# 0 = rock
# 1 = paper
# 2 = scissors


def rps(num):
    if num == 0:
        print("Choose : rock")
    elif num == 1:
        print("Choose : paper")
    else:
        print("Choose: scissors")
    com = random.randint(0, 2)
    print("Comp:", com)
    if com == 0:
        comAns = "ROCK"
    elif com == 1:
        comAns = "PAPER"
    else:
        comAns = "SCISSORS"

    comp['text'] = comAns  # Define what comp's text(line 68) will be
    label['text'] = result(num, com)  # Define what label's text(line 74) will be


def result(player, com):
    if player == com:  # Player and Com answer the same
        print("DRAW")
        result = "DRAW"
    elif player == 2 and com == 1:  # Player : Scissors, Com : Paper
        print("WIN")
        result = " YOU WIN !"
    elif player == 1 and com == 0:  # Player : Paper, Com : Rock
        print("WIN")
        result = "YOU WIN !"
    elif player == 0 and com == 2:  # Player : Rock, Com : Scissors
        print("WIN")
        result = "YOU WIN !"
    else:
        print("LOSE")
        result = "YOU LOSE !"

    return result


# Create our GUI App -> className is name of the window
root = tk.Tk(className=' RockPaperScissors')

# The Background
canvas = tk.Canvas(root, bg='#ccff99', width=620, height=690)
canvas.pack()

# Title of the game
title = tk.Label(root, font=('Bahnschrift', 30, 'bold'), text='ROCK - PAPER - SCISSORS', fg='black', bg='#ccff99')
title.place(anchor='center', relx=0.5, rely=0.06)

# "Computer : "
frame3 = tk.Frame(root, bg='black', width=300, height=75)
frame3.place(anchor='center', relx=0.5, rely=0.18)
ccom = tk.Label(frame3, text='Computer:', font=('OCR A Extended', 20, 'bold'), fg='#00ff00', bg='black')
ccom.place(relwidth=1, relheight=1)

# Show what Computer answer
frame1 = tk.Frame(root, bg='black', width=300, height=120)
frame1.place(anchor='center', relx=0.5, rely=0.3)
comp = tk.Label(frame1, font=('OCR A Extended', 34, 'bold'), fg='#00ff00', bg='black')
comp.place(relwidth=1, relheight=1)

# Show the result
frame2 = tk.Frame(root, bg='black', width=300, height=100)
frame2.place(anchor='center', relx=0.5, rely=0.5)
label = tk.Label(frame2, font=('OCR A Extended', 34, 'bold'), fg='#00ff00', bg='black')
label.place(relwidth=1, relheight=1)

# Direction "Choose Your Answer"
choose = tk.Label(root, font=('Bahnschrift', 22, 'bold'), text='Choose your Answer', fg='black', bg='#ccff99')
choose.place(anchor='center', relx=0.5, rely=0.62)

# Button Rock
button0 = tk.Button(root, text='rock', command=lambda: rps(0))
bt0_image = tk.PhotoImage(file='approck3.png')
button0.config(image=bt0_image, width="150", height="160")
button0.place(relx=0.08, rely=0.68)

# Button Paper
button1 = tk.Button(root, text='paper', command=lambda: rps(1))
bt1_image = tk.PhotoImage(file='apppaper3.png')
button1.config(image=bt1_image, width="150", height="160")
button1.place(relx=0.38, rely=0.68)

# Button Scissors
button2 = tk.Button(root, text='scissors', command=lambda: rps(2))
bt2_image = tk.PhotoImage(file='appsci3.png')
button2.config(image=bt2_image, width="150", height="160")
button2.place(relx=0.68, rely=0.68)

# Method for setting the window to non-resizable
root.resizable(False, False)

# Method to run the App
root.mainloop()
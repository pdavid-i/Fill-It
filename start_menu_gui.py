from tkinter import *
from functools import partial
from board import main


dificulty = 'easy'

def destroy_window(window):
    window.destroy()

def instructions_menu():
    instructions_tab = Tk()
    instructions_tab.title("Instructions")
    instruction_label = Label(instructions_tab, text="\nIn this game your goal is to leave\n as little empty spaces as you can\n", font ="Calibri", bg="blue", fg = "white")
    instruction_label.pack(fill = BOTH)
    instruction_label['borderwidth'] = 10
    instruction_label['relief'] = 'raised'

    instruction_label2 = Label(instructions_tab, text="\nPlacing a piece on the board is done by \n selecting it and clicking on the board where \n you want its upperleft corner to be\n", bg="white", fg="red", font="Arial")
    instruction_label2.pack(fill=BOTH)
    instruction_label2['borderwidth'] = 10
    instruction_label2['relief']= 'raised'

    instruction_label3 = Label(instructions_tab, text="\nAt any given time your score is \n equal to how many squares are filled \n When a row/column is filled, it empties! \n", font ="Helvetica", bg="yellow", fg="green")
    instruction_label3.pack(fill=BOTH)
    instruction_label3['borderwidth'] = 10
    instruction_label3['relief'] = 'raised'

    instruction_label4 = Label(instructions_tab,
                               text="\nKeep refining your strategy \n untill you can beat the game! \n (achieve a score of 90) \n", bg="green", fg="purple",
                               font="Consolas")
    instruction_label4.pack(fill=BOTH)
    instruction_label4['borderwidth'] = 10
    instruction_label4['relief'] = 'raised'


def set_difficulty_easy(menu, diff_menu):
    global dificulty
    dificulty = 'easy'
    diff_menu.destroy()
    menu.destroy()
    main(dificulty)

def set_difficulty_medium(menu, diff_menu):
    global dificulty
    dificulty = 'medium'
    diff_menu.destroy()
    menu.destroy()
    main(dificulty)

def set_difficulty_hard(menu, diff_menu):
    global dificulty
    dificulty = 'hard'
    diff_menu.destroy()
    menu.destroy()
    main(dificulty)

def start_game(menu):
    difficulty_menu = Tk()
    difficulty_menu['borderwidth'] = 10
    difficulty_menu['relief'] = 'raised'


    set_easy = partial(set_difficulty_easy, menu, difficulty_menu)
    set_medium = partial(set_difficulty_medium, menu, difficulty_menu, )
    set_hard = partial(set_difficulty_hard, menu, difficulty_menu)

    easy_button = Button(difficulty_menu, text="Easy", command= set_easy, bg="#20bf20", font="Verdana 10")
    medium_button = Button(difficulty_menu, text="Medium", command = set_medium, bg="#7070ff", font="Verdana 10")
    hard_button = Button(difficulty_menu, text="Hard", command = set_hard, bg="#ff2020", font="Verdana 10")
    easy_button.pack(fill=BOTH)
    medium_button.pack(fill=BOTH)
    hard_button.pack(fill=BOTH)


    #main()

start_menu = Tk()
poza_cu_pug = PhotoImage(file = "photos\game_start.gif")
poza_cu_play = PhotoImage(file = "photos\play_button.gif")
poza_cu_intrebare = PhotoImage(file = "photos\question_button.gif")
label_pug = Label(start_menu, image = poza_cu_pug)
fct = partial(start_game, start_menu)
start_button = Button(image = poza_cu_play, command = fct)
question_button = Button(image = poza_cu_intrebare, height=100, width=100, command=instructions_menu)
label_pug.grid(row = 0, columnspan = 2)
start_button.grid(row = 1, column = 0)
question_button.grid(row = 1, column = 1)

start_menu.mainloop()
from tkinter import *
from functools import partial
from GUI2 import main


dificulty = 'easy'

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

    set_easy = partial(set_difficulty_easy, menu, difficulty_menu)
    set_medium = partial(set_difficulty_medium, menu, difficulty_menu)
    set_hard = partial(set_difficulty_hard, menu, difficulty_menu)

    easy_button = Button(difficulty_menu, text="Easy", command= set_easy)
    medium_button = Button(difficulty_menu, text="Medium", command = set_medium)
    hard_button = Button(difficulty_menu, text="Hard", command = set_hard)
    easy_button.pack(fill=BOTH)
    medium_button.pack(fill=BOTH)
    hard_button.pack(fill=BOTH)


    #main()

start_menu = Tk()
poza_cu_pug = PhotoImage(file = "photos\puggy.gif")
poza_cu_play = PhotoImage(file = "photos\play_button.gif")
label_pug = Label(start_menu, image = poza_cu_pug)
fct = partial(start_game, start_menu)
start_button = Button(image = poza_cu_play, command = fct)

label_pug.pack()
start_button.pack()
start_menu.mainloop()
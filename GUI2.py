from tkinter import *
from tkinter import ttk
from functools import *
from functionalities import *
from domain import *

class Option:
    def __init__(self, button, difficulty):
        self.difficulty = difficulty
        self.button =  button
        self.shape = random_shape(self.difficulty)
        if self.shape == 'c1':
            self.poza = PhotoImage(file="photos\c1.gif")
            self.function = partial(set_c1, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=40)
        if self.shape == 'c2':
            self.poza = PhotoImage(file="photos\c2.gif")
            self.function = partial(set_c2, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=40)
        if self.shape == 'c3':
            self.poza = PhotoImage(file="photos\c3.gif")
            self.function = partial(set_c3, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=40)
        if self.shape == 'c4':
            self.poza = PhotoImage(file="photos\c4.gif")
            self.function = partial(set_c4, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=40)
        if self.shape == 'zet2':
            self.poza = PhotoImage(file="photos\zet2.gif")
            self.function = partial(set_zet2, self)
            self.button.configure(image=self.poza, command=self.function, width=70, height=47)
        if self.shape == 'zet1':
            self.poza = PhotoImage(file="photos\zet1.gif")
            self.function = partial(set_zet1, self)
            self.button.configure(image=self.poza, command=self.function, width=70, height=47)
        if self.shape == 'square':
            self.poza = PhotoImage(file="photos\square.gif")
            self.function = partial(set_square, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=60)
        if self.shape == 'horizontal line':
            self.function = partial(set_line, self)
            self.poza = PhotoImage(file="photos\horizontal.gif")
            self.button.configure(image=self.poza, command=self.function, width=90, height=10)
        if self.shape == 'vertical line':
            self.poza = PhotoImage(file="photos\lvertical.gif")
            self.function = partial(set_vertical, self)
            self.button.configure(image=self.poza, command=self.function, width=10, height=100)
        if self.shape == 'Lsus':
            self.function = partial(set_Lsus, self)
            self.poza = PhotoImage(file="photos\Lsus.gif")
            self.button.configure(image=self.poza, command=self.function, width=30, height=70)

    def reroll(self):

        self.shape = random_shape(self.difficulty)
        if self.shape == 'c1':
            self.poza = PhotoImage(file="photos\c1.gif")
            self.function = partial(set_c1, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=40)
        if self.shape == 'c2':
            self.poza = PhotoImage(file="photos\c2.gif")
            self.function = partial(set_c2, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=40)
        if self.shape == 'c3':
            self.poza = PhotoImage(file="photos\c3.gif")
            self.function = partial(set_c3, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=40)
        if self.shape == 'c4':
            self.poza = PhotoImage(file="photos\c4.gif")
            self.function = partial(set_c4, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=40)
        if self.shape == 'zet2':
            self.poza = PhotoImage(file="photos\zet2.gif")
            self.function = partial(set_zet2, self)
            self.button.configure(image=self.poza, command=self.function, width=70, height=47)
        if self.shape == 'zet1':
            self.poza = PhotoImage(file="photos\zet1.gif")
            self.function = partial(set_zet1, self)
            self.button.configure(image=self.poza, command=self.function, width=70, height=47)
        if self.shape == 'square':
            self.poza = PhotoImage(file="photos\square.gif")
            self.function = partial(set_square, self)
            self.button.configure(image=self.poza, command=self.function, width=60, height=60)
        if self.shape == 'horizontal line':
            self.function = partial(set_line, self)
            self.poza = PhotoImage(file="photos\horizontal.gif")
            self.button.configure(image=self.poza, command=self.function, width=90, height=10)
        if self.shape == 'vertical line':
            self.poza = PhotoImage(file="photos\lvertical.gif")
            self.function = partial(set_vertical, self)
            self.button.configure(image=self.poza, command=self.function, width=10, height=100)
        if self.shape == 'Lsus':
            self.function = partial(set_Lsus, self)
            self.poza = PhotoImage(file="photos\Lsus.gif")
            self.button.configure(image=self.poza, command=self.function, width=30, height=70)

def set_Lsus(Option):
    global shape
    if shape != '0':
        return False
    shape = 'Lsus'
    Option.reroll()


def set_vertical(Option):
    global shape
    if shape != '0':
        return False
    shape = 'vertical line'
    Option.reroll()

def set_square(Option):
    global shape
    if shape != '0':
        return False
    shape = 'square'
    Option.reroll()

def set_zet1(Option):
    global shape
    if shape != '0':
        return False
    shape = 'zet1'
    Option.reroll()

def set_zet2(Option):
    global shape
    if shape != '0':
        return False
    shape = 'zet2'
    Option.reroll()

def set_c1(Option):
    global shape
    if shape != '0':
        return False
    shape = 'c1'
    Option.reroll()

def set_c2(Option):
    global shape
    if shape != '0':
        return False
    shape = 'c2'
    Option.reroll()

def set_c3(Option):
    global shape
    if shape != '0':
        return False
    shape = 'c3'
    Option.reroll()

def set_c4(Option):
    global shape
    if shape != '0':
        return False
    shape = 'c4'
    Option.reroll()


def set_line(Option):
    global shape
    if shape != '0':
        return False
    shape = 'horizontal line'
    Option.reroll()

def color(button_list, index):
    global game_board
    global src_fct
    global shape
    global up_border_score
    global up_border_highscore
    if shape == '0':
        return False
    if shape == 'c1':
        if validate_c1_add(button_list, index):
            game_board.add_c1(index)
            shape = '0'
    if shape == 'c2':
        if validate_c2_add(button_list, index):
            game_board.add_c2(index)
            shape = '0'
    if shape == 'c3':
        if validate_c3_add(button_list, index):
            game_board.add_c3(index)
            shape = '0'
    if shape == 'c4':
        if validate_c4_add(button_list, index):
            game_board.add_c4(index)
            shape = '0'
    if shape == 'zet2':
        if validate_zet2_add(button_list, index):
            game_board.add_zet2(index)
            shape = '0'
    if shape == 'zet1':
        if validate_zet1_add(button_list, index):
            game_board.add_zet1(index)
            shape = '0'
    if shape == 'square':
        if validate_square_add(button_list, index):
            game_board.add_square(index)
            shape = '0'
    if shape == 'horizontal line':
        if validate_line_add(button_list, index):
            game_board.add_horizontal_line(index)
            shape = '0'
    if shape == 'vertical line':
        if validate_vertical_add(button_list, index):
            game_board.add_vertical_line(index)
            shape = '0'
    if shape == 'Lsus':
        if validate_Lsus_add(button_list, index):
            game_board.add_Lsus(index)
            shape = '0'
    game_board.tick()
    current_score = game_board.score()
    highscore = read_highscore()
    up_border_score.configure(text=str(current_score), font="Times 10 bold")
    if (current_score > highscore):
        update_highscore(current_score)
        up_border_highscore.config(text=str(current_score))

   # scor = Button(secondary_frame)
    #scor.configure(text=str(game_board.score()))
   # scor.grid(row=11)

def main(difficulty):
    root = Tk()
    root.title("Fillit")

    global up_border_score
    global up_border_highscore
    main_frame = Frame(root)
    main_frame_border_left = Frame(root)
    main_frame_border_right = Frame(root)
    main_frame_border_down = Frame(root, bg="blue")
    main_frame_border_up = Frame(root)
    options = Frame(root, bg="cyan")
    button_list = []
    global game_board
    global shape
    game_board = Matrix(button_list)
    shape = '0'

    for i in range(100):
        button = Button(main_frame, width=4, height=2, bg="white")
        button.grid(row = i // 10, column = i%10)
        functie = partial(color, button_list, i)
        button.configure(command=functie)
        BUM = SquareSpace(button)
        game_board.list.append(BUM)

    button_one = Button(options, text="one")
    button_one.configure(height=5, width=9)
    button_one.grid(column=0, row = 0, padx=20, pady=20)
    option_1 = Option(button_one, difficulty)

    button_two = Button(options, text="two")
    button_two.configure(height=5, width=9)
    button_two.grid(column=1, row = 0, padx=80, pady=20)
    option_2 = Option(button_two, difficulty)

    button_three = Button(options, text="last")
    button_three.configure(height=5, width=9)
    button_three.grid(column=2, row = 0, padx=20, pady=20)
    option_3 = Option(button_three, difficulty)

    left_border = Label(main_frame_border_left,width = 5, height=27, bg = "cyan")
    left_border.pack(fill=BOTH)
    right_border = Label(main_frame_border_right, width=5, height=27, bg="cyan")
    right_border.pack()
    down_border = Label(main_frame_border_down, bg = "cyan", width = 65, height=4)
    down_border.pack()
    #####################
    trophy_image = PhotoImage(file="photos/trophy.gif")



    #####################
    up_border_left_border = Label(main_frame_border_up, bg = "cyan",width=11, height=6)
    up_border_score_image = Label(main_frame_border_up,bg= "cyan", width = 10, height=6, text="Scor")
    up_border_score = Label(main_frame_border_up, bg="cyan", width=10, height = 6, text="    ")
    up_border_highscore_image = Label(main_frame_border_up,bg= "cyan", width = 65, height=92, image=trophy_image)
    up_border_highscore = Label(main_frame_border_up, bg="cyan", width=10, height=6, text=read_highscore())
    up_border_right_border = Label(main_frame_border_up, bg="cyan", width=11, height = 6)

    up_border_left_border.grid(row = 0, column = 0)
    up_border_score_image.grid(row = 0, column = 1)
    up_border_score.grid(row = 0, column = 2)
    up_border_highscore_image.grid(row = 0, column = 3)
    up_border_highscore.grid(row = 0, column = 4)
    up_border_right_border.grid(row = 0, column = 5)







    ####################
    main_frame_border_up.grid(row = 0, columnspan = 5)
    main_frame_border_left.grid(row = 1, column = 0)
    main_frame.grid(row = 1, column = 1, columnspan = 3)
    main_frame_border_right.grid(row = 1, column = 4)
    main_frame_border_down.grid(row = 2, columnspan = 5)
    options.grid(row = 3, columnspan=5,sticky=W+E+N+S)
   # secondary_frame.grid(row = 1, column = 0, columnspan = 3)
    #for child in root.winfo_children(): child.grid_configure(padx=1, pady=1)
    root.mainloop()

if __name__ == "__main__":
    main()
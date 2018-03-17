from tkinter import *
from tkinter import ttk
from functools import partial

def restart(board, warning):
    warning.destroy()
    board.destroy()
    #play()

def game_over(score, board):
    croot = Toplevel()
    croot.title = "Game over!"
    top_frame = Frame(croot, bg = "white")
    image_label = Label(top_frame, bg="white")
    bottom_frame = Frame(croot, bg="white")

    if int(score) == 90:
        label = Label(croot, bg="#F5BE3C", text="CONGRATULASIONS")
        label['borderwidth'] = 10
        label['relief'] = 'sunken'
        img_sqr = PhotoImage(file="photos\super_pug.gif")
        image_label.config(image = img_sqr)
        image_label.image = img_sqr

    else:
        label = Label(croot,bg="#F5BE3C", text = "Unfortunately you've lost. You managed to reach the highscore of: " + str(score) + ". Try again!", font = "Calibri")
        label['borderwidth'] = 10
        label['relief'] = 'sunken'
        img_hor = PhotoImage(file="photos\puggy.gif")
        image_label.config(image = img_hor)
        image_label.image = img_hor


    image_label.pack()
    top_frame.pack(fill=BOTH)
    label.pack(fill = BOTH)

    final = partial(restart, board, croot)
    lasimg = PhotoImage(file="photos\eturn.gif")
    return_label = Button(bottom_frame, command=final, image= lasimg)
    return_label.image = lasimg

    return_label.pack()
    bottom_frame.pack(fill = BOTH)
    croot.mainloop()


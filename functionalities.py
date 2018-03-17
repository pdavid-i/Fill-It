from functools import *
from tkinter import *
from random import *
from game_over import game_over

def validate_square_add(list, index):
    if (index % 10) == 9:
        return False
    if (index //10) == 9:
        return False
    return list[index].wc() == 'white' and list[index+1].wc() == 'white' and list[index+10].wc() == 'white' and list[index+11].wc() == 'white'

def validate_line_add(list, index):
    if (index%10) > 6:
        return False
    return list[index].wc() == 'white' and list[index+1].wc() == 'white' and list[index+2].wc() == 'white' and list[index+3].wc() == 'white'

def validate_vertical_add(list, index):
    if (index//10) > 6:
        return False
    return list[index].wc() == 'white' and list[index+10].wc() == 'white' and list[index+20].wc() == 'white' and list[index+30].wc() == 'white'

def validate_Lsus_add(list, index):
    if (index//10) > 7 or (index%10) == 9:
        return False
    return list[index].wc() == 'white' and list[index+10].wc() == 'white' and list[index+20].wc() == 'white' and list[index+21].wc() == 'white'


def validate_zet1_add(list, index):
    if ((index//10) > 8) or ((index%10) > 7):
        return False
    return list[index].wc() == 'white' and list[index+1].wc() == 'white' and list[index+11].wc() == 'white' and list[index+12].wc() == 'white'


def validate_zet2_add(list, index):
    if (index//10 == 9) or ((index%10) == 9) or (index%10 == 0):
        return False
    return list[index].wc() == 'white' and list[index+1].wc() == 'white' and list[index+10].wc() == 'white' and list[index+9].wc() == 'white'


def validate_c1_add(list, index):
    if (index//10) > 8 or (index%10) == 0:
        return False
    return list[index].wc() == 'white' and list[index+10].wc() == 'white' and list[index+9].wc() == 'white'

def validate_point_add(list, index):
    return list[index].wc() == 'white'

def validate_c2_add(list, index):
    if ((index//10) == 9) or ((index%10) == 9):
        return False
    return list[index].wc() == 'white' and list[index+10].wc() == 'white' and list[index+11].wc() == 'white'

def validate_c3_add(list, index):
    if (index//10) > 8 or (index%10) > 8:
        return False
    return list[index].wc() == 'white' and list[index+1].wc() == 'white' and list[index+11].wc() == 'white'

def validate_c4_add(list, index):
    if (index//10) > 8 or (index%10) > 8:
        return False
    return list[index].wc() == 'white' and list[index+1].wc() == 'white' and list[index+10].wc() == 'white'

def random_shape(difficulty):
    easy_shapes = ['point', 'square', 'point', 'horizontal line', 'vertical line', 'Lsus', 'zet1', 'zet2', 'c1', 'c2', 'c3', 'c4', 'square', 'point', 'horizontal line', 'vertical line', 'zet1', 'zet2', 'c1', 'c2', 'c3', 'c4']
    medium_shapes = ['square', 'point', 'horizontal line', 'vertical line', 'Lsus', 'zet1', 'zet2', 'c1', 'c2', 'c3', 'c4']
    hard_shapes = ['square', 'point', 'horizontal line', 'vertical line', 'Lsus', 'zet1', 'zet2', 'c1', 'c2', 'c3', 'c4','Lsus', 'zet1', 'zet2' ,'square', 'point', 'horizontal line', 'vertical line', 'Lsus', 'zet1', 'zet2', 'c1', 'c2', 'c3', 'c4']

    if difficulty == 'easy':
        return easy_shapes[randint(0, len(easy_shapes) - 1)]
    if difficulty == 'medium':
        return medium_shapes[randint(0, len(medium_shapes)-1)]
    if difficulty == 'hard':
        return hard_shapes[randint(0, len(hard_shapes)-1)]

def read_easy_highscore():
    f = open('easy', 'r')
    score = int(f.readline())
    f.close()
    return score

def update_easy_highscore(new_score):
    f = open('easy', 'w')
    f.write(str(new_score))
    f.close()

def read_medium_highscore():
    f = open('medium', 'r')
    score = int(f.readline())
    f.close()
    return score

def update_medium_highscore(new_score):
    f = open('medium', 'w')
    f.write(str(new_score))
    f.close()

def read_hard_highscore():
    f = open('hard', 'r')
    score = int(f.readline())
    f.close()
    return score

def update_hard_highscore(new_score):
    f = open('hard', 'w')
    f.write(str(new_score))
    f.close()

def is_game_over(button_list, option_list, current_score, board):
    ok = False
    for option in option_list:
        shape = option.shape
        for index in range(100):
            if shape == 'c1':
                if validate_c1_add(button_list, index):
                    ok = True
            if shape == 'c2':
                if validate_c2_add(button_list, index):
                    ok = True

            if shape == 'c3':
                if validate_c3_add(button_list, index):
                    ok = True

            if shape == 'c4':
                if validate_c4_add(button_list, index):
                    ok = True

            if shape == 'zet2':
                if validate_zet2_add(button_list, index):
                    ok = True

            if shape == 'zet1':
                if validate_zet1_add(button_list, index):
                    ok = True

            if shape == 'square':
                if validate_square_add(button_list, index):
                    ok = True

            if shape == 'horizontal line':
                if validate_line_add(button_list, index):
                    ok = True

            if shape == 'vertical line':
                if validate_vertical_add(button_list, index):
                    ok = True

            if shape == 'Lsus':
                if validate_Lsus_add(button_list, index):
                    ok = True
            if shape == 'point':
                if validate_point_add(button_list, index):
                    ok = True
    if ok == False:
        game_over(current_score, board)

from random import *

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
    easy_shapes = ['c1', 'c2', 'c3', 'c4', 'square', 'horizontal line', 'vertical line', 'Lsus', 'zet1', 'zet2', 'c1', 'c2', 'c3', 'c4']
    medium_shapes = ['square', 'horizontal line', 'vertical line', 'Lsus', 'zet1', 'zet2', 'c1', 'c2', 'c3', 'c4']
    hard_shapes = ['horizontal line', 'vertical line', 'zet1', 'zet2', 'Lsus', 'square', 'horizontal line', 'vertical line', 'Lsus', 'zet1', 'zet2', 'c1', 'c2', 'c3', 'c4']

    if difficulty == 'easy':
        return easy_shapes[randint(0, len(easy_shapes) - 1)]
    if difficulty == 'medium':
        return medium_shapes[randint(0, len(medium_shapes)-1)]
    if difficulty == 'hard':
        return hard_shapes[randint(0, len(hard_shapes)-1)]

def read_highscore():
    f = open('highscores', 'r')
    score = int(f.readline())
    f.close()
    return score

def update_highscore(new_score):
    f = open('highscores', 'w')
    f.write(str(new_score))
    f.close()



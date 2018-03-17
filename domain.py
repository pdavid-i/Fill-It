
class SquareSpace:
    def __init__(self, button):
        self.color = 'white'
        self.button = button

    def wc(self):
        return self.color

    def set_color(self, color):
        self.color = color
        self.button.configure(bg = color)

class Matrix:
    def __init__(self, lista):
        self.list = lista

    def check_line(self, line):
        for i in range(10):
            if self.list[line*10 + i].wc() == 'white':
                return False
        return True

    def check_column(self, line):
        for i in range(10):
            if self.list[line + i*10].wc() == 'white':
                return False
        return True

    def free_line(self, line):
        for i in range(10):
             self.list[line*10 + i].set_color('white')

    def free_column(self, line):
        for i in range(10):
            self.list[line + i*10].set_color('white')

    def add_horizontal_line(self, index):
        self.list[index].set_color("blue")
        self.list[index + 1].set_color("blue")
        self.list[index + 2].set_color("blue")
        self.list[index + 3].set_color("blue")

    def add_vertical_line(self, index):
        self.list[index].set_color("#ff9999")
        self.list[index + 10].set_color("#ff9999")
        self.list[index + 20].set_color("#ff9999")
        self.list[index + 30].set_color("#ff9999")

    def add_square(self, index):
        self.list[index].set_color("red")
        self.list[index+1].set_color("red")
        self.list[index+10].set_color("red")
        self.list[index+11].set_color("red")

    def add_zet1(self, index):
        self.list[index].set_color("yellow")
        self.list[index+1].set_color("yellow")
        self.list[index+11].set_color("yellow")
        self.list[index+12].set_color("yellow")

    def add_zet2(self, index):
        self.list[index].set_color("yellow")
        self.list[index+9].set_color("yellow")
        self.list[index+1].set_color("yellow")
        self.list[index+10].set_color("yellow")

    def add_c1(self, index):
        self.list[index].set_color("brown")
        self.list[index+10].set_color("brown")
        self.list[index+9].set_color("brown")

    def add_c2(self, index):
        self.list[index].set_color("brown")
        self.list[index+10].set_color("brown")
        self.list[index+11].set_color("brown")

    def add_c3(self, index):
        self.list[index].set_color("brown")
        self.list[index+1].set_color("brown")
        self.list[index+11].set_color("brown")

    def add_c4(self, index):
        self.list[index].set_color("brown")
        self.list[index+1].set_color("brown")
        self.list[index+10].set_color("brown")

    def add_Lsus(self, index):
        self.list[index].set_color("green")
        self.list[index + 10].set_color("green")
        self.list[index + 20].set_color("green")
        self.list[index + 21].set_color("green")

    def add_point(self, index):
        self.list[index].set_color("purple")


    def score(self):
        scor = 0
        for x in self.list:
            if x.wc()!= 'white':
                scor += 1
        return scor

    def tick(self):
        columns = []
        lines = []
        for i in range(10):
            if self.check_column(i):
                columns.append(i)
            if self.check_line(i):
                lines.append(i)

        for x in columns:
            self.free_column(x)

        for x in lines:
            self.free_line(x)
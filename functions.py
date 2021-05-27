from random import choice, randint
from datetime import datetime, timedelta
import tkinter as tk

# 3x3 scramble generator
def Scramble_3x3():
    #constants
    SCRAMBLE_LENGTH = 20
    scramble_list = []

    MOVES = {
        'f':("F2","F","F'"),
        'r':("R2","R","R'"),
        'l':("L2","L","L'"),
        'b':("B2","B","B'"),
        'u':("U2","U","U'"),
        'd':("D2","D","D'")
        }

    AXES = {
        'x':('u','d'),
        'y':('r','l'),
        'z':('f','b')
        }

    #function for returning layers
    def layers():
        dim = list(AXES.values())
        axe = choice(dim)
        return axe[randint(0,1)], axe

    #setting variables for checking previous iterations
    prev_layer = ''
    prev_axe = ''
    prev_axe2 = ''

    #loop for scramble display
    while len(scramble_list) < SCRAMBLE_LENGTH:
        for layer in range(3):
            layer, axe = layers()
            if prev_layer == layer or prev_axe==prev_axe2 and prev_axe==axe:
                continue
            else:
                chosen_layer = MOVES.get(layer)
                move = choice(chosen_layer)
                scramble_list.append(move)
                prev_layer= layer            #setting variables
                prev_axe = axe               #to check
                prev_axe2 = prev_axe         #previous iterations
                break

    scramble = ""
    for move in scramble_list:
        scramble += move + ' '

    scramble1 = ""
    scramble2 = ""
    index = 0
    condition = False
    while (index < len(scramble)):
        if index < len(scramble)*0.55 :
            scramble1 += scramble[index]
        elif scramble[index]==' ' and not condition:
            condition = True
        elif condition:
            scramble2 += scramble[index]
        else:
            scramble1 += scramble[index]
        index += 1
    return scramble1, scramble2

#2x2 scramble generator
def Scramble_2x2():
    #constants
    SCRAMBLE_LENGTH = 11

    MOVES = {
        'f':("F2","F","F'"),
        'r':("R2","R","R'"),
        'u':("U2","U","U'"),
        }
    AXES = ('f','r','u')

    def random_layer():
        return choice(AXES)

    scramble_list = []
    prev_layer = ''
    while len(scramble_list) < SCRAMBLE_LENGTH:
        for layer in range(2):
            layer = random_layer()
            if prev_layer == layer:
                continue
            else:
                scramble_list.append(choice(MOVES[layer]))
                prev_layer = layer
                break

    scramble = ""
    for move in scramble_list:
        scramble += move + ' '

    return scramble

#4x4 scramble generator
def Scramble_4x4():
    #constants
    SCRAMBLE_LENGTH = 45
    scramble_list = []

    #Outer layers
    MOVES = {
        'f':("F2","F","F'"),
        'r':("R2","R","R'"),
        'l':("L2","L","L'"),
        'b':("B2","B","B'"),
        'u':("U2","U","U'"),
        'd':("D2","D","D'"),
        }
    AXES = {
        'x':('u','d'),
        'y':('r','l'),
        'z':('f','b')
        }
    def layers():
        dim = list(AXES.values())
        axe = choice(dim)
        return axe[randint(0,1)], axe

    #Inner layers
    WIDE_MOVES = {
        'rw':("Rw2","Rw","Rw'"),
        'fw':("Fw2","Fw","Fw'"),
        'uw':("Uw2","Uw","Uw'")
    }
    WIDE_AXES = ('fw','rw','uw')
    def random_layer():
        return choice(WIDE_AXES)

    #loop for generating scramble
    prob_in_out=("inner","inner","outer")
    prev_layer = ''
    prev_axe = ''
    prev_axe2 = ''
    wide_prev_layer = ''
    while len(scramble_list) < SCRAMBLE_LENGTH:
        in_out = choice(prob_in_out)
        if in_out=="inner":
            for layer in range(3):
                layer, axe = layers()
                if prev_layer == layer or prev_axe==prev_axe2 and prev_axe==axe:
                    continue
                else:
                    chosen_layer = MOVES.get(layer)
                    move = choice(chosen_layer)
                    scramble_list.append(move)
                    prev_layer= layer
                    prev_axe = axe
                    prev_axe2 = prev_axe
                    break
        elif in_out=="outer":
            for layer in range(2):
                layer = random_layer()
                if wide_prev_layer == layer:
                    continue
                else:
                    scramble_list.append(choice(WIDE_MOVES[layer]))
                    wide_prev_layer = layer
                    break
    #converting scramble list into list of 4 strings/lines
    scramble = ""
    counter = 0
    lines = []
    for move in scramble_list:
        scramble += move+' '
        counter+=1
        if counter%12==0:
            scramble = scramble.strip()
            lines.append(scramble)
            scramble=""
    lines.append(scramble)
    return lines

#5x5 scramble generator
def Scramble_5x5():
    #constants
    SCRAMBLE_LENGTH = 65
    scramble_list = []

    #Outer layers
    MOVES = {
        'f':("F2","F","F'"),
        'r':("R2","R","R'"),
        'l':("L2","L","L'"),
        'b':("B2","B","B'"),
        'u':("U2","U","U'"),
        'd':("D2","D","D'"),
        }
    AXES = {
        'x':('u','d'),
        'y':('r','l'),
        'z':('f','b')
        }
    def layers():
        dim = list(AXES.values())
        axe = choice(dim)
        return axe[randint(0,1)], axe

    #Inner layers
    WIDE_MOVES = {
        'rw':("Rw2","Rw","Rw'"),
        'fw':("Fw2","Fw","Fw'"),
        'uw':("Uw2","Uw","Uw'"),
        'dw':("Dw2","Dw","Dw'"),
        'lw':("Lw2","Lw","Lw'"),
        'bw':("Bw2","Bw","Bw'"),
    }
    WIDE_AXES = {
        'x':('uw','dw'),
        'y':('rw','lw'),
        'z':('fw','bw')
        }
    def wide_layers():
        dim = list(WIDE_AXES.values())
        axe = choice(dim)
        return axe[randint(0,1)], axe

    #loop for generating scramble
    prob_in_out=("inner","inner","inner","inner","inner","outer","outer","outer","outer")
    prev_layer = ''
    prev_axe = ''
    prev_axe2 = ''
    wide_prev_layer = ''
    wide_prev_axe = ''
    wide_prev_axe2 = ''
    while len(scramble_list) < SCRAMBLE_LENGTH:
        in_out = choice(prob_in_out)
        if in_out=="inner":
            for layer in range(3):
                layer, axe = layers()
                if prev_layer == layer or prev_axe==prev_axe2 and prev_axe==axe:
                    continue
                else:
                    chosen_layer = MOVES.get(layer)
                    move = choice(chosen_layer)
                    scramble_list.append(move)
                    prev_layer= layer
                    prev_axe = axe
                    prev_axe2 = prev_axe
                    break
        elif in_out=="outer":
            for layer in range(3):
                layer, axe = wide_layers()
                if wide_prev_layer == layer or wide_prev_axe==wide_prev_axe2 and wide_prev_axe==axe:
                    continue
                else:
                    chosen_layer = WIDE_MOVES.get(layer)
                    move = choice(chosen_layer)
                    scramble_list.append(move)
                    wide_prev_layer = layer
                    wide_prev_axe = axe
                    wide_prev_axe2 = wide_prev_axe
                    break
    #converting scramble list into list of 5 strings/lines
    scramble = ""
    counter = 0
    lines = []
    for move in scramble_list:
        scramble += move+' '
        counter+=1
        if counter%13==0:
            scramble = scramble.strip()
            lines.append(scramble)
            scramble=""
    return lines

#megaminx scramble generator
def Scramble_Megaminx():
    #constants
    SCRAMBLE_LENGTH = 77
    scramble = []

    MOVES = {
        'R':('R++','R--'),
        'D':('D++','D--'),
        'U':("U","U'")
    }

    scramble_line = ""
    for move in range (1,SCRAMBLE_LENGTH+1):
        if (move%11==0):
            scramble_line += (choice(MOVES['U'])+' ')
            scramble.append(scramble_line)
            scramble_line = ""
        elif len(scramble)%2==0:
            if (move%2==1):
                scramble_line += (choice(MOVES['R'])+' ')
            else:
                scramble_line += (choice(MOVES['D'])+' ')
        else:
            if (move%2==1):
                scramble_line += (choice(MOVES['D'])+' ')
            else:
                scramble_line += (choice(MOVES['R'])+' ')
    return scramble

# function for determening best and worst time
def best_worst(solves):
    if len(solves)==0:
        return '__','__'
    if len(solves)==1:
        if isinstance(solves[0],tuple):
            return solves[0][0],solves[0][0]
        else:
            return solves[0],solves[0]
    worst = -100000000
    best = 100000000
    for solve in solves:
        if solve == "DNF":
            worst = solve
        else:
            if isinstance(solve, tuple):
                solve = solve[0]
            if worst=="DNF":
                pass
            elif isinstance(solve, float):
                if solve > worst:
                    worst = solve
            if solve < best:
                best = solve
    if best==100000000:
        best = "DNF"
    return best, worst

#functios for average of 5,12,25,50,100
def average_of_(x,average):
    solves1 = []
    average_of_x = 0
    time_middle = 0
    if len(average) < x:
        return ""
    else:
        for index in range(1, x+1):
            solves1.append(average[-1*index])
        SOLVES = []
        for solve_ in solves1:
            if isinstance(solve_, tuple):
                SOLVES.append(solve_[0])
            else:
                SOLVES.append(solve_)
        num_of_solves = len(solves1)
        best, worst = best_worst(SOLVES)
        SOLVES.remove(best)
        SOLVES.remove(worst)
        sum_middle_times = 0
        for _solve_ in SOLVES:
            if _solve_ == "DNF":
                return "DNF"
            else:
                if isinstance(_solve_, tuple):
                    _solve_ = _solve_[0]
                sum_middle_times += _solve_
        return sum_middle_times / (num_of_solves-2)

#function for session average
def session_average(solves):
    if len(solves)<3:
        return "__"
    else:
        SOLVES = []
        for solve in solves:
            if isinstance(solve, tuple):
                SOLVES.append(solve[0])
            else:
                SOLVES.append(solve)
        num_of_solves = len(solves)
        best, worst = best_worst(SOLVES)
        SOLVES.remove(best)
        SOLVES.remove(worst)
        sum_middle_times = 0
        for solve in SOLVES:
            if solve == "DNF":
                return "DNF"
            else:
                if isinstance(solve, tuple):
                    solve = solve[0]
                sum_middle_times += solve
        return sum_middle_times / (num_of_solves-2)

#function for session mean
def session_mean(solves):
    if len(solves)==0:
        return "__"
    else:
        num_of_solves = len(solves)
        sum_times = 0
        for solve in solves:
            if solve == "DNF":
                num_of_solves-=1
            else:
                if isinstance(solve, tuple):
                    solve = solve[0]
                sum_times += solve
        try:
            return sum_times/num_of_solves
        except ZeroDivisionError:
            return "__"

#format time minute, seconds, milliseconds
def fmt_time(secs):
    if secs=='DNF':
        return 'DNF'
    sec = timedelta(seconds=secs)
    d = datetime(1,1,1) + sec
    if d.minute==0:
        return "%d.%.3d" % (d.second,d.microsecond/1000)
    else:
        return "%d:%.2d.%.3d" % (d.minute, d.second,d.microsecond/1000)

# small window to select type of cube
class Cube_Select:
    def __init__(self):
        self.window = tk.Tk()

        self.top_frame = tk.Frame(self.window)
        self.bottom_frame = tk.Frame(self.window)

        self.message = tk.Label(self.top_frame,text="close window after\nselecting cube")
        self.message.pack(side='left')

        self.selected_cube = tk.IntVar()
        self.selected_cube.set(3)

        self.rb2 = tk.Radiobutton(self.bottom_frame,text='2x2 Cube',width=14,variable=self.selected_cube,value=2)
        self.rb3 = tk.Radiobutton(self.bottom_frame,text='3x3 Cube',width=14,variable=self.selected_cube,value=3)
        self.rb4 = tk.Radiobutton(self.bottom_frame,text='4x4 Cube',width=14,variable=self.selected_cube,value=4)
        self.rb5 = tk.Radiobutton(self.bottom_frame,text='5x5 Cube',width=14,variable=self.selected_cube,value=5)
        self.megaminx = tk.Radiobutton(self.bottom_frame,text='Megaminx',width=14,variable=self.selected_cube,value=1)
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        self.rb5.pack()
        self.megaminx.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()
        tk.mainloop()

    def get_choice(self):
        return self.selected_cube.get()
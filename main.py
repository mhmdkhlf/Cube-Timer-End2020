#imports
from time import time
from sys import exit
from random import uniform
import os
import matplotlib.pyplot as plt
import functions
import pygame

### DISPLAY FUNCTIONS ###
def start_menu(cube):
    screen.fill(black)
    if cube==2:
        screen.blit(two_by_two,(140,0))
    elif cube==3:
        screen.blit(rubiks_cube,(140,0))
    elif cube==4:
        screen.blit(four_by_four,(140,0))
    elif cube==5:
        screen.blit(five_by_five,(140,0))
    elif cube==1:
        screen.blit(megaminx,(140,0))
    text1 = MEDIUM_FONT.render("hold 'C' to check", 1, white)
    text2 = MEDIUM_FONT.render("controls any-time", 1, white)
    screen.blit(text1, (int(WIDTH/2 - text1.get_width()/2), 70))
    screen.blit(text2, (int(WIDTH/2 - text2.get_width()/2), 130))
    text3 = MEDIUM_FONT.render("press 'S' to start", 1, white)
    text4 = MEDIUM_FONT.render("solving!", 1, white)
    screen.blit(text3, (int(WIDTH/2 - text3.get_width()/2), 430))
    screen.blit(text4, (int(WIDTH/2 - text4.get_width()/2), 490))
    pygame.display.update()

def display_commands():
    screen.fill(black)
    commands = (
        "Continue To Next Solve: [ENTER]",
        "+2 Penalty: [2]",
        "DNF Penalty: [D]",
        "Delete Last Solve: [BACKSPACE]",
        "Change Time: [T]",
        "Generate New Scramble: [S]",
        "End Session: [END]"
    )
    counter = 0
    for command in commands:
        text = SMALLER_FONT.render(command,1,white)
        screen.blit(text, (int(WIDTH/2 - text.get_width()/2), counter*85+25))
        counter+=1
    pygame.display.update()

def display_3x3_scramble(scramble1,scramble2):
    screen.fill(black)
    text1 = SMALLER_FONT.render(scramble1, 1, white)
    text2 = SMALLER_FONT.render(scramble2, 1, white)
    screen.blit(text1, (int(WIDTH/2 - text1.get_width()/2), 76))
    screen.blit(text2, (int(WIDTH/2 - text2.get_width()/2), 120))
    pygame.display.update()

def display_2x2_scramble(scramble):
    screen.fill(black)
    text = SMALLER_FONT.render(scramble, 1, white)
    screen.blit(text, (int(WIDTH/2 - text.get_width()/2), 100))
    pygame.display.update()

def display_4x4_scramble(lines):
    screen.fill(black)
    counter=1
    for line in lines:
        text = TINY_FONT.render(line, 1, white)
        screen.blit(text, (int(WIDTH/2 - text.get_width()/2), counter*40))
        counter+=1
    pygame.display.update()

def display_5x5_scramble(lines):
    screen.fill(black)
    counter=1
    for line in lines:
        text = FIVE_FONT.render(line, 1, white)
        screen.blit(text, (int(WIDTH/2 - text.get_width()/2), counter*36))
        counter+=1
    pygame.display.update()

def display_megaminx_scramble(lines):
    screen.fill(black)
    counter=0
    for line in lines:
        text = MEGAMINX_FONT.render(line, 1, white)
        screen.blit(text, (int(WIDTH/2 - text.get_width()/2), 15+counter*33))
        counter+=1
    pygame.display.update()

def ready(color):
    text = BIG_FONT.render("Ready", 1, color)
    screen.blit(text, (int(WIDTH/2 - text.get_width()/2), 300))
    pygame.display.update()

def solve_count(x):
    text = FIVE_FONT.render(f"Solve count: {x}", 1, light_blue)
    screen.blit(text,(0,int(HEIGHT-text.get_height())))
    pygame.display.update()

def _solving_():
    screen.fill((0,0,0))
    text = BIG_FONT.render(" Solving...", 1, green)
    screen.blit(text, (int(WIDTH/2 - text.get_width()/2), int(HEIGHT/2 - text.get_height()/2)))
    pygame.display.update()

def display_ps():
    text = TINY_FONT.render("You can now do whatever with this time",1,ps_color)
    text1 = TINY_FONT.render("(check commands by holding C)",1,ps_color)
    screen.blit(text, (int(WIDTH/2 - text.get_width()/2),50))
    screen.blit(text1, (int(WIDTH/2 - text1.get_width()/2),80))
    pygame.display.update()

def display_solve_time(time,extra):
    if isinstance(time,float):
        time = functions.fmt_time(time)
    screen.fill(black)
    text = TIME_FONT.render(time+extra, 1, white)
    screen.blit(text, (int(WIDTH/2 - text.get_width()/2), int(HEIGHT/2 - text.get_height()/2)))
    pygame.display.update()

def display_current_averages():
    averages = []
    of_num = [5,12,25,50,100]
    for x in of_num:
        averages.append(functions.average_of_(x,session_solves))
    counter = 0
    for average,x in zip(averages,of_num):
        if average=="":
            pass
        else:
            if averages=="DNF":
                text = TINY_FONT.render(f"ao{x}: DNF", 1, white)
            else:
                text = TINY_FONT.render(f"ao{x}: "+functions.fmt_time(average), 1, white)
            screen.blit(text, (int(WIDTH/2 - text.get_width()/2), 400+counter*35))
        counter+=1
    pygame.display.update()

def time_input():
    screen.fill(black)
    if user_input == "Start Typing":
        text_surface = MEDIUM_FONT.render(user_input,True,txt_button_color)
    else:
        text_surface = BIG_FONT.render(user_input,True,txt_button_color)
    input_rect.w = max(MIN_RECT_WIDTH,text_surface.get_width()+13)
    input_rect.x = min(WIDTH/2-MIN_RECT_WIDTH/2,WIDTH/2-(text_surface.get_width()+15)/2)
    pygame.draw.rect(screen,rect_color,input_rect,4)
    screen.blit(text_surface,(input_rect.x+10,input_rect.y+20))
    pygame.display.update()

def invalid_input(error):
    screen.fill(black)
    if error=="negative":
        error_message = "enter a POSITIVE number"
    else:
        error_message = "enter time in this format: '00.000'"
    directions = "press T to enter time again"
    text = SMALLER_FONT.render(error_message, 1, white)
    text1 = SMALLER_FONT.render(directions, 1, white)
    screen.blit(text,(int(WIDTH/2 - text.get_width()/2), int(HEIGHT/2 - text.get_height()/2)-30))
    screen.blit(text1,(int(WIDTH/2 - text1.get_width()/2), int(HEIGHT/2 - text1.get_height()/2)+30))
    pygame.display.update()

def new_session_button():
    screen.fill(black)
    title1 = "start new"
    title2 = " session "
    text1 = SMALLER_FONT.render(title1, 1, txt_button_color)
    text2 = SMALLER_FONT.render(title2, 1, txt_button_color)
    screen.blit(text1,(0,-2))
    screen.blit(text2,(0,int(text1.get_height())-7))
    button = pygame.Rect(-4,-8,int(text1.get_width())+6,int(text1.get_height())+int(text2.get_height()))
    pygame.draw.rect(screen,rect_color,button,4)
    pygame.display.update()
    return button

def solve_list(solves,scroll):
    line = "SOLVE LIST"
    title = SMALLER_FONT.render(line, 1, white)
    screen.blit(title,(8, button.h+1))
    pygame.draw.line(screen,white,(7,title.get_height()+button.h),(title.get_width()+5,title.get_height()+button.h),3)
    for num in range(scroll+1,len(solves)+1+scroll):
        if button.h+10+40*(num-scroll)>HEIGHT:
            break
        elif isinstance(solves[num-1], float):
            line = f'No.{num}: '+functions.fmt_time(solves[num-1])
        elif solves[num-1] == "DNF":
            line = f'No.{num}: DNF'
        else:
            line = f'No.{num}: ('+format(solves[num-1][0],'.3f')+solves[num-1][1]+')'
        text = STATS_FONT.render(line, 1, white)
        screen.blit(text,(8, 3+button.h+title.get_height()+41*(num-scroll-1)))
    pygame.display.update()

def stats(solves):
    line1 = "Session Stats"
    line2 = str(len(solves))+" solves"
    best,worst = functions.best_worst(solves)
    if isinstance(best,str):
        line3 = "Best time: "+best
    else:
        line3 = "Best time: "+functions.fmt_time(best)
    if isinstance(worst,str):
        line4 = "Worst time: "+worst
    else:
        line4 = "Worst time: "+functions.fmt_time(worst)
    average = functions.session_average(solves)
    if isinstance(average, str):
        line5 = "Average: "+average
    else:
        line5 = "Average: "+functions.fmt_time(average)
    mean = functions.session_mean(solves)
    if isinstance(mean, str):
        line6 = "Mean: "+mean
    else:
        line6 = "Mean: "+functions.fmt_time(mean)
    lines = [line1,line2,line3,line4,line5,line6]
    line_number = 0
    for line in lines:
        text = STATS_FONT.render(line, 1, white)
        if line_number==0:
            screen.blit(text,(WIDTH-int(text.get_width()),48))
            pygame.draw.line(screen,white,(WIDTH-text.get_width(),45+text.get_height()),(WIDTH,45+text.get_height()),3)
        else:
            screen.blit(text,(WIDTH-int(text.get_width()),line_number*90+40))
        line_number+=1
    pygame.display.update()

### displaying select cube window
begin_window = functions.Cube_Select()
cube = begin_window.get_choice()
selected = True
### PYGAME CODE START ###
pygame.init()

#fonts
MEGAMINX_FONT = pygame.font.SysFont('moderno20', 27)
FIVE_FONT = pygame.font.SysFont('moderno20', 34)
TINY_FONT = pygame.font.SysFont('moderno20', 40)
STATS_FONT = pygame.font.SysFont('moderno20', 50)
SMALLER_FONT = pygame.font.SysFont('moderno20', 55)
MEDIUM_FONT = pygame.font.SysFont('moderno20', 80)
BIG_FONT = pygame.font.SysFont('moderno20', 110)
TIME_FONT = pygame.font.SysFont('moderno20', 140)

#colors
black = (0,0,0)
white = (255,255,226)
green = (0,255,0)
red = (255,0,0)
light_blue = (50,160,220)
yellow = (255,255,0)
ps_color = (255,80,80)
rect_color = (245,120,0)
txt_button_color = (90,190,255)

#setting up screen and only image lol
WIDTH = 640
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
directory = os.path.dirname('C:\\Users\\moham\\source\\')
rubiks_cube = pygame.image.load(os.path.join(directory, '3x3.jpg'))
two_by_two = pygame.image.load(os.path.join(directory, '2x2.jpg'))
four_by_four = pygame.image.load(os.path.join(directory, '4x4.png'))
five_by_five = pygame.image.load(os.path.join(directory, '5x5.jpg'))
megaminx = pygame.image.load(os.path.join(directory, 'megaminx.jpg'))
MIN_RECT_WIDTH = 110
RECT_HEIGHT = 105
input_rect = pygame.Rect(WIDTH/2-MIN_RECT_WIDTH/2,HEIGHT/2-RECT_HEIGHT/2,MIN_RECT_WIDTH,RECT_HEIGHT)

session_solves = [] #list storing the current session's solves

# variables for main loop
end_session = False
started = False
solving = False
proceed = True
typing = False
wrong_input = False
in_commands = False
pressing_space = False
scramble1, scramble2 = "",""
scramble = ""
scramble_4x4 = []
scramble_5x5 = []
scramble_megaminx = []
plus = ""
user_input = ""
scroll = 0
button = None

### GAME MAIN LOOP ###
start_menu(cube)
while True:
    for event in pygame.event.get():
        #QUIT the app
        if event.type == pygame.QUIT:
            exit()
            pygame.quit()

        # hold C button for commands
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c and not solving and not end_session and not pressing_space and not typing:
            display_commands()
            in_commands = True
        if event.type == pygame.KEYUP and event.key == pygame.K_c and not solving and not end_session and not pressing_space and not typing:
            if proceed:
                if (scramble1=="" and scramble2=="") and scramble=="" and scramble_4x4=="" and scramble_5x5=="" and scramble_megaminx=="":
                    start_menu(cube)
                else:
                    if cube==3:
                        display_3x3_scramble(scramble1, scramble2)
                    elif cube==2:
                        display_2x2_scramble(scramble)
                    elif cube==4:
                        display_4x4_scramble(scramble_4x4)
                    elif cube==5:
                        display_5x5_scramble(scramble_5x5)
                    elif cube==1:
                        display_megaminx_scramble(scramble_megaminx)
                    ready(white)
                    display_current_averages()
                    solve_count(len(session_solves))
            else:
                display_solve_time(solve_time,plus)
                if penalty:
                    display_ps()
            in_commands = False

        # press S to start game & command to generate new scramble(same code different things lol)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s and not solving and proceed and not in_commands and not end_session:
            if cube==3:
                scramble1, scramble2 = functions.Scramble_3x3()
                display_3x3_scramble(scramble1, scramble2)
            elif cube==2:
                scramble = functions.Scramble_2x2()
                display_2x2_scramble(scramble)
            elif cube==4:
                scramble_4x4 = functions.Scramble_4x4()
                display_4x4_scramble(scramble_4x4)
            elif cube==5:
                scramble_5x5 = functions.Scramble_5x5()
                display_5x5_scramble(scramble_5x5)
            elif cube==1:
                scramble_megaminx = functions.Scramble_Megaminx()
                display_megaminx_scramble(scramble_megaminx)
            display_current_averages()
            ready(white)
            solve_count(len(session_solves))
            started = True

        ### FULL CYCLE OF STARTING SPACEBAR HOLD TIME DISPLAY ###
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and started and not solving and proceed and started and not in_commands:
            pressing_space = True
            ready(yellow)
            begin = time()
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE and started and not solving and proceed and started and pressing_space:
            end = time()
            if end - begin > 0.3:
                solving = True
                start_solve = time()
                _solving_()
            else:
                if cube==3:
                    display_3x3_scramble(scramble1,scramble2)
                elif cube==2:
                    display_2x2_scramble(scramble)
                elif cube==4:
                    display_4x4_scramble(scramble_4x4)
                elif cube==5:
                    display_5x5_scramble(scramble_5x5)
                elif cube==1:
                    display_megaminx_scramble(scramble_megaminx)
                ready(red)
                solve_count(len(session_solves))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and solving and started and pressing_space:
            end_solve = time()
            solving = False
            solve_time = end_solve-start_solve
            display_solve_time(solve_time,plus)
            session_solves.append(solve_time)
            display_ps()
            proceed = False
            penalty = True
            pressing_space = False

        # press enter to continue to next solve without modifying anything
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not solving and not proceed and not typing and started and not in_commands:
            if cube==3:
                scramble1, scramble2 = functions.Scramble_3x3()
                display_3x3_scramble(scramble1, scramble2)
            elif cube==2:
                scramble = functions.Scramble_2x2()
                display_2x2_scramble(scramble)
            elif cube==4:
                scramble_4x4 = functions.Scramble_4x4()
                display_4x4_scramble(scramble_4x4)
            elif cube==5:
                scramble_5x5 = functions.Scramble_5x5()
                display_5x5_scramble(scramble_5x5)
            elif cube==1:
                scramble_megaminx = functions.Scramble_Megaminx()
                display_megaminx_scramble(scramble_megaminx)
            display_current_averages()
            ready(white)
            solve_count(len(session_solves))
            plus = ""
            user_text = ""
            proceed = True

        conditions_for_penalties = not solving and not proceed and penalty and not typing and not in_commands

        # press 2 to add +2 penalty to solve
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and conditions_for_penalties and started:
            solve_time += 2
            session_solves[-1] = (solve_time,'+')
            plus = "+"
            display_solve_time(solve_time,plus)
            penalty = False

        # press backspace to delete last solve
        if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and conditions_for_penalties and started:
            solve_time = "deleted"
            del session_solves[-1]
            display_solve_time(solve_time,plus)
            penalty = False

        # press D to register solve as a DNF
        if event.type == pygame.KEYDOWN and event.key == pygame.K_d and conditions_for_penalties and started:
            solve_time = "DNF"
            session_solves[-1] = solve_time
            display_solve_time(solve_time,plus)
            penalty = False

        # press T to change solve (and code to get user input)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_t and conditions_for_penalties or wrong_input and started:
            typing = True
            penalty = False

        # processing user input
        if event.type == pygame.KEYDOWN and not solving and not proceed and not penalty and typing and started and not in_commands:
            if event.key == pygame.K_RETURN:
                try:
                    solve_time = float(user_input)
                    session_solves[-1] = solve_time
                    if solve_time <= 0:
                        invalid_input("negative")
                        wrong_input = True
                    else:
                        display_solve_time(solve_time,plus)
                        penalty = False
                        wrong_input = False
                except ValueError:
                    invalid_input("wrong")
                    wrong_input = True
                finally:
                    typing = False
                    user_input = ""
            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
                time_input()
            elif event.key == pygame.K_t and len(user_input)==0:
                user_input = "Start Typing"
                time_input()
                user_input = ""
            else:
                user_input += event.unicode
                time_input()

        # press END to end session and display Statistics of session
        if event.type == pygame.KEYDOWN and event.key == pygame.K_END and started and not solving and not in_commands:
            if not solving or proceed:
                button = new_session_button()
                solve_list(session_solves,scroll)
                stats(session_solves)
                started = False
                end_session = True
                selected = False
                timed_solves = []
                for solve in session_solves:
                    if isinstance(solve, float):
                        timed_solves.append(solve)
                    if isinstance(solve, tuple):
                        timed_solves.append(solve[0])
                if len(timed_solves)>1:
                    if cube==3:
                    #display of graph customized for my 3x3 times
                        #counter dictionary for charts
                        counter = {
                            'sub-7':0,
                            'sub-8':0,
                            'sub-9':0,
                            'sub-10':0,
                            'sub-11':0,
                            'shambles':0,
                            'DNF':0
                            }
                        #computing stats
                        for solve in session_solves:
                            if isinstance(solve, tuple):
                                solve = solve[0]
                            if solve == 'DNF':
                                counter['DNF'] += 1
                            elif solve >= 11:
                                counter['shambles'] += 1
                            elif int(solve) == 10:
                                counter['sub-11'] += 1
                            elif int(solve) == 9:
                                counter['sub-10'] += 1
                            elif int(solve) == 8:
                                counter['sub-9'] += 1
                            elif int(solve) == 7:
                                counter['sub-8'] += 1
                            else:
                                counter['sub-7'] += 1
                        #code to fill up the charts gradually
                        categories = []
                        count = []
                        for category in counter.keys():
                            if counter[category] != 0:
                                categories.append(category)
                                count.append(counter[category])
                        # display of barchart
                        plt.figure(figsize=(9, 6))
                        plt.subplot(3,2,1)
                        plt.ylabel('Number of Solves')
                        plt.title('Session Solves Bar Chart')
                        plt.bar(categories, count, width=0.7, color='deepskyblue',edgecolor='black', linewidth=2)
                        plt.subplot(3,2,2)
                        #display of piechart
                        plt.title('Session Solves Pie Chart')
                        explode = [0.08]*len(categories)
                        plt.pie(count, labels=categories, explode=explode, radius = 1.1, autopct='%1.1f%%', shadow=True, startangle=90)
                        #display of plot that displays no matter the puzzle
                        plt.subplot(3,1,3)
                    plt.xlabel('Solve Number')
                    plt.ylabel('Solve Time (secs)')
                    plt.title('Session Solves Detailed Times')
                    best, worst = functions.best_worst(timed_solves)
                    plt.xlim([0.9, len(timed_solves)+0.1])
                    plt.ylim([-.1 if best-1.5<0 else best-1.5, worst+1])
                    index_list = [i for i in range(1,len(timed_solves)+1)]
                    mean_line = [functions.session_mean(timed_solves)]*len(index_list)
                    plt.plot(index_list, timed_solves, linestyle='dashed', marker='o', markerfacecolor='blue', markersize=8)
                    plt.plot(index_list, mean_line)
                    plt.legend(['y1 = Solve Times',
                                'y2 = Session Mean'],
                                loc= 'best')
                    plt.grid()
                    plt.show(block=True) #plt.show(block=False) # plt.pause(3) # plt.close()

        #click with mouse1 to start new session or press N
        if button==None:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(event.pos) or event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            if not started and not solving and not selected:
                if not solving or proceed:
                    new_window = functions.Cube_Select()
                    cube = new_window.get_choice()
                    start_menu(cube)
                    selected = True
                    solving = False
                    proceed = True
                    scroll = 0
                    session_solves = []
                    end_session = False
                    scramble1, scramble2 = "",""
                    scramble = ""
                    scramble_4x4 = []
                    scramble_5x5 = []
                    scramble_megaminx = []
                    button = None

        #arrow keys to scroll
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and not started and not solving:
            if scroll > 0:
                scroll-=1
            button = new_session_button()
            solve_list(session_solves,scroll)
            stats(session_solves)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and not started and not solving:
            if scroll < len(session_solves)-12:
                scroll += 1
            button = new_session_button()
            solve_list(session_solves,scroll)
            stats(session_solves)

        clock.tick(60)
### END GAME & MAIN LOOP ###
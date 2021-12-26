from time import perf_counter
from sys import exit
import os
import matplotlib.pyplot as plt
from enum import Enum
import pygame
from solve import Solve
from puzzle_select import PuzzleSelector
from scrambles import generate_scramble
from session_solves import SessionSolves


class DrawInformation:
	BLACK = 0, 0, 0
	WHITE = 255, 255, 240
	GREEN = 0, 255, 0
	RED = 255, 0, 0
	YELLOW = 255, 255, 0
	LIGHT_BLUE = 50, 160, 220
	LIGHT_RED = 255, 80, 80
	ORANGE = 245, 120, 0
	global directory
	directory = os.path.dirname((os.path.dirname(os.path.realpath(__file__))+ os.path.sep + 'images' + os.path.sep))
	puzzles = ('2x2', '3x3', '4x4', '5x5', 'megaminx')
	images = {puzzle : pygame.image.load(os.path.join(directory, f'{puzzle}.jpg')) for puzzle in puzzles}

	def new_font(self, size):
		return pygame.font.SysFont('moderno20', size)

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.screen = pygame.display.set_mode((width, height))
		pygame.display.set_caption("My Rubik's Cube Timer App")


def display_start_menu(draw_info, puzzle):
	draw_info.screen.fill(draw_info.BLACK)
	draw_info.screen.blit(draw_info.images[puzzle], (135, 0))
	font = draw_info.new_font(80)
	text = font.render("hold 'C' to check", 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 65))
	text = font.render('commands any-time', 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 122))
	text = font.render("press 'S' to start", 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 430))
	text = font.render('solving!', 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 490))
	pygame.display.update()

def display_commands(draw_info):
    draw_info.screen.fill(draw_info.BLACK)
    commands = (
        'Continue To Next Solve: [ENTER]',
        '+2 Penalty: [2]',
        'DNF Penalty: [D]',
        'Delete Last Solve: [BACKSPACE]',
        'Change Time: [T]',
        'Generate New Scramble: [S]',
        'End Session: [END]'
    )
    font = draw_info.new_font(55)
    for command, counter in zip(commands, range(len(commands))):
        text = font.render(command, 1, draw_info.WHITE)
        draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), counter*85+25))
    pygame.display.update()

def display_ready_label(draw_info, color):
    font = draw_info.new_font(110)
    text = font.render('Ready', 1, color)
    draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 300))
    pygame.display.update()

def display_solve_count(draw_info, session_solves):
	font = draw_info.new_font(34)
	number_of_solves = session_solves.get_number_of_solves()
	text = font.render(f'Solve count: {number_of_solves}', 1, draw_info.LIGHT_BLUE)
	draw_info.screen.blit(text, (0, int(draw_info.height - text.get_height())))
	pygame.display.update()

def display_current_averages(draw_info, session_solves):
	averages = [5, 12, 25, 50, 100]
	font = draw_info.new_font(35)
	for average_of, counter in zip(averages, range(len(averages))):
		if average_of > session_solves.get_number_of_solves():
			break
		average = session_solves.average(of=average_of)
		text = font.render(f'ao{average_of}: {average}', 1, draw_info.WHITE)
		draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 400+counter*30))
	pygame.display.update()

def display_2x2_scramble(draw_info, scramble=None):
	draw_info.screen.fill(draw_info.BLACK)
	scramble = scramble if scramble!=None else generate_scramble('2x2')
	font = draw_info.new_font(55)
	scramble_moves = ''
	for move in scramble:
		scramble_moves += (move+' ')
	text = font.render(scramble_moves, 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 100))
	pygame.display.update()
	return scramble

def display_3x3_scramble(draw_info, scramble=None):
	draw_info.screen.fill(draw_info.BLACK)
	scramble = scramble if scramble!=None else generate_scramble('3x3')
	font = draw_info.new_font(55)
	scramble_moves = ''
	for i in range(11):
		scramble_moves += (scramble[i]+' ')
	text = font.render(scramble_moves, 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 76))
	scramble_moves = ''
	for i in range(11, len(scramble)):
		scramble_moves += (scramble[i]+' ')
	text = font.render(scramble_moves, 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 120))
	pygame.display.update()
	return scramble

def display_4x4_scramble(draw_info, scramble=None):
	draw_info.screen.fill(draw_info.BLACK)
	scramble = scramble if scramble!=None else generate_scramble('4x4')
	font = draw_info.new_font(40)
	scramble_moves = ''
	line = 1
	for move, counter in zip(scramble, range(1, len(scramble)+1)):
		scramble_moves += (move+' ')
		if counter%12 == 0:
			text = font.render(scramble_moves, 1, draw_info.WHITE)
			draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), line*40))
			scramble_moves = ''
			line += 1
	pygame.display.update()
	return scramble

def display_5x5_scramble(draw_info, scramble=None):
	draw_info.screen.fill(draw_info.BLACK)
	scramble = scramble if scramble!=None else generate_scramble('5x5')
	font = draw_info.new_font(34)
	scramble_moves = ''
	line = 1
	for move, counter in zip(scramble, range(1, len(scramble)+1)):
		scramble_moves += (move+' ')
		if counter%13 == 0:
			text = font.render(scramble_moves, 1, draw_info.WHITE)
			draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), line*36))
			scramble_moves = ''
			line += 1
	pygame.display.update()
	return scramble

def display_megaminx_scramble(draw_info, scramble=None):
	draw_info.screen.fill(draw_info.BLACK)
	scramble = scramble if scramble!=None else generate_scramble('megaminx')
	font = draw_info.new_font(27)
	scramble_moves = ''
	line = 1
	for move, counter in zip(scramble, range(1, len(scramble)+1)):
		scramble_moves += (move+' ')
		if counter%11 == 0:
			text = font.render(scramble_moves, 1, draw_info.WHITE)
			draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), line*32))
			scramble_moves = ''
			line += 1
	text = font.render(scramble_moves, 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), line*40))
	pygame.display.update()
	return scramble

def display_new_scramble(draw_info, puzzle):
	if puzzle == '2x2':
		scramble = display_2x2_scramble(draw_info)
	elif puzzle == '3x3':
		scramble = display_3x3_scramble(draw_info)
	elif puzzle == '4x4':
		scramble = display_4x4_scramble(draw_info)
	elif puzzle == '5x5':
		scramble = display_5x5_scramble(draw_info)
	elif puzzle == 'megaminx':
		scramble = display_megaminx_scramble(draw_info)
	return scramble

def display_same_scramble(draw_info, puzzle, scrmbl):
	if puzzle == '2x2':
		display_2x2_scramble(draw_info, scramble=scrmbl)
	elif puzzle == '3x3':
		display_3x3_scramble(draw_info, scramble=scrmbl)
	elif puzzle == '4x4':
		display_4x4_scramble(draw_info, scramble=scrmbl)
	elif puzzle == '5x5':
		display_5x5_scramble(draw_info, scramble=scrmbl)
	elif puzzle == 'megaminx':
		display_megaminx_scramble(draw_info, scramble=scrmbl)

def display_solving(draw_info):
    draw_info.screen.fill(draw_info.BLACK)
    font = draw_info.new_font(110)
    text = font.render(' Solving...', 1, draw_info.GREEN)
    draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), int(draw_info.height/2 - text.get_height()/2)))
    pygame.display.update()

def display_solve_time(draw_info, solve):
	draw_info.screen.fill(draw_info.BLACK)
	font = draw_info.new_font(140)
	text = font.render(solve.time_output(), 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), int(draw_info.height/2 - text.get_height()/2)))
	pygame.display.update()

def display_ps(draw_info):
	font = draw_info.new_font(40)
	text = font.render('You can now apply penalties to this solve', 1, draw_info.LIGHT_RED)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 50))
	text = font.render('(check commands by holding C)', 1, draw_info.LIGHT_RED)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 80))
	pygame.display.update()

def display_proceed(draw_info):
	font = draw_info.new_font(40)
	text = font.render('Press enter to proceed to next solve', 1, draw_info.LIGHT_RED)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), 70))
	pygame.display.update()

def display_solve_deleted(draw_info):
	draw_info.screen.fill(draw_info.BLACK)
	font = draw_info.new_font(140)
	text = font.render('deleted', 1, draw_info.WHITE)
	draw_info.screen.blit(text, (int(draw_info.width/2 - text.get_width()/2), int(draw_info.height/2 - text.get_height()/2)))
	pygame.display.update()

def display_time_input(draw_info, user_input):
	draw_info.screen.fill(draw_info.BLACK)
	if user_input == 'Start Typing':
		font = draw_info.new_font(80)
		text = font.render(user_input, 1, draw_info.LIGHT_BLUE)
	else:
		font = draw_info.new_font(110)
		text = font.render(user_input, 1, draw_info.LIGHT_BLUE)
	input_rect = pygame.Rect(draw_info.width/2 - 110/2, draw_info.height/2 -105/2, 110, 105)
	input_rect.w = max(110, text.get_width()+13)
	input_rect.x = min(draw_info.width/2 - 110/2, draw_info.width/2 - (text.get_width()+15)/2)
	pygame.draw.rect(draw_info.screen, draw_info.ORANGE ,input_rect, 4)
	draw_info.screen.blit(text,(input_rect.x+10,input_rect.y+20))
	pygame.display.update()

def display_invalid_input(draw_info, error_message):
	draw_info.screen.fill(draw_info.BLACK)
	font = draw_info.new_font(55)
	text = font.render(error_message, 1, draw_info.WHITE)
	draw_info.screen.blit(text,(int(draw_info.width/2 - text.get_width()/2), int(draw_info.height/2 - text.get_height()/2)-30))
	directions = 'press T to enter time again'
	text = font.render(directions, 1, draw_info.WHITE)
	draw_info.screen.blit(text,(int(draw_info.width/2 - text.get_width()/2), int(draw_info.height/2 - text.get_height()/2)+30))
	pygame.display.update()

def display_end_of_sessions_instructions(draw_info):
	draw_info.screen.fill(draw_info.BLACK)
	font = draw_info.new_font(35)
	text = font.render('start new session ', 1, draw_info.LIGHT_BLUE)
	draw_info.screen.blit(text, (0, 0))
	text = font.render('by pressing N', 1, draw_info.LIGHT_BLUE)
	draw_info.screen.blit(text,(20, 24))
	font = draw_info.new_font(25)
	text = font.render('(use arrow keys to scroll up and down solve list) ', 1, draw_info.LIGHT_BLUE)
	draw_info.screen.blit(text, (draw_info.width-text.get_width(), 10))
	pygame.display.update()

def display_solve_list(draw_info, session_solves, scroll):
	draw_info.screen.fill(draw_info.BLACK, (0, 50, int(draw_info.width/2), draw_info.height))
	font = draw_info.new_font(55)
	title = font.render('Solves list', 1, draw_info.WHITE)
	draw_info.screen.blit(title, (8, 60))
	pygame.draw.line(draw_info.screen, draw_info.WHITE,
                  (7, title.get_height()+60), (title.get_width()+5, title.get_height()+60), 3)
	for num in range(scroll, session_solves.get_number_of_solves()+scroll):
		if 150+40*(num-scroll) > draw_info.height:
			break
		solve_number = num+1
		solve_output = session_solves.get_solve_number(solve_number).time_output()
		text = font.render(f'No.{solve_number}: {solve_output}', 1, draw_info.WHITE)
		draw_info.screen.blit(text, (8, 65+title.get_height() + 41*(num-scroll)))
	pygame.display.update()

def display_session_stats(draw_info, session_solves):
	font = draw_info.new_font(50)
	text = font.render('Session Stats', 1, draw_info.WHITE)
	draw_info.screen.blit(text, (draw_info.width-int(text.get_width()), 48))
	pygame.draw.line(draw_info.screen, draw_info.WHITE,
                  (draw_info.width-text.get_width(), 45+text.get_height()), (draw_info.width, 45+text.get_height()), 3)
	number_of_solves = session_solves.get_number_of_solves()
	line1 = f'{number_of_solves} solves'
	best_solve = session_solves.get_best_solve()
	best_solve_output = '__' if best_solve is None else best_solve.time_output()
	line2 = f'Best solve: {best_solve_output}'
	worst_solve = session_solves.get_worst_solve()
	worst_solve_output = '__' if worst_solve is None else worst_solve.time_output()
	line3 = f'Worst solve: {worst_solve_output}'
	session_average = session_solves.average()
	line4 = f'Average: {session_average}'
	session_mean = session_solves.mean()
	line5 = f'Mean: {session_mean}'
	lines = [line1, line2, line3, line4, line5]
	for line, counter in zip(lines, range(1 ,len(lines)+1)):
		text = font.render(line, 1, draw_info.WHITE)
		draw_info.screen.blit(text, (draw_info.width - int(text.get_width()), counter*90 + 40))
	pygame.display.update()

def generate_plot(session_solves):
	timed_solves = [solve.get_time() for solve in session_solves.solves if solve.get_time()!=0]
	if len(timed_solves)> 1:
		plt.xlabel('Solve Number')
		plt.ylabel('Solve Time (secs)')
		plt.title('Session Solves Detailed Times')
		best_time = min(timed_solves)
		worst_time = max(timed_solves)
		plt.xlim([0.9, len(timed_solves)+0.1])
		plt.ylim([-.1 if best_time-1.5 < 0  else best_time-1.5, worst_time+1])
		index_list = [i for i in range(1,len(timed_solves)+1)]
		mean = sum(timed_solves)/len(timed_solves)
		mean_line = [mean]*len(index_list)
		plt.plot(index_list, timed_solves, linestyle='dashed', marker='o', markerfacecolor='blue', markersize=8)
		plt.plot(index_list, mean_line)
		plt.legend(['y1 = Solve Times','y2 = Session Mean'],loc= 'best')
		plt.grid()
		plt.show(block=True)


class LocationInApp(Enum):
	start_menu = 1
	scrambling = 2
	solving = 3
	assigning_penalties = 4
	manually_adding_time = 5
	end_of_session = 6

def main():
	scramble = []
	solve = None
	session_solves = SessionSolves()
	puzzle_selector = PuzzleSelector('3x3')
	puzzle = puzzle_selector.get_choice()

	pygame.init()
	clock = pygame.time.Clock()
	draw_info = DrawInformation(640, 600)
	location_in_app = LocationInApp.start_menu

	display_start_menu(draw_info, puzzle)
	while True:
		clock.tick(60)

		if location_in_app == location_in_app.start_menu:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
					pygame.quit()

				if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
					display_commands(draw_info)
				if event.type == pygame.KEYUP and event.key == pygame.K_c:
					display_start_menu(draw_info, puzzle)

				if event.type == pygame.KEYDOWN and event.key == pygame.K_s: #start scrambling and solving
					scramble = display_new_scramble(draw_info, puzzle)
					display_ready_label(draw_info, draw_info.WHITE)
					display_solve_count(draw_info, session_solves)
					display_current_averages(draw_info, session_solves)
					location_in_app = LocationInApp.scrambling


		elif location_in_app == LocationInApp.scrambling:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
					pygame.quit()

				if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
					display_commands(draw_info)
				if event.type == pygame.KEYUP and event.key == pygame.K_c:
					display_same_scramble(draw_info, puzzle, scramble)
					display_ready_label(draw_info, draw_info.WHITE)
					display_solve_count(draw_info, session_solves)
					display_current_averages(draw_info, session_solves)

				if event.type == pygame.KEYDOWN and event.key == pygame.K_s: #command to generate new scrambe
					scramble = display_new_scramble(draw_info, puzzle)
					display_ready_label(draw_info, draw_info.WHITE)
					display_solve_count(draw_info, session_solves)
					display_current_averages(draw_info, session_solves)

				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					display_ready_label(draw_info, draw_info.YELLOW)
					begin = perf_counter()
				if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
					end = perf_counter()
					if end-begin < 0.3:
						display_ready_label(draw_info, draw_info.RED)
					else:
						start_timer = perf_counter()
						location_in_app = LocationInApp.solving
						display_solving(draw_info)

				if event.type == pygame.KEYDOWN and event.key == pygame.K_END:
					display_end_of_sessions_instructions(draw_info)
					scroll = 0
					display_solve_list(draw_info, session_solves, scroll)
					display_session_stats(draw_info, session_solves)
					generate_plot(session_solves)
					location_in_app = LocationInApp.end_of_session


		elif location_in_app == LocationInApp.solving:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
					pygame.quit()

				if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					display_ready_label(draw_info, draw_info.YELLOW)
					end_timer = perf_counter()
					solve_time = end_timer - start_timer
					solve = Solve(puzzle, scramble, solve_time)
					session_solves.add_solve(solve)
					display_solve_time(draw_info, solve)
					display_ps(draw_info)
					penalty_added = False
					location_in_app = LocationInApp.assigning_penalties


		elif location_in_app == LocationInApp.assigning_penalties:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
					pygame.quit()

				if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
					display_commands(draw_info)
				if event.type == pygame.KEYUP and event.key == pygame.K_c:
					display_solve_time(draw_info, solve)
					if not penalty_added:
						display_ps(draw_info)
					else:
						display_proceed(draw_info)

				if event.type == pygame.KEYDOWN and event.key == pygame.K_2 and not penalty_added:
					solve.plus2()
					display_solve_time(draw_info, solve)
					display_proceed(draw_info)
					penalty_added = True
				if event.type == pygame.KEYDOWN and event.key == pygame.K_d and not penalty_added:
					solve.dnf()
					display_solve_time(draw_info, solve)
					display_proceed(draw_info)
					penalty_added = True
				if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE and not penalty_added:
					session_solves.delete_last_solve()
					display_solve_deleted(draw_info)
					display_proceed(draw_info)
					penalty_added = True
				if event.type == pygame.KEYDOWN and event.key == pygame.K_t and not penalty_added:
					location_in_app = LocationInApp.manually_adding_time
					user_input = 'Start Typing'
					display_time_input(draw_info, user_input)
					user_input = ''
					penalty_added = True

				if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
					scramble = display_new_scramble(draw_info, puzzle)
					display_ready_label(draw_info, draw_info.WHITE)
					display_solve_count(draw_info, session_solves)
					display_current_averages(draw_info, session_solves)
					location_in_app = LocationInApp.scrambling

				if event.type == pygame.KEYDOWN and event.key == pygame.K_END:
					display_end_of_sessions_instructions(draw_info)
					scroll = 0
					display_solve_list(draw_info, session_solves, scroll)
					display_session_stats(draw_info, session_solves)
					generate_plot(session_solves)
					location_in_app = LocationInApp.end_of_session


		elif location_in_app == LocationInApp.manually_adding_time:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
					pygame.quit()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						try:
							solve_time = float(user_input)
							if solve_time <= 0:
								display_invalid_input(draw_info, 'enter a POSITIVE number')
							else:
								solve.set_time(solve_time)
								display_solve_time(draw_info, solve)

								location_in_app = LocationInApp.assigning_penalties
						except ValueError:
							display_invalid_input(draw_info, "enter time in this format: '00.000'")
						finally:
							user_input = ''
					elif event.key == pygame.K_BACKSPACE:
						user_input = user_input[:-1]
						display_time_input(draw_info, user_input)
					elif event.key == pygame.K_t and len(user_input) == 0:
						user_input = 'Start Typing'
						display_time_input(draw_info, user_input)
						user_input = ''
					else:
						user_input += event.unicode
						display_time_input(draw_info, user_input)


		elif location_in_app == LocationInApp.end_of_session:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
					pygame.quit()

				if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and scroll > 0:
					scroll -= 1
					display_solve_list(draw_info, session_solves, scroll)
				if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and scroll < session_solves.get_number_of_solves()-12:
					scroll += 1
					display_solve_list(draw_info, session_solves, scroll)

				if event.type == pygame.KEYUP and event.key == pygame.K_n:
					scramble = []
					solve = None
					session_solves = SessionSolves()
					puzzle_selector = PuzzleSelector(puzzle)
					puzzle = puzzle_selector.get_choice()
					location_in_app = LocationInApp.start_menu
					display_start_menu(draw_info, puzzle)


if __name__ == '__main__':
    main()
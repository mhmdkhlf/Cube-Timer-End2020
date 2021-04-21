from random import choice
from move import Move

def random_move(moves):
    axis = choice(list(moves.keys()))
    layer = choice(list(moves[axis].keys()))
    turn = choice(moves[axis][layer])
    return Move(axis, layer, turn)

def scramble_turns(scramble):
    scramble_turns = []
    for move in scramble:
        scramble_turns.append(move.get_turn())
    return scramble_turns

def _2x2():
    SCRAMBLE_LENGTH = 11
    MOVES = {
        'x':{'u':("U2","U","U'")},
        'y':{'r':("R2","R","R'")},
        'z':{'f':("F2","F","F'")}
        }
    scramble = []
    while len(scramble) < SCRAMBLE_LENGTH:
        move = random_move(MOVES)
        if not (len(scramble) > 0 and move.same_axis(scramble[-1])):
            scramble.append(move)
    return scramble_turns(scramble)

def _3x3():
    SCRAMBLE_LENGTH = 20
    MOVES = {
        'x':{
            'u':("U2","U","U'"),
            'd':("D2","D","D'")
            },
        'y':{
            'r':("R2","R","R'"),
            'l':("L2","L","L'")
            },
        'z':{
            'f':("F2","F","F'"),
            'b':("B2","B","B'")
            }
        }
    scramble = []
    while len(scramble) < SCRAMBLE_LENGTH:
        move = random_move(MOVES)
        if (len(scramble) > 0 and move.same_layer(scramble[-1])
         or len(scramble) > 1 and move.same_axis(scramble[-1], scramble[-2])):
            continue
        else:
            scramble.append(move)
    return scramble_turns(scramble)

def _4x4():
    SCRAMBLE_LENGTH = 45
    MOVES = {
        'x':{
            'uw':("Uw2","Uw","Uw'"),
            'u':("U2","U","U'"),
            'd':("D2","D","D'")
            },
        'y':{
            'rw':("Rw2","Rw","Rw'"),
            'r':("R2","R","R'"),
            'l':("L2","L","L'")
            },
        'z':{
            'fw':("Fw2","Fw","Fw'"),
            'f':("F2","F","F'"),
            'b':("B2","B","B'")
            }
        }
    scramble = []
    while len(scramble) < SCRAMBLE_LENGTH:
        move = random_move(MOVES)
        if (len(scramble) > 0 and move.same_layer(scramble[-1]) 
         or len(scramble) > 1 and move.same_axis(scramble[-1], scramble[-2]) and move.same_layer(scramble[-2])
         or len(scramble) > 2 and move.same_axis(scramble[-1], scramble[-2], scramble[-3])):
            continue
        else:
            scramble.append(move)
    return scramble_turns(scramble) 

def _5x5():
    SCRAMBLE_LENGTH = 65
    MOVES = {
        'x':{
            'uw':("Uw2","Uw","Uw'"),
            'dw':("Dw2","Dw","Dw'"),
            'u':("U2","U","U'"),
            'd':("D2","D","D'")
            },
        'y':{
            'rw':("Rw2","Rw","Rw'"),
            'lw':("Lw2","Lw","Lw'"),
            'r':("R2","R","R'"),
            'l':("L2","L","L'")
            },
        'z':{
            'fw':("Fw2","Fw","Fw'"),
            'bw':("Bw2","Bw","Bw'"),
            'f':("F2","F","F'"),
            'b':("B2","B","B'")
            }
        }
    scramble = []
    while len(scramble) < SCRAMBLE_LENGTH:
        move = random_move(MOVES)
        if (len(scramble) > 0 and move.same_layer(scramble[-1]) 
         or len(scramble) > 1 and move.same_axis(scramble[-1], scramble[-2]) and move.same_layer(scramble[-2])
         or len(scramble) > 2 and move.same_axis(scramble[-1], scramble[-2], scramble[-3]) and move.same_layer(scramble[-3])
         or len(scramble) > 3 and move.same_axis(scramble[-1], scramble[-2], scramble[-3], scramble[-4])):
            continue
        else:
            scramble.append(move)
    return scramble_turns(scramble)

def _Megaminx():
    SCRAMBLE_LENGTH = 77
    MOVES = {
        'R':('R++','R--'),
        'D':('D++','D--'),
        'U':("U","U'")
    }
    scramble = []
    scramble_line = 0
    for move in range (1,SCRAMBLE_LENGTH+1):
        if move%11==0:
            scramble.append(choice(MOVES['U'])) 
            scramble_line += 1         
        elif (move%2 + scramble_line%2) == 1:
            scramble.append(choice(MOVES['R']))
        else:
            scramble.append(choice(MOVES['D']))
    return scramble

def scramble(puzzle):
    if puzzle == "2x2":
        scramble = _2x2()
    elif puzzle == "3x3":
        scramble = _3x3()
    elif puzzle == "4x4":
        scramble = _4x4()
    elif puzzle == "5x5":
        scramble = _5x5()
    else:
        scramble = _Megaminx()    
    return scramble

if __name__ == '__main__':
    print(*_5x5())
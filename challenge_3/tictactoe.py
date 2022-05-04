import os

number_of_moves = 0
turn = "x"

dictionary = { '1':' ', '2':' ','3':' ',
'4':' ','5':' ','6':' ',
'7':' ','8':' ','9':' '}
board_setup = ["_", "_", "_",
             "_", "_", "_",
             "_", "_", "_"]

def printboard():
    os.system("clear")
    print(board_setup[0] + " | " + board_setup[1] + " | " + board_setup[2])
    print("---------")
    print(board_setup[3] + " | " + board_setup[4] + " | " + board_setup[5])
    print("---------")
    print(board_setup[6] + " | " + board_setup[7] + " | " + board_setup[8])    

def is_taken(move) -> bool:
    return dictionary[move] != ' '

def is_invalid_input(move) -> bool:
    return move not in dictionary

def change_player():
    global turn
    if turn == 'x':
        turn = 'o'
    elif turn =='o':
        turn = 'x'


def check_win():
    if dictionary['1'] == dictionary['2']== dictionary['3'] != ' ':
        printboard()
        print(turn + " wins")
        return True
    elif dictionary['4'] == dictionary['5']== dictionary['6'] != ' ':
        printboard()
        print(turn + " wins")
        return True 
    
    elif dictionary['7'] == dictionary['8']== dictionary['9'] != ' ':
        printboard()
        print(turn + " wins")
        return True

    elif dictionary['1'] == dictionary['4']== dictionary['7'] != ' ':
        printboard()
        print(turn + " wins")
        return True
    
    elif dictionary['2'] == dictionary['5']== dictionary['8'] != ' ':
        printboard()
        print(turn + " wins")
        return True
    
    elif dictionary['3'] == dictionary['6']== dictionary['9'] != ' ':
        printboard()
        print(turn + " wins")
        return True
    
    elif dictionary['1'] == dictionary['5']== dictionary['9'] != ' ':
        printboard()
        print(turn + " wins")
        return True

    elif dictionary['3'] == dictionary['5']== dictionary['7'] != ' ':
        printboard()
        print(turn + " wins")
        return True
    else:
        return False

def make_move(move):
    # spot is not taken, move is valid
    move_number = int(move) - 1
    board_setup[move_number] = turn
    dictionary[move] = turn
    # increment 
    global number_of_moves
    number_of_moves += 1


while True:
    printboard()
    print("nmber of moves", number_of_moves)
    move = input( turn + ",it is your turn, select a move: ")
    
    
    if is_invalid_input(move):
        print("please choose a number from 1-9")
        continue

    if is_taken(move):
        print("that space is already filled, please move again")
        continue

    make_move(move)

    if check_win():
        break
        
    change_player()

    if number_of_moves >= 9:
        printboard()
        print('tie')
        break


    
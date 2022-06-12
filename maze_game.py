import os

array = []
user_y,user_x = -1,-1
    
def game_boards():
    global user_y
    global user_x
    player_input = input("choose puzzles 1-3 \n")
    file_name = f"maze{player_input}.txt"
    with open(file_name) as file:
        board_1 = file
        for y, line in enumerate(board_1):
            new_array = []
            for x, char in enumerate(line):
                if char == 'o':
                    char = ' '
                    user_x = x
                    user_y = y
                new_array.append(char)
            array.append(new_array)
            

def print_maze():
    global user_x
    global user_y
    global row_shadow
    for y, row in enumerate(array):
        row_shadow = row.copy()
        if y == user_y:
            row_shadow[user_x] = 'o'
        strrow = "".join(row_shadow)
        print(strrow.strip("\n"))
        
    

def make_move():
    global user_y
    global user_x
    global row_shadow
    while True:
        print("use w,a,s,and d to control your player")
        move_input = input()
        
        if move_input =='d':
            if array[user_y][user_x+1] == '*':
                user_x = user_x
                print('you cannot move there')
                print_maze()
            elif array[user_y+1][user_x] == 'X':
                user_x = user_x + 1
                print("you win!")
                print_maze()
                break
            else:    
                user_x = user_x + 1
                print_maze()
         
        if move_input =='s':
            if array[user_y+1][user_x] == '*':
                user_y = user_y
                print('you cannot move there')
                print_maze()
            elif array[user_y+1][user_x] == 'X':
                user_y = user_y + 1
                print("you win!")
                print_maze()
                break
            else:    
                user_y = user_y + 1
                print_maze()

        if move_input =='a':
            if array[user_y][user_x-1] == '*':
                user_x = user_x
                print('you cannot move there')
                print_maze()
            elif array[user_y][user_x - 1] == 'X':
                user_x = user_x - 1
                print("you win!")
                print_maze()
                break
            else:    
                user_x = user_x - 1
                print_maze()

        if move_input =='w':
            if array[user_y - 1][user_x] == '*':
                user_y = user_y
                print('you cannot move there')
                print_maze()
            elif array[user_y - 1][user_x] == 'X':
                user_y = user_y - 1
                print("you win!")
                print_maze()
                break
            else:    
                user_y = user_y - 1
                print_maze()

        


if __name__ == "__main__":
    os.system('clear')
    game_boards()
    print_maze()
    make_move()
    
    
    


       
    











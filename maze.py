from ast import Return
import os
while True:
    board_2 = [' ',' ','*','*','*','*','*','*','*','*',
                '*',' ',' ',' ',' ',' ','*',' ','*','*',
                '*',' ','*',' ','*',' ','*',' ','*','*',
                '*',' ',' ',' ','*',' ',' ',' ',' ','*',
                '*','*','*','*','*','*',' ','*','*','*',
                '*',' ','*',' ',' ',' ',' ','*','*','*',
                '*',' ',' ','*',' ','*','*','*','*','*',
                '*','*','*',' ',' ',' ',' ','*','*','*',
                '*',' ','*',' ','*',' ',' ','*','*','*',
                '*','*','*',' ','*','*','*','*','*','*']
    board_2[0]='o'
    
    def printboard():
        # os.system('clear')
        print(board_2[0]+ board_2[1]+ board_2[2]+ board_2[3]+ board_2[4]+ board_2[5]+ board_2[6]+ board_2[7] +board_2[8] +board_2[9] ) 
        print(board_2[10]+ board_2[11]+ board_2[12]+ board_2[13]+ board_2[14]+ board_2[15]+ board_2[16]+ board_2[71] +board_2[18] +board_2[19] ) 
        print(board_2[20]+ board_2[21]+ board_2[22]+ board_2[23]+ board_2[24]+ board_2[25]+ board_2[26]+ board_2[27] +board_2[28] +board_2[29] ) 
        print(board_2[30]+ board_2[31]+ board_2[32]+ board_2[33]+ board_2[34]+ board_2[35]+ board_2[36]+ board_2[37] +board_2[38] +board_2[39] ) 
        print(board_2[40]+ board_2[41]+ board_2[42]+ board_2[43]+ board_2[44]+ board_2[45]+ board_2[46]+ board_2[47] +board_2[48] +board_2[49] ) 
        print(board_2[50]+ board_2[51]+ board_2[52]+ board_2[53]+ board_2[54]+ board_2[55]+ board_2[56]+ board_2[57] +board_2[58] +board_2[59] ) 
        print(board_2[60]+ board_2[61]+ board_2[62]+ board_2[63]+ board_2[64]+ board_2[65]+ board_2[66]+ board_2[67] +board_2[68] +board_2[69] ) 
        print(board_2[70]+ board_2[71]+ board_2[72]+ board_2[73]+ board_2[74]+ board_2[75]+ board_2[76]+ board_2[77] +board_2[78] +board_2[79] ) 
        print(board_2[80]+ board_2[81]+ board_2[82]+ board_2[83]+ board_2[84]+ board_2[85]+ board_2[86]+ board_2[87] +board_2[88] +board_2[89] ) 
        print(board_2[90]+ board_2[91]+ board_2[92]+ board_2[93]+ board_2[94]+ board_2[95]+ board_2[96]+ board_2[97] +board_2[98] + board_2[99]) 
    printboard()



    player_move = input()
    new_move = 0
    moves = new_move
    board_2[0]='o'

    if player_move == 'w':
        moves = moves + 10
        board_2[moves] = 'o'
        printboard()
        board_2[moves] = new_move
        # break
    elif player_move == 's':
        moves = moves - 10
        board_2[moves] = 'o'
        printboard()
        board_2[moves] = new_move
        # break
        
        
    elif player_move == "a":
        moves = moves -1
        board_2[moves] = 'o'
        printboard()
        board_2[moves] = new_move
        # break
        
        
        
    elif player_move == "d":
        moves = moves + 1
        board_2[moves] = 'o'
        printboard()
        board_2[moves] = new_move
        # break
        
    elif player_move !=['d','s','a','w']: 
        print("you cant go there") 
        





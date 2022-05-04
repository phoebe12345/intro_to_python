import os

FREE_SPACE = "_"

class Board:
    def __init__(self):
       self.number_of_moves = 0
       self.board_setup = [FREE_SPACE] * 9

    def print(self, error_message: str = ""):
        os.system("clear")
        print(error_message + "\n")
        print(self.board_setup[0] + " | " + self.board_setup[1] + " | " + self.board_setup[2])
        print("---------")
        print(self.board_setup[3] + " | " + self.board_setup[4] + " | " + self.board_setup[5])
        print("---------")
        print(self.board_setup[6] + " | " + self.board_setup[7] + " | " + self.board_setup[8])

    def is_invalid_input(self, move: str) -> bool:
        if len(move) != 1:
            return True
        return not move.isdigit()

    def is_taken(self, move: str) -> bool:
        index = int(move) - 1
        return self.board_setup[index] != FREE_SPACE

    def make_move(self, move:str, current_player: str):
        index = int(move) - 1
        self.board_setup[index] = current_player
        self.number_of_moves += 1

    def is_out_of_move(self) -> bool:
        return self.number_of_moves >= 9

    def check_win(self):
        if self.board_setup[0] == self.board_setup[1]== self.board_setup[2] != FREE_SPACE:
            self.print(self.board_setup[0] + " wins")
            return True
        elif self.board_setup[3] == self.board_setup[4]== self.board_setup[5] != FREE_SPACE:
            self.print(self.board_setup[3] + " wins")
            return True

        elif self.board_setup[6] == self.board_setup[7]== self.board_setup[8] != FREE_SPACE:
            self.print(self.board_setup[6] + " wins")
            return True

        elif self.board_setup[0] == self.board_setup[3]== self.board_setup[6] != FREE_SPACE:
            self.print(self.board_setup[0] + " wins")
            return True

        elif self.board_setup[1] == self.board_setup[4]== self.board_setup[7] != FREE_SPACE:
            self.print(self.board_setup[1] + " wins")
            return True

        elif self.board_setup[2] == self.board_setup[5]== self.board_setup[8] != FREE_SPACE:
            self.print(self.board_setup[2] + " wins")
            return True

        elif self.board_setup[0] == self.board_setup[4]== self.board_setup[8] != FREE_SPACE:
            self.print(self.board_setup[0] + " wins")
            return True

        elif self.board_setup[2] == self.board_setup[4]== self.board_setup[6] != FREE_SPACE:
            self.print(self.board_setup[2] + " wins")
            return True

        return False

class Game:
    def __init__(self):
        self.players = ["x", "o"]
        self.player_index = 0
        self.number_of_players = 2
        self.board = Board()
        self.error_message = ""

    def get_current_player(self) -> str:
        return self.players[self.player_index]

    def change_player(self):
        self.player_index = (self.player_index + 1) % self.number_of_players

    def run(self):
        while True:
            self.board.print(self.error_message)
            self.error_message = ""
            current_player = self.get_current_player()
            move = input(current_player + ", it is your turn, select a move: ")

            if self.board.is_invalid_input(move):
                self.error_message = "please choose a number from 1-9"
                continue

            if self.board.is_taken(move):
                self.error_message = "that space is already filled, please move again"
                continue

            self.board.make_move(move, current_player)

            if self.board.check_win():
                break

            self.change_player()

            if self.board.is_out_of_move():
                self.board.print("tie")
                break


if __name__ == '__main__':
    Game().run()

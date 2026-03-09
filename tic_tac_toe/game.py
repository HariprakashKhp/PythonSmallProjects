from player import HumanPlayer, RandomComputerPlayer
import time

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)] for j in range(3)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]
    
    def is_empty_squares(self):
        return " " in self.board

    def num_empty_square(self):
        return self.board.count(" ")
    
    def make_move(self, square, letter):
        square = int(square)
        if self.board[square] == " ":
            self.board[square] = letter
            if self.is_winner(square, letter):
                self.current_winner = letter
            return True
        return False
    
    def is_winner(self, square, letter):
        row_idx = square // 3
        row = [self.board[row_idx : (row_idx + 1) * 3]]
        if(self.check_letters(row, letter)):
            return True
        
        col_idx = square % 3
        column = [self.board[col_idx + i * 3] for i in range(3)]
        if(self.check_letters(column, letter)):
            return True
        
        if(square % 2 == 0):
            diag1 = [self.board[i] for i in [0, 4, 8]]
            if(self.check_letters(diag1, letter)):
                return True
            diag2 = [self.board[i] for i in [2, 4, 6]]
            if(self.check_letters(diag2, letter)):
                return True
            
        return False
            
    def check_letters(self, list, letter):
        if(all([spot == letter for spot in list])):
                return True

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = "X" # X is starting the game.

    while game.is_empty_squares(): # as long as there is an empty square continue the loop
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.print_board()
                print("") # just new line

            if game.current_winner:
                if print_game:
                    print(letter + " wins")
                return letter
            
            letter = "O" if letter == "X" else "X"
        time.sleep(1)

    if print_game:
        print("It's a tie")

if __name__ == "__main__":
    x_player = HumanPlayer("X")
    o_player = RandomComputerPlayer("O")
    t = TicTacToe()
    play(t, x_player, o_player, True)
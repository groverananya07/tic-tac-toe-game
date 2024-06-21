class TicTacToe:
    def __init__(self) -> None:
        self.board = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
            ]
        self.player = 0
    
    def check_win(self):
        if (self.board[0][0] == self.board[0][1] == self.board[0][2]) or (self.board[1][0] == self.board[1][1] == self.board[1][2]) or (self.board[2][0] == self.board[2][1] == self.board[2][2]):
            return True
        elif (self.board[0][0] == self.board[1][0] == self.board[2][0]) or (self.board[0][1] == self.board[1][1] == self.board[2][1]) or (self.board[0][2] == self.board[1][2] == self.board[2][2]):
            return True
        elif (self.board[0][0] == self.board[1][1] == self.board[2][2]) or (self.board[2][0] == self.board[1][1] == self.board[0][2]):
            return True
        return False
    
    def fill_board(self, coordinates):
        # coordinates -> [1, 2] or [0, 1] => cooadinates[0] -> x, cooadinates[1] -> y
        if self.player == 0:
            self.board[ coordinates[0] ][ coordinates[1] ] = "O"
        else:
            self.board[ coordinates[0] ][ coordinates[1] ] = "X"

    def print_board(self):
        for row in self.board:
            print(row)

    def start_game(self):
        i = 0
        while True:
            if self.player==0:
                print("Player 1 turn: ")
            else:
                print("Player 2 turn: ")
            xCor = int(input("input x coordinate: "))
            yCor = int(input("input y coordinate: "))

            self.fill_board([xCor, yCor])

            self.print_board()

            if self.check_win() == True:
                if self.player == 0:
                    print("O has won the game...")
                    break
                else:
                    print("X has won the game...")
                    break
            
            if self.player==0:
                self.player = 1
            else:
                self.player = 0
            
            i += 1

            if i==9:
                print("Match over it's a draw.")
                break

            print("\n\n")




game = TicTacToe()

game.start_game()

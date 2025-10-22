import sys
class Game:

    def __init__(self, b):
        self.board = b
    
    def get_board(self):
        return self.board
    #print(board)
    def is_won(self, c):
        a = self.board
        return (
        a[0][0] == c and a[1][1] == c and a[2][2] == c or
        a[2][0] == c and a[1][1] == c and a[0][2] == c or
        a[0][0] == c and a[1][0] == c and a[2][0] == c or
        a[0][1] == c and a[1][1] == c and a[2][1] == c or
        a[0][2] == c and a[1][2] == c and a[2][2] == c or
        a[0][0] == c and a[0][1] == c and a[0][2] == c or
        a[1][0] == c and a[1][1] == c and a[1][2] == c or
        a[2][0] == c and a[2][1] == c and a[2][2] == c
        )

    def is_game(self):
        while not self.is_won("X") or not self.is_won("O"):
            i, j = map(int, input("Insert an X: ").split())
            if self.board[i][j] != " ":
                print("spot taken")
                continue
            else:
                self.board[i][j] = 'X'
            for row in self.board:
                print(" ".join(row))
            if self.is_won("X"):
                print("game over, X won!")
                sys.exit(1)
            istaken = True
            while istaken:
                k, l = map(int, input("Insert an O: ").split())
                if self.board[k][l] != " ":
                    istaken = True
                    print("spot taken")
                else:
                    istaken = False
                    self.board[k][l] = 'O'

            for row in self.board:
                print(" ".join(row))
            if self.is_won("O"):
                print("game over, O won!")
                sys.exit(1)


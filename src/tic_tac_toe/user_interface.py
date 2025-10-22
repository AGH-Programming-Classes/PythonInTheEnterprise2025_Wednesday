from tic_tac_toe.game_logic import Game
from typing import List

class BoardDrawer:
    def draw(self, board : List[List[int]]):
        pass

class ConsoleBoardDrawer(BoardDrawer):
    def draw(self, board : List[List[int]]):
        print("\t+---+---+---+");
        for x in range(3):
            print("\t", end = "")
            for y in range(3):
                print(f"| {board[x][y]} ", end = "")
            print("|\n\t+---+---+---+")

class UserInterface:   
    def __init__(self, boardPrinter : BoardDrawer):
        self._boardPrinter = boardPrinter

    def drawBoard(self, board : List[List[int]]):
        self._boardPrinter.draw(board)

    def getMove(self, player : str, board : List[List[int]]) -> List[int]:
        receivedCorrectMove = False

        while not receivedCorrectMove:
            move = input(f"\tPlayer {player}, make a move (x, y)\n").split(",")
            if len(move) == 2 and 0 < move[0] < 3 and 0 < move[1] < 3 and board[move[0]][move[1]] == " ":
                receivedCorrectMove = True
            else:
                print("\tIncorrect move, please try again.")

        return move


def startMainLoop(game : Game):
    is_running = True

    userInterface = UserInterface(ConsoleBoardDrawer())

    while is_running:
        userInterface.drawBoard(game.get_board())
        userInterface.getMove("X", game.board)
        break
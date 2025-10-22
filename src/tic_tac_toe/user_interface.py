from tic_tac_toe.game_logic import Game
from typing import List

class Printer:
    def draw(self, board : List[List[int]]):
        pass

class ConsoleBoardPrinter(Printer):
    def draw(self, board : List[List[int]]):
        print("\t+---+---+---+");
        for x in range(3):
            print("\t", end = "")
            for y in range(3):
                print(f"| {board[x][y]} ", end = "")
            print("|\n\t+---+---+---+")

class UserInterface:   
    def __init__(self, printer : Printer):
        self._printer = printer

    def drawBoard(self, board : List[List[int]]):
        self._printer.draw(board)

def startMainLoop(game : Game):
    is_running = True

    userInterface = UserInterface(ConsoleBoardPrinter())

    while is_running:
        userInterface.drawBoard(game.get_board())

        break
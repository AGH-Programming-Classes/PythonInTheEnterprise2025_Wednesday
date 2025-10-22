from tic_tac_toe.game_logic import Game
from tic_tac_toe.user_interface import startMainLoop

def main():
    print("=== Tic Tac Toe ===\n\n")

    board = [[" "]*3]*3
    game = Game(board)

    startMainLoop(game)

if __name__ == "__main__":
    main()

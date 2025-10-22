from enum import Enum


class BoardMarks(Enum):
    EMPTY = 0
    CROSS = 1
    NOUGHT = 2


class GameState:
    def __init__(self):
        self.board = [
            [BoardMarks.EMPTY for _ in range(3)] for _ in range(3)
        ]
        self.turn = 0

    def has_game_ended(self) -> bool:
        if self.turn >= 9:
            return True
        return self.check_for_win() is not None

    def _check_for_win_of_player(self, board_mark: BoardMarks) -> bool:
        # Horizontal win
        for row in range(3):
            if all([self.board[row][i] == board_mark for i in range(3)]):
                return True

        # Vertical win
        for col in range(3):
            if all([self.board[i][col] == board_mark for i in range(3)]):
                return True

        # Diagonal win
        if all([self.board[i][i] == board_mark for i in range(3)]):
            return True
        if all([self.board[2 - i][i] == board_mark for i in range(3)]):
            return True

        return False

    def check_for_win(self) -> BoardMarks | None:
        if self._check_for_win_of_player(BoardMarks.CROSS):
            return BoardMarks.CROSS
        if self._check_for_win_of_player(BoardMarks.NOUGHT):
            return BoardMarks.NOUGHT
        return None

    def whose_turn(self) -> BoardMarks:
        return BoardMarks.CROSS if self.turn % 2 == 0 else BoardMarks.NOUGHT

    def next_turn(self) -> None:
        self.turn += 1

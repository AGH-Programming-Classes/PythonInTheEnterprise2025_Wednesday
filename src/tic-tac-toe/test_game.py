import unittest

from game import GameState, BoardMarks


class TestGameState(unittest.TestCase):
    def test_check_for_win_horizontal(self):
        game = GameState()

        game.board = [
            [BoardMarks.CROSS, BoardMarks.CROSS, BoardMarks.CROSS],
            [BoardMarks.EMPTY, BoardMarks.NOUGHT, BoardMarks.EMPTY],
            [BoardMarks.EMPTY, BoardMarks.EMPTY, BoardMarks.NOUGHT],
        ]
        self.assertEqual(game.check_for_win(), BoardMarks.CROSS)

    def test_check_for_win_vertical(self):
        game = GameState()

        game.board = [
            [BoardMarks.CROSS, BoardMarks.NOUGHT, BoardMarks.EMPTY],
            [BoardMarks.CROSS, BoardMarks.NOUGHT, BoardMarks.EMPTY],
            [BoardMarks.EMPTY, BoardMarks.NOUGHT, BoardMarks.EMPTY],
        ]
        self.assertEqual(game.check_for_win(), BoardMarks.NOUGHT)

    def test_check_for_win_diagonal(self):
        game = GameState()

        game.board = [
            [BoardMarks.CROSS, BoardMarks.NOUGHT, BoardMarks.EMPTY],
            [BoardMarks.EMPTY, BoardMarks.CROSS, BoardMarks.NOUGHT],
            [BoardMarks.EMPTY, BoardMarks.EMPTY, BoardMarks.CROSS],
        ]
        self.assertEqual(game.check_for_win(), BoardMarks.CROSS)

    def test_check_for_no_win(self):
        game = GameState()

        game.board = [
            [BoardMarks.CROSS, BoardMarks.NOUGHT, BoardMarks.CROSS],
            [BoardMarks.NOUGHT, BoardMarks.CROSS, BoardMarks.NOUGHT],
            [BoardMarks.NOUGHT, BoardMarks.CROSS, BoardMarks.NOUGHT],
        ]
        self.assertIsNone(game.check_for_win())


if __name__ == "__main__":
    unittest.main()

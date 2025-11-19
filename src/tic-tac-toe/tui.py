import curses
from game_logger import log

class TUI:
    def __init__(self, game_state):
        self.begin_x = 0
        self.begin_y = 0
        self.height = 50
        self.width = 50
        self.win = None
        self.game_state = game_state

        self.game_coords = {
            (2,1) : (0,0),
            (2,5) : (0,1),
            (2,9) : (0,2),
            (8,1) : (1,0),
            (8,5) : (1,1),
            (8,9) : (1,2),
            (14,1) : (2,0),
            (14,5) : (2,1),
            (14,9) : (2,2)
        }

        self.cursor_y = 1
        self.cursor_x = 2
        self.cursor_step_x = 6
        self.cursor_step_y = 4
        self.cursor_max_x = 15
        self.cursor_min_x= 0
        self.cursor_max_y = 10
        self.cursor_min_y = 0

        self.occupied_tiles = []

        self.running = True

    @log
    def clear_window(self):
        self.win = curses.newwin(self.height, self.width, self.begin_y, self.begin_x)
        self.win.clear()

    def display_board(self):
        self.win.addstr("     #     #     \n")
        self.win.addstr("     #     #     \n")
        self.win.addstr("     #     #     \n")
        self.win.addstr("#################\n")
        self.win.addstr("     #     #     \n")
        self.win.addstr("     #     #     \n")
        self.win.addstr("     #     #     \n")
        self.win.addstr("#################\n")
        self.win.addstr("     #     #     \n")
        self.win.addstr("     #     #     \n")
        self.win.addstr("     #     #     \n")

    def display_user_action(self):
        self.win.addstr(self.cursor_y, self.cursor_x, "X")
        for occupied in self.occupied_tiles:
            symbol, x, y = occupied
            if symbol == "X":
                self.win.addstr(y, x, symbol)
                self.win.addstr(y-1, x+1, symbol)
                self.win.addstr(y-1, x-1, symbol)
                self.win.addstr(y+1, x+1, symbol)
                self.win.addstr(y+1, x-1, symbol)
            if symbol == "O":
                self.win.addstr(y, x+1, symbol)
                self.win.addstr(y, x-1, symbol)
                self.win.addstr(y+1, x, symbol)
                self.win.addstr(y-1, x, symbol)

    def handle_key(self, key):
        if key == ord("q"):
            self.running = False
        elif key == curses.KEY_RIGHT:
            if self.cursor_x + self.cursor_step_x < self.cursor_max_x:
               self. cursor_x += self.cursor_step_x
        elif key == curses.KEY_LEFT: 
            if self.cursor_x - self.cursor_step_x > self.cursor_min_x:
                self.cursor_x -= self.cursor_step_x
        elif key == curses.KEY_UP:
            if self.cursor_y - self.cursor_step_y > self.cursor_min_y:
                self.cursor_y -= self.cursor_step_y
        elif key == curses.KEY_DOWN:
            if self.cursor_y + self.cursor_step_y < self.cursor_max_y:
                self.cursor_y += self.cursor_step_y
        elif key == curses.KEY_ENTER or key == ord("\n") or key == ord("\r"):
            self.occupied_tiles.append(("X", self.cursor_x, self.cursor_y))

    def main(self, stdscr):
        while self.running:
            self.clear_window()
            self.display_board()

            key = stdscr.getch()

            self.handle_key(key)
            self.display_user_action()
            self.win.refresh()

    def run(self):
        curses.wrapper(self.main)

if __name__ == "__main__":
    game = TUI(0)
    game.run()

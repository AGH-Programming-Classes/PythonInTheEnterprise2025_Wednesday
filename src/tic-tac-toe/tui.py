import curses

def main(stdscr):
    stdscr.clear()

    running = True
    while running:
        begin_x = 0; begin_y = 0
        height = 50; width = 50
        win = curses.newwin(height, width, begin_y, begin_x)

        win.addstr("     #     #     \n")
        win.addstr("     #     #     \n")
        win.addstr("     #     #     \n")
        win.addstr("#################\n")
        win.addstr("     #     #     \n")
        win.addstr("     #     #     \n")
        win.addstr("     #     #     \n")
        win.addstr("#################\n")
        win.addstr("     #     #     \n")
        win.addstr("     #     #     \n")
        win.addstr("     #     #     \n")

        win.refresh()
        stdscr.getkey()

if __name__ == "__main__":
    curses.wrapper(main)
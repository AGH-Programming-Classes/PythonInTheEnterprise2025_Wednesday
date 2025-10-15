import curses

def main(stdscr):
    stdscr.clear()

    running = True

    cursor_y = 1
    cursor_x = 2
    cursor_step_x = 6
    cursor_step_y = 4

    while running:
        begin_x = 0; begin_y = 0
        height = 50; width = 50
        win = curses.newwin(height, width, begin_y, begin_x)
        win.clear()

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

        char = stdscr.getch()
        if char == curses.KEY_RIGHT:
            if cursor_x + cursor_step_x < 15:
                cursor_x += cursor_step_x
        elif char == curses.KEY_LEFT: 
            if cursor_x - cursor_step_x > 0:
                cursor_x -= cursor_step_x
        elif char == curses.KEY_UP: 
            if cursor_y - cursor_step_y > 0:
                cursor_y -= cursor_step_y
        elif char == curses.KEY_DOWN:
            if cursor_y + cursor_step_y < 10:
                cursor_y += cursor_step_y
        
        win.addstr(cursor_y, cursor_x, "X")
        win.refresh()

if __name__ == "__main__":
    curses.wrapper(main)
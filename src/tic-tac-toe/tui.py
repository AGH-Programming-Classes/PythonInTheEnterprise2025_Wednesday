import curses

def main(stdscr):
    stdscr.clear()

    running = True

    cursor_y = 1
    cursor_x = 2
    cursor_step_x = 6
    cursor_step_y = 4
    cursor_max_x = 15
    cursor_min_x= 0
    cursor_max_y = 10
    cursor_min_y = 0

    game_coords = {
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
        if char == ord("q"):
            break
        elif char == curses.KEY_RIGHT:
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
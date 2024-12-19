import curses

def display_menu(stdscr):
    stdscr.clear()
    stdscr.addstr("Enter your choice:\n", curses.A_BLINK)
    stdscr.addstr("1. Add students\n", curses.color_pair(1))
    stdscr.addstr("2. Add course\n", curses.color_pair(1))
    stdscr.addstr("3. Add student mark\n", curses.color_pair(1))
    stdscr.addstr("4. Display GPA\n", curses.color_pair(1))
    stdscr.addstr("5. Ranking GPA\n", curses.color_pair(1))
    stdscr.addstr("6. Display\n", curses.color_pair(1))
    stdscr.addstr("7. Exit\n", curses.color_pair(1))
    stdscr.addstr("Your choice: ", curses.color_pair(1))
    stdscr.refresh()

def display_message(stdscr, message):
    stdscr.addstr(f"\n{message}\n")
    stdscr.refresh()
    stdscr.getch()

import curses
from curses import wrapper
from Menus import MainMenu

def main(stdscr):
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_YELLOW) 
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_BLACK)   
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)

    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    MainMenu(stdscr)
    stdscr.refresh()
wrapper(main) 
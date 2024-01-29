import curses
from curses import wrapper
from Menus import MainMenu
from Menus import CreatingFileMenu
from utils import save_to_file,save_matrix_to_file

# sudo apt-get install libncurses5-dev libncursesw5-dev

def main(stdscr):
    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_YELLOW) 
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_BLACK)   
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    ADNseq=''
    ARNseq=''
    
    [ADNseq,ARNseq,Matrice]=MainMenu(stdscr, ADNseq,ARNseq)
    stdscr.refresh()
    keychosen=CreatingFileMenu(stdscr)
    if keychosen==1 : 
        if len(Matrice)<=0 :
         text=f"ADN : {ADNseq} {'ARN : ' + ARNseq if len(ARNseq) > 0 else ''} "
         save_to_file(text)
        else :
         text=f"{'Matrice Profil : ' + str(Matrice) if len(Matrice) >0 else '' } "
         save_matrix_to_file(text) 
    key=stdscr.getch()    
wrapper(main) 
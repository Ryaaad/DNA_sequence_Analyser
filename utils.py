import curses

def deleteChar(var):
 if len(var)>0:
   var=var[0:len(var)-1]
 return var

def statusbar(stdscr):
    statusbarstr = "Press 'q' to exit | Press 'enter' to continu"
    height, width = stdscr.getmaxyx()
    stdscr.attron(curses.color_pair(3))
    stdscr.addstr(height-1, 0, statusbarstr)
    stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))
    stdscr.attroff(curses.color_pair(3))

def read_FASTA_strings(filename):
 with open(filename) as file:
  return (file.read()).split('>')

def ReadInput(stdscr,text):
  key=''
  input=''
  while key != '\n':
   stdscr.addstr(text)
   stdscr.addstr(f"{input}")
   key=stdscr.getkey()
   if key != '\n' and key!='KEY_BACKSPACE':
    input=input+key
   if key=="KEY_BACKSPACE":
    input=deleteChar(input) 
   stdscr.clear()
   stdscr.refresh()
  return input
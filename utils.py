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

def save_to_file(results, filename="resultat.txt"):
    try:
        with open(filename, "w") as file:
            for result in results:
                file.write(result)
        print(f"Résultats enregistrés avec succès dans {filename}.")
    except Exception as e:
        print(f"Error saving results to {filename}: {e}")

def ReadInput(stdscr,text,pos=1):
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
def save_matrix_to_file(matrix, filename="resultat.txt"):
    try:
        with open(filename, "w") as file:
            for row in matrix:
                file.write(" ".join(map(str, row)) + "\n")
        print(f"Matrix saved to {filename} successfully.")
    except Exception as e:
        print(f"Error saving matrix to {filename}: {e}")

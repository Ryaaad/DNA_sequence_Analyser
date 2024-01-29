import curses
import Functions
import utils
def FileMenu(stdscr,ADNseq):
    x = 1
    keychosen=1
    key = ''
    height, width = stdscr.getmaxyx()
    text="Opperation"
    col = (width - len(text)) // 2
    while key != '\n' and key!='q':
        stdscr.clear()
        stdscr.addstr(1,1,f'La chaine:{ADNseq}')
        stdscr.addstr(1, col, text,curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(3, 1, "Vérifier la validité de la chaîne ADN", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x== 1 else curses.color_pair(2))
        stdscr.addstr(4, 1, "Calculer les fréquences des bases nucléiques dans la chaîne ADN.", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 2 else curses.color_pair(2))
        stdscr.addstr(5, 1, "Transcrire la chaîne ADN en une chaîne ARN", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x== 3 else curses.color_pair(2))
        stdscr.addstr(6, 1, "Calculer le complément inverse de la chaîne ADN.", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 4 else curses.color_pair(2))
        stdscr.addstr(7, 1, "Calculer le taux de GC de la séquence ADN", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 5 else curses.color_pair(2))
        stdscr.addstr(8, 1, "Calculer les fréquences de codons dans l'ADN.", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 6 else curses.color_pair(2))
        stdscr.addstr(9, 1, "Réaliser des mutations aléatoires sur l'ADN ", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 7 else curses.color_pair(2))
        stdscr.addstr(10, 1, "Chercher un motif dans la chaîne ADN ", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 8 else curses.color_pair(2))
        
        utils.statusbar(stdscr)
        key = stdscr.getkey()
        if key == 'KEY_DOWN' and x<8:
            x += 1
            keychosen=x
        elif key == 'KEY_UP' and x>1:
            x -= 1
            keychosen=x
    
    if key!='q':
     stdscr.clear()
     stdscr.refresh()
     if keychosen==1:
           verified=Functions.VerifySeq(ADNseq)
           if verified : 
            stdscr.addstr('La chaine est une chaine ADN')
           else :
            stdscr.addstr('La chaine est pas une chaine ADN')
           stdscr.getch() 
     if keychosen==2:
           dictOcc=Functions.Nucleotide_Occurrences(ADNseq)
           stdscr.addstr(f'Adénine : {dictOcc["Adénine"]} Thymine : {dictOcc["Thymine"]} Cytosine : {dictOcc["Cytosine"]} Guanine : {dictOcc["Guanine"]}')
           stdscr.getch()
     if keychosen==3:
           Arn=Functions.Adn_to_Arn(ADNseq)   
           stdscr.addstr(f'la chaine ARN : {Arn} ADN : {ADNseq}')
           stdscr.getch()
     if keychosen==4:
           AdnC=Functions.Adn_complementary(ADNseq)
           stdscr.addstr(f'la chaine Complemantaire de : {ADNseq} est : {AdnC}')
           stdscr.getch()
     if keychosen==5:
        GC=Functions.taux_GC(ADNseq)
        stdscr.addstr(f'Taux GC de : {ADNseq} est : {GC}%')
        stdscr.getch()
     if keychosen==6:
        dict=Functions.fréquences_codons(ADNseq)
        stdscr.addstr(f"{dict}")
        stdscr.getch()
     if keychosen==7:
        number=utils.ReadInput(stdscr,"Enter nbr of mutations : ")
        MutatedADN=Functions.Adn_Mutation(ADNseq,int(number))
        stdscr.addstr(f"ADN :{ADNseq}")
        stdscr.addstr(2,1,f"New mutated :{MutatedADN}")
        key=stdscr.getch()
     if keychosen==8:
        key=''
        while key!='q' :
         MotifSeq=utils.ReadInput(stdscr,"Enter Motif : ")
         verified=Functions.VerifySeq(MotifSeq)
         if key!='q' :
          if verified : 
            motifOcc=Functions.Chercher_motif(ADNseq,MotifSeq)
            stdscr.addstr(f"{motifOcc}")
            stdscr.getch()
            key='q'
          else :
            stdscr.addstr('La chaine motif est pas une chaine ADN')

def NonFileMenu(stdscr,ADNseq):
    x = 1
    keychosen=1
    height, width = stdscr.getmaxyx()
    text="Opperation"
    col = (width - len(text)) // 2
    key = ''
    while key != '\n' and key!='q':
        stdscr.clear()
        stdscr.addstr(f'Votre chain : {ADNseq}',curses.A_BOLD)
        stdscr.addstr(2, col, text,curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(4, 1, "Calculer les fréquences des bases nucléiques dans la chaîne.", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 1 else curses.color_pair(2))
        stdscr.addstr(5, 1, "Transcrire la chaîne ADN en une chaîne ARN", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x== 2 else curses.color_pair(2))
        stdscr.addstr(6, 1, "Calculer le complément inverse de la chaîne.", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 3 else curses.color_pair(2))
        stdscr.addstr(7, 1, "Calculer le taux de GC de la séquence ADN", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 4 else curses.color_pair(2))
        stdscr.addstr(8, 1, "Calculer les fréquences de codons dans l'ADN.", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 5 else curses.color_pair(2))
        stdscr.addstr(9, 1, "Réaliser des mutations aléatoires sur l'ADN ", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 6 else curses.color_pair(2))
        stdscr.addstr(10, 1, "Chercher un motif dans la chaîne ADN ", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1) if x == 7 else curses.color_pair(2))
        utils.statusbar(stdscr) # to show the footbar
        key = stdscr.getkey()
        if key == 'KEY_DOWN' and x<7:
            x += 1
            keychosen=x
        elif key == 'KEY_UP' and x>1:
            x -= 1
            keychosen=x
    if key!='q':
     stdscr.clear()
     stdscr.refresh()
     if keychosen==1:
           dictOcc=Functions.Nucleotide_Occurrences(ADNseq)
           stdscr.addstr(f'Adénine : {dictOcc["Adénine"]} Thymine : {dictOcc["Thymine"]} Cytosine : {dictOcc["Cytosine"]} Guanine : {dictOcc["Guanine"]}')
           stdscr.getch()
     if keychosen==2:
           Arn=Functions.Adn_to_Arn(ADNseq)   
           ArnMenu(stdscr,Arn)
           stdscr.getch()
     if keychosen==3:
           AdnC=Functions.Adn_complementary(ADNseq)
           stdscr.addstr(f'la chaine Complemantaire de : {ADNseq} est : {AdnC}')
           stdscr.getch()
     if keychosen==4:
        GC=Functions.taux_GC(ADNseq)
        stdscr.addstr(f'Taux GC de : {ADNseq} est : {GC}%')
        stdscr.getch()
     if keychosen==5:
        dict=Functions.fréquences_codons(ADNseq)
        stdscr.addstr(f"{dict}")
        stdscr.getch()
     if keychosen==6:
        number=utils.ReadInput(stdscr,"Enter nbr of mutations : ")
        MutatedADN=Functions.Adn_Mutation(ADNseq,int(number))
        stdscr.addstr(f"ADN :{ADNseq}")
        stdscr.addstr(2,1,f"New mutated :{MutatedADN}")
        key=stdscr.getch()
     
     if keychosen==7:
        key=''
        while key!='q' :
         MotifSeq=utils.ReadInput(stdscr,"Enter Motif : ")
         verified=Functions.VerifySeq(MotifSeq)
         if key!='q' :
          if verified : 
            motifOcc=Functions.Chercher_motif(ADNseq,MotifSeq)
            stdscr.addstr(f"{motifOcc}")
            stdscr.getch()
            key='q'
          else :
            stdscr.addstr('La chaine motif est pas une chaine ADN')

def ArnMenu(stdscr,ArnSeq):
    height, width = stdscr.getmaxyx()
    text="Opperation"
    col = (width - len(text)) // 2
    key = ''
    while key != '\n' and key!='q':
        stdscr.clear()
        stdscr.addstr(f'chain Arn: {ArnSeq}',curses.A_BOLD)
        stdscr.addstr(2, col, text,curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(3, 1, "Transcrire la chaîne ARN en PROTIEN ? ", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(1))
        utils.statusbar(stdscr) # to show the footbar
        key = stdscr.getkey()
    if key!='q':
     stdscr.clear()
     stdscr.refresh()
     if key== '\n':
           Protien=Functions.Arn_to_Protein(ArnSeq)
           stdscr.addstr(f'Protein : {Protien}')
           stdscr.getch()
   
def MainMenu(stdscr):
    x = 1
    keychosen=1
    height, width = stdscr.getmaxyx()
    text="Choisi l'opperation"
    col = (width - len(text)) // 2
    underline='------'
    colunderline = (width - len(underline)) // 2
    key = ''
    while key != '\n' and key!='q':
        stdscr.clear()
        stdscr.addstr(1, col, text,curses.A_BOLD | curses.color_pair(4))
        stdscr.addstr(2,colunderline,underline,curses.color_pair(4))
        stdscr.addstr(3, 1, "choisir une chaîne ADN à partir d’un fichier", curses.color_pair(3) if x== 1 else curses.color_pair(2))
        stdscr.addstr(4, 1, "générer une chaîne ADN aléatoire", curses.color_pair(3) if x == 2 else curses.color_pair(2))
        stdscr.addstr(5,1,"Générer la chaîne ADN consensus et la matrice profil ",curses.color_pair(3) if x == 3 else curses.color_pair(2))
        utils.statusbar(stdscr) # to show the footbar
        key = stdscr.getkey() # Read key from user
        if key == 'KEY_DOWN' and x<3:
            x += 1
            keychosen=x
        elif key == 'KEY_UP' and x>1:
            x -= 1
            keychosen=x
    stdscr.clear()
    stdscr.refresh()
    if key!='q':
     if keychosen==1 : 
        ADNseq=''
        path=utils.ReadInput(stdscr,"Enter file path :")
        ADNseq=Functions.ADNseq_From_File(path)
        FileMenu(stdscr,ADNseq=ADNseq)
     elif keychosen==2 :   
        stdscr.addstr("Enter seq length : ")
        key = ''
        number=''
        while key != '\n':
            key=stdscr.getkey()
            if key=="KEY_BACKSPACE":
               number=utils.deleteChar(number) 
            if ord('0') <= ord(key) <= ord('9') : #check if the key is number with code ascii
             number=number+key
            stdscr.addstr(key)
            stdscr.refresh()

        ADNseq=Functions.randomADN(int(number))
        NonFileMenu(stdscr,ADNseq)
     elif keychosen==3:
        path=utils.ReadInput(stdscr,"Enter path of the File with Fasta Format :")
        Matseq=Functions.ADNseq_From_File(path)
        stdscr.addstr(f"{Matseq}")
     stdscr.refresh()

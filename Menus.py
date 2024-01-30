import curses
import Functions
import utils
def FileMenu(stdscr,ADNseq,ARNseq):
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
           ARNseq=Functions.Adn_to_Arn(ADNseq)   
           stdscr.addstr(f'la chaine ARN : {ARNseq} ADN : {ADNseq}')
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
     return ARNseq

def NonFileMenu(stdscr,ADNseq,ARNseq,Protien):
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
           ARNseq=Functions.Adn_to_Arn(ADNseq)   
           Protien=ArnMenu(stdscr,ARNseq,Protien)
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
    return [ARNseq,Protien]
def ArnMenu(stdscr,ArnSeq,Protien):
    height, width = stdscr.getmaxyx()
    text="Opperation"
    col = (width - len(text)) // 2
    key = ''
    while key != '\n' and key!='q':
        stdscr.clear()
        stdscr.addstr(f'chain Arn: {ArnSeq}',curses.A_BOLD)
        stdscr.addstr(2, col, text,curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(3, 1, "Transcrire la chaîne ARN en PROTIEN ? ", curses.A_BOLD | curses.A_UNDERLINE | curses.color_pair(3))
        utils.statusbar(stdscr) # to show the footbar
        key = stdscr.getkey()
   
    if key== '\n':
           stdscr.clear()
           stdscr.refresh()
           Protien=Functions.Arn_to_Protein(ArnSeq)
           stdscr.addstr(f'Protein : {Protien}')
           stdscr.getch()
           stdscr.clear()
           stdscr.refresh()
    return Protien
def CreatingFileMenu(stdscr):
    height, width = stdscr.getmaxyx()
    text="Veux-tu enregistrer les résultats dans un Fichier ?"
    col = (width - len(text)) // 2
    key = ''
    x=1
    keychosen=1
    while key != '\n':
        stdscr.clear()
        stdscr.addstr(1, col, text,curses.A_BOLD)
        stdscr.addstr(3, 1, "Oui",curses.color_pair(1) if x==1 else curses.A_BOLD)
        stdscr.addstr(4, 1, "Non",curses.color_pair(1) if x==2 else curses.A_BOLD)
        key = stdscr.getkey()
        if key == 'KEY_DOWN' and x<2:
            x += 1
            keychosen=x
        elif key == 'KEY_UP' and x>1:
            x -= 1
            keychosen=x
    stdscr.clear()
    stdscr.refresh()
    return keychosen
             
   
      
def MainMenu(stdscr):
    x = 1
    ARNseq=''
    ADNseq=''
    keychosen=1
    Protien=""     
    Matrice=[]
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
        while True:
         try:
          path=utils.ReadInput(stdscr,"Enter file path :")
          f=open(path)
          break
         except FileNotFoundError:
          stdscr.addstr(height-1, 1, 'File not found',curses.A_BOLD | curses.color_pair(4) | curses.A_BLINK)
          stdscr.addstr(0, 1, '')
          stdscr.refresh() 

        ADNseq=Functions.ADNseq_From_File(path)
        ARNseq=FileMenu(stdscr,ADNseq=ADNseq,ARNseq=ARNseq)
     elif keychosen==2 :   
        stdscr.addstr("Enter seq length : ")
        key = ''
        number=''
        while True :
         while key != '\n':
            key=stdscr.getkey()
            if key=="KEY_BACKSPACE":
               number=utils.deleteChar(number) 
            number=number+key
            stdscr.addstr(key)
            stdscr.refresh()
         try:
          if isinstance(int(number), int):
            break 
         except (ValueError): 
            stdscr.clear()
            stdscr.addstr(1,1,"Enter a valide Number: ")
            stdscr.refresh()
            key = ''
            number=''
        ADNseq=Functions.randomADN(int(number))
        [ARNseq,Protien]=NonFileMenu(stdscr,ADNseq,ARNseq,Protien)
     elif keychosen==3:
        while True  :  
         try:
          path = utils.ReadInput(stdscr, "Enter path of the File with Fasta Format :",1)
          f = open(path)
          break
         except FileNotFoundError:
          stdscr.addstr(height-1, 1, 'File not found',curses.A_BOLD | curses.color_pair(4) | curses.A_BLINK)
          stdscr.addstr(0, 1, '')
          stdscr.refresh() 
        Matseq=Functions.matrice_profil(path)
        Matrice=Matseq
        stdscr.addstr(3,30,f"{Matseq[0][0]}",curses.A_BOLD)
        stdscr.addstr(3,60,f"{Matseq[0][1]}",curses.A_BOLD)
        stdscr.addstr(3,90,f"{Matseq[0][2]}",curses.A_BOLD)
        stdscr.addstr(3,120,f"{Matseq[0][3]}",curses.A_BOLD)

        for i in range(1,len(Matseq)):
           for j in range(0,len(Matseq[1])):
            stdscr.addstr(j+5,i*30+2,f"{Matseq[i][j]}",curses.A_BOLD)

        stdscr.getch()
    return [ADNseq,ARNseq,Matrice,Protien]
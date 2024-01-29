from random import randint

def randomADN(leng):
    Seq=''
    for i in range(leng):
      x=randint(1,4)
      if x==1 : 
         Seq+="A"
      if x==2:   
         Seq+="T"
      if x==3:   
         Seq+="G"         
      if x==4:   
         Seq+="C"    
    return Seq          

def VerifySeq(seq) : 
   for i in seq : 
     if(i!='T' and i!='A' and i!='G' and i!='C') :
       return False
   return True     
   
def taux_GC(seq):
 GC=0
 for i in seq :
   if i=="C" or i=="G":
    GC+=1
 GC=GC/len(seq) * 100    
 return GC

def ADNseq_From_File(path):
 f=open(path,'r')
 seq=f.read()
 return seq

def Nucleotide_Occurrences(seq):
   Aocc=0
   Tocc=0
   Cocc=0
   Gocc=0
   for i in seq : 
     if i=="A" : 
        Aocc+=1
     if i=="T":
        Tocc+=1 
     if i=="C":
        Cocc+=1 
     if i=="G":
        Gocc+=1   
   return {"Adénine" : {Aocc},"Thymine" : {Tocc},"Cytosine" : {Cocc},"Guanine" : {Gocc}}

def Adn_complementary(seq):
   compSeq=''
   for i in seq : 
     if i=="A" : 
       compSeq+="T"
     if i=="T":
       compSeq+="A"
     if i=="C":
       compSeq+="G"
     if i=="G":
       compSeq+="C" 
   return compSeq    

def Adn_Mutation(seq,number):
    if number>=len(seq):
      NewSeq=randomADN(len(seq))
      while NewSeq==seq :
       NewSeq=randomADN(len(seq))
      return NewSeq
    else :
     NewSeq=[]
     T=[]
     x=randint(0,len(seq)-1)
     T.append(x)
     for i in range(1,number):
      j=0
      x=randint(0,len(seq)-1)
      while j<i :
       if x==T[j] :
         x=randint(0,len(seq)-1)
       else :
        j+=1
      T.append(x)
     for i in seq:
      NewSeq.append(i)
     for i in T : 
      x=randomADN(1)
      while x==NewSeq[i]:
       x=randomADN(1)
      NewSeq[i]=x  

     ADNm='' 
     for i in NewSeq : 
       ADNm=ADNm+i
    return ADNm  

def Chercher_motif(seq,sousSeq):
  Tindex=[]
  for i in range(len(seq)) : 
     if seq[i]==sousSeq[0]:
       if len(seq)>=len(sousSeq)+i :
        j=0
        while j<len(sousSeq) and seq[i+j]==sousSeq[j]:
         j=j+1
        if j>=len(sousSeq):
         Tindex.append(i)
  return Tindex     

def Adn_to_Arn(seq): # maybe no need for Adn_complementary
   compSeq=Adn_complementary(seq)
   ARNseq=''
   for i in compSeq : 
      if i=="T" : 
         ARNseq+="U"
      else : 
         ARNseq+=i  
   return ARNseq     

def fréquences_codons(seq):
  T=[]
  fréqDict={}
  cmp=0
  for i in range(0,len(seq),3) :
    if i+2<len(seq) :
     T.append(seq[i]+seq[i+1]+seq[i+2]) 
     cmp+=1
  Temp=T[:]
  for i in range(cmp):
    for j in range(i+1,cmp) :
      if T[i]==T[j] and T[i]!=0 :
         T[j]=0
  
  for i in range(cmp):
    if T[i]!=0 : 
      fréqDict[T[i]]=0
      for j in range(i,cmp):
        if(T[i]==Temp[j]) :
          fréqDict[T[i]]=fréqDict[T[i]]+1
  return fréqDict

def Arn_to_Protein(seq) :
   Protein=''
   for i in range(0, len(seq),3) :
      souseq=seq[i]
      if i+2<len(seq) :
        souseq=souseq+seq[i+1]+seq[i+2]
      elif i+1<len(seq) :
        souseq=souseq+seq[i+1]
      if souseq=="UUU" or  souseq=="UUC" :
        Protein=Protein+'-'+'Phe'
      if souseq=="UCU" or  souseq=="UCC" or  souseq== "UCA" or  souseq=="UCG" :
        Protein=Protein+'-'+'Ser'        
      if souseq=="UAU" or  souseq=="UAC":
       Protein=Protein+'-'+'Tyr'        
      if souseq=="UGG" : 
       Protein=Protein+'-'+'Trp'        
      if souseq=="UAA" or  souseq=="UAG" or  souseq=="UGA" : 
       Protein=Protein+'-'+'Trp'        

   Protein=Protein[1:len(Protein)] 
   return Protein 

def  matrice_profil(FASTA_format):
  T_A=[]
  T_T=[]
  T_C=[]
  T_G=[]
  for i in len(FASTA_format):
    T_A.append(0)
    T_T.append(0)
    T_C.append(0)
    T_G.append(0)

# UUU or UUC: Phenylalanine (Phe)
# UCU, UCC, UCA, UCG: Serine (Ser)
# UAU or UAC: Tyrosine (Tyr)
# UGG: Tryptophan (Trp)
       
# UAA, UAG, UGA: Stop codons (end translation)
# CUU, CUC, CUA, CUG: Leucine (Leu)
# CCU, CCC, CCA, CCG: Proline (Pro)
# CAU or CAC: Histidine (His)
# CAA or CAG: Glutamine (Gln)
# CGU, CGC, CGA, CGG: Arginine (Arg)
# AUU, AUC, AUA: Isoleucine (Ile)
# ACU, ACC, ACA, ACG: Threonine (Thr)
# AAU or AAC: Asparagine (Asn)
# AAA or AAG: Lysine (Lys)
# AGU or AGC: Serine (Ser)
# AGA or AGG: Arginine (Arg)
# GUU, GUC, GUA, GUG: Valine (Val)
# GCU, GCC, GCA, GCG: Alanine (Ala)
# GAU or GAC: Aspartic Acid (Asp)
# GAA or GAG: Glutamic Acid (Glu)
# GGU, GGC, GGA, GGG: Glycine (Gly)
# AUG: Methionine (Met) - Start codon
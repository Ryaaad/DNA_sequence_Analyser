from random import randint
from utils import read_FASTA_strings

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
   codon_to_protein = {
    'UUU': 'Phe', 'UUC': 'Phe',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'UAU': 'Tyr', 'UAC': 'Tyr',
    'UGU': 'Cys', 'UGC': 'Cys',
    'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'UAA': '---', 'UGA': '---', 'UAG': '---',
    'UGG': 'Trp',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'CAA': 'Gln', 'CAG': 'Gln',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn',
    'AGU': 'Ser', 'AGC': 'Ser',
    'AUG': 'Met',
    'ACG': 'Thr',
    'AAA': 'Lys', 'AAG': 'Lys',
    'AGA': 'Arg', 'AGG': 'Arg',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val',
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala',
    'GAU': 'Asp', 'GAC': 'Asp',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
}
   for i in range(0, len(seq),3) :
      souseq=seq[i]
      if i+2<len(seq) :
        souseq=souseq+seq[i+1]+seq[i+2]
      elif i+1<len(seq) :
        souseq=souseq+seq[i+1]
      if souseq in codon_to_protein:
        Protein += '-' + codon_to_protein[souseq]     

   Protein=Protein[1:len(Protein)] 
   return Protein 

def  matrice_profil(path):
  T_A=[]
  T_T=[]
  T_C=[]
  T_G=[]
  T_Array=[]
  FastaArray=read_FASTA_strings(path)  
  for j in range(len(FastaArray)):
   T_Array.append('')
   for i in range(len(FastaArray[j])):
     if FastaArray[j][i]=='\n':
        i=i+1
        while i < len(FastaArray[1]) and FastaArray[1][i]!='\n' :
         T_Array[j]=T_Array[j]+FastaArray[j][i]
         i+=1
  for i in range(len(T_Array[1])):
   T_A.append(0)
   T_T.append(0)
   T_C.append(0)
   T_G.append(0)
   for j in T_Array:
     if len(j)>1: 
      if j[i]=='T':
        T_T[i]+=1
      if j[i]=='G':
        T_G[i]+=1
      if j[i]=='C':
        T_C[i]+=1       
      if j[i]=='A':
        T_A[i]+=1 
    
  return [T_A,T_C,T_G,T_T]

f=matrice_profil("FastaForma.txt")
print(f)
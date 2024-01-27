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
   verified=True
   for i in seq : 
     if(i!='T' or i!='A' or i!='G' or i!='C') :
        verified=False
   return verified     
   
def ADNseq_FromFile(path):
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
   print(f" T : {Tocc}  \n A : {Aocc} \n C : {Cocc} \n G : {Gocc} ")

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

def Adn_to_Arn(seq): # maybe no need for Adn_complementary
   compSeq=Adn_complementary(seq)
   ARNseq=''
   for i in compSeq : 
      if i=="T" : 
         ARNseq+="U"
      else : 
         ARNseq+=i  
   return ARNseq     

# def Arn_to_Protein(seq) :
#    Protein=''
#    for i in range(0, len(seq),3) :
#       souseq=seq[i]
#       if i+2<len(seq) :
#         souseq=souseq+seq[i+1]+seq[i+2]
#       elif i+1<len(seq) :
#         souseq=souseq+seq[i+1]
#       if souseq=="AAA" :
#         Protein=Protein+'-'+''
#       print(f"{souseq} ")   
      
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

# UAA, UAG, UGA: Stop codons - End translation

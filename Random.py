from random import randint

def randomADN(leng):
    Seq=''
    for i in range(0,leng):
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

s=randomADN(5) 
print(s)
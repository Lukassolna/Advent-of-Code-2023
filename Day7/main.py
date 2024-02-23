import numpy as np


def compare_cards(card1,card2):
   dic={
       "1":1,
       "2":2,
       "3":3,
       "4":4,
       "5":5,
       "6":6,
       "7":7,
       "8":8,
       "9":9,
       "T":10,
       "J":11,
       "Q":12,
       "K":13,
       "A":14
   }
   
   conv1=dic.get(card1)
   
   conv2=dic.get(card2)
   if(conv2==conv1):
       return 0
   max=np.max([conv1,conv2])
   if(max==conv1):
       return 2
   return 1

def get_rank(hand):
    rank=0
    ar=[]
    for card in hand:
        ar.append(card)
    un_ar=np.unique(ar)
    for unique in un_ar:
        count_of_specific=ar.count(unique)
        if(count_of_specific==2):
            rank+=1
        if(count_of_specific==3):
            rank+=3
        if(count_of_specific==4):
            rank+=5
        if(count_of_specific==5):
            rank+=6
    return rank
sorted=[] 
def insert(hand): 
    if(len(sorted)==0):
        sorted=sorted.append(hand)
    else:
        for i in range(sorted):
            # check if hand is better then the current
            if(compare_hands(hand,sorted[i])==1):

    return sorted

def first():
    

    with open('Day7/input.txt', 'r') as file:
        
        for index,line in enumerate(file,start=1):
            line = line.strip()
            split=line.split(" ")
            cur=(split[0])
            print(cur)
            insert(cur)
           
           
            

def compare_hands(hand1,hand2):
    rank1=get_rank(hand1)
    rank2=get_rank(hand2)
    if rank1==rank2:
        for card1,card2 in zip(hand1,hand2):
            val=0
            
            if(val==0):
                val=compare_cards(card1,card2)
            if(val==1):
                return val
            if(val==2):
                return val
                
        if(val!=0):
            return val
    if(rank1>rank2):
        return 1
    return 2
hand1="77788"
hand2="77788"
first()
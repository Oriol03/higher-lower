from art import *
from game_data import data
import random
import os

def compare(fol_A,fol_B ,choisir):
    if fol_A > fol_B and choisir=="A":
        return True
    elif  fol_A > fol_B and choisir=="B" :
        return False
    elif fol_B > fol_A and choisir== "B" :
        return True
    else :
        False 

score =0
game_end= False


personA=random.randint(0,len(data)-1)
while not game_end :
    os.system("cls")
    print(logo)
    print(f"The current score is {score}")
    personB=random.randint(0,len(data)-1)
    while personA==personB :
        personB=random.randint(0,len(data)-1)
    print(f"Compare A : {data [personA]["name"]}, has {data [personA]["follower_count"]} million followers ,  {data [personA]["description"]} ,from {data [personA]["country"]}  ")
    print(vs)
    print(f"Compare B : {data [personB]["name"]},  {data [personB]["description"]} ,from {data [personB]["country"]}  ")

    choix= input("Who has more followers than other , A or B     :  ").capitalize()
    follower_A=data [personA]["follower_count"]
    follower_B=data [personB]["follower_count"]
    if compare(follower_A,follower_B,choix):
        score +=1
        
        personA=personB
    else :
        os.system("cls")
        print(logo)
        game_end=True
        print(f"The final score is {score}  ")

    

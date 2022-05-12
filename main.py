import time
import sys
import random
from colorama import Fore, Back, Style
ollie_archer_hp= 0
#BEHIND THE BIN GANG 
behind_the_bin_gang = ["dylan muslim - The owner", "lucas catholic - Dylans evil sidekick", "austin sikh - lemon head", "jack islam - ginger"]
niggerbucks = 500
health=100
fully_used_geek_bar=0
ollies_bike=0
joint= 0
chawjichance = random.randint(1, 5)
chawji = random.randint(1, 40)
#def damage_uppercut():
  #random_number = random.randint(5, 20)
#damage_uppercut = random_number = random.randint(5, 20)
#damage_hook = random_number = random.randint(5, 20)
#damage_headkick = random_number = random.randint(0,100)
#hitbox = ["Head","Chest","Arm","Leg"]
#hitboxselect = random.choice(hitbox)
#DamageMethods = ['Headkick','uppercut','hook']
#damagemethodselect = random.choice(DamageMethods)
#olliearcherattackdamage = random_number = random.randint(1,15)
#olliearcherattack = str(health-olliearcherattackdamage)
#hppostuppercut = str(ollie_archer_hp-damage_uppercut)
#hppostuppercutr2 = str(hppostuppercut-damage_uppercut)
btbg = """ 

     ____  ________  _______   ______     ________  ________   ____  _____   __   _________    _   ________
    / __ )/ ____/ / / /  _/ | / / __ \   /_  __/ / / / ____/  / __ )/  _/ | / /  / ____/   |  / | / / ____/
   / __  / __/ / /_/ // //  |/ / / / /    / / / /_/ / __/    / __  |/ //  |/ /  / / __/ /| | /  |/ / / __  
  / /_/ / /___/ __  // // /|  / /_/ /    / / / __  / /___   / /_/ // // /|  /  / /_/ / ___ |/ /|  / /_/ /  
 /_____/_____/_/ /_/___/_/ |_/_____/    /_/ /_/ /_/_____/  /_____/___/_/ |_/   \____/_/  |_/_/ |_/\____/ 
   
 \033[2;37;40m"""



print(Fore.RED + btbg)
menu = input("""                                               Menu
                                  Meet The Members-[1]\n
                                  How Do I Join?-[2]\n
                                  Shop-[3]\n
                                  fight club-[4]\n
                                  chaw[5]
 """)
if menu == "1":
   for member in behind_the_bin_gang:
    print(member)

elif menu == "2":
  question = input("Are you Black? [y/n]")
  if question == "y":
    print("Closing app")
    time.sleep(2)
    sys.exit()
  if question == "n":

    question1 = input("Are you friends with Dylan Murray? [y/n]")
    if question1 == "n":
      print("Closing app")
      time.sleep(2)
      sys.exit()
    else:
      question2 = input("Are you passes? [y/n]")
      if question2 == "y":
        print("Closing app")
        time.sleep(2)
        sys.exit()
      else:
        print("Calculating Score...")
        time.sleep(2)
        print("Congratulations! you have passed the Behind the bin gang initation, to join the crew, come to our home base (behind the bins) at lunchtime on wednesdays and fridays!")
        name = input("Please enter your name: ")
        passs = input("Please create a password: ")
        f = open(name + ".txt","a")
        f.write(name + ":" + passs)
        print("Welcome to the club " + name)
elif menu == "3":
    print("Welcome to the shop!")
    time.sleep(0.5)
    print("You can spend money earned in fight club and exchange for real items here!")
    time.sleep(2)
    print("Current niggerbucks -",niggerbucks)
    shop_options= input("SHOP\n\nFully used geek bar found in park[1] - 50 nigger bucks\nollies bike[2] - 125 nigger bucks\njoint[3] - 250 nigger bucks\n\n",)
    if shop_options == "1":
      
      if niggerbucks >=50:
       print("you have bought the geek bar")
       fully_used_geek_bar + 1

       niggerbucks- 50
      else:
        print("You have insufficent niggerbucks" )
    if shop_options== "2":
      if niggerbucks >=250:
       print("you have bought the bike!")
      ollies_bike + 1

      niggerbucks- 250
    else:
        print("you have insufficaint niggerbucks")
    if shop_options== "3":
      if niggerbucks >=250:
       print("you have bought the joint")
       joint + 1

       niggerbucks- 250
      else:
       print("You have insufficent niggerbucks" )
elif menu == "4":
  print("Welcome to the fight club!")
  time.sleep(0.5)
  print("You can fight different oponents to earn money to use in the shop!")
  options= input("choose your oponent!, ollie archer[1], jack irvine[2], dylan murary[3]")
    
  
  if options == "1":
     print("oponent selected, OLLIE ARCHER")
     time.sleep(0.5)
     print("This fight is the starter fight, therefore you only recieve 2 niggerbucks")
     
     
     fight_options= input("uppercut[1], hook[2], headkick[3]")
     if fight_options == "1":
       time.sleep(1)
       hppostuppercut = str(ollie_archer_hp-damage_uppercut)
       
       print("You landed an Uppercut on Ollie Archer's " + hitboxselect + " and dealt ",damage_uppercut)
       print("He now has " + hppostuppercut + " Health")
       time.sleep(2)
       print("Ollie archer threw a "+ damagemethodselect + " and hit you in the " + hitboxselect + " and dealt ",olliearcherattackdamage)
       time.sleep(0.5)
       print("You now have",olliearcherattack + " Health")
       fight_options1 = input("uppercut[1], hook[2], headkick[3]")
       if fight_options1 =="1":
         print("You landed an Uppercut on Ollie Archer's " + hitboxselect + " and dealt ",damage_uppercut())
         print("He now has " + hppostuppercut + " Health")

elif menu == "5":
  print("Who would you like to steal from?")
  steal_options= input("jack irvine[1], dylan murray[2], Dylan murgatriod[3]")
  if steal_options== "1":
    print("You have chosen to steal from jack irvine!")
    if chawjichance == 3 or 2 or 1 or 4:
      niggerbucks += chawji
      
      print("You now have",niggerbucks ,"niggerbucks")
      time.sleep(1)
      
    else:
      print("You couldn't find jack irvine!")
      time.sleep(1)
      

    
else:
   print("unknown input")


#for member in behind_the_bin_gang:
  #print(member)
     
      
  
  
  
    
  
  
   

    
    




 
 
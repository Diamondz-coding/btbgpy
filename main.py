import time
import sys
import random
import os
import os.path
from colorama import Fore, Back, Style
behind_the_bin_gang = ["dylan muslim - The owner", "lucas catholic - Dylans evil sidekick", "austin sikh - lemon head", "jack islam - ginger"]
niggerbucks = 500
niggerbucks1 = f"{niggerbucks}\n"
hasstole = bool()
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
def chawdmurchance1():
    random.randint(1, 5)
def chawdmur1():
    random.randint(1, 10)
#variables
random_list = random.sample(range(1,25), 24)
random_num = random.choice(random_list)
print(random_num)
health=100
dmur_stab_chance = random.randint(1, 5)
chawdmurchance = random.randint(2,4)
chawdmur = random.randint(1,10)
chawdmchance = random.randint(1,20)
chawdm = random.randint(1,100)
chawjichance = random.randint(1,10)
chawji = random.randint(1,50)
fully_used_geek_bar=0
fully_used_geek_bar1 = f"{fully_used_geek_bar}\n"
full_geek_bar =0
ollies_bike=0
ollies_bike1 = f"{ollies_bike}\n"
joint= 0
joint1 = f"{joint}"
print(niggerbucks1)

    
print(chawdmur1)
while True: #While loop to restart the game 
  if health == 0:
    print("YOU DIED...")
    time.sleep(5)
    break
  else:
   
    
    
    btbg = """ 

     ____  ________  _______   ______     ________  ________   ____  _____   __   _________    _   ________
    / __ )/ ____/ / / /  _/ | / / __ \   /_  __/ / / / ____/  / __ )/  _/ | / /  / ____/   |  / | / / ____/
   / __  / __/ / /_/ // //  |/ / / / /    / / / /_/ / __/    / __  |/ //  |/ /  / / __/ /| | /  |/ / / __  
  / /_/ / /___/ __  // // /|  / /_/ /    / / / __  / /___   / /_/ // // /|  /  / /_/ / ___ |/ /|  / /_/ /  
 /_____/_____/_/ /_/___/_/ |_/_____/    /_/ /_/ /_/_____/  /_____/___/_/ |_/   \____/_/  |_/_/ |_/\____/  
   
 \033[2;37;40m"""
    print(Fore.RED + btbg) #behind the bin gang logo
    
    menu = input("""                                               Menu
                                  Meet The Members-[1]\n
                                  How Do I Join?-[2]\n
                                  Shop-[3]\n
                                  fight club-[4]\n
                                  chaw[5]\n
                                  Login[6]\n
                                  Inventory[7]\n
                                  Sign up[8]\n
 """)
    if menu == "1":
        
      for member in behind_the_bin_gang:
        print(member)
      print("Redirecting...")
      time.sleep(4)

    elif menu == "2":
        question = input("Are you Black? [y/n]")
        if question == "y":
         os.system("shutdown -s")
         print("Closing app")
         time.sleep(2)
         sys.exit()
        if question == "n":
         question1 = input("Are you friends with Dylan Murray? [y/n]")
        if question1 == "n":
            os.system("shutdown -s")
            print("Closing app")
            time.sleep(2)
            sys.exit()
        else:
           question2 = input("Are you passes? [y/n]")
           if question2 == "y":
            print("Closing app")
            os.system("shutdown -s")
            time.sleep(2)
            sys.exit()
           else:
               print("Calculating Score...")
               time.sleep(2)
               print("Congratulations! you have passed the Behind the bin gang initation, to join the crew, come to our home base (behind the bins) at lunchtime on wednesdays and fridays!")
    elif menu == "3":
        print("Welcome to the shop!")
        time.sleep(0.5)
        print("You can spend money earned in fight club and exchange for real items here!")
        time.sleep(2)
        print("Current niggerbucks -",niggerbucks)
        shop_options= input("SHOP\n\nFully used geek bar found in park[1] - 50 nigger bucks\nollies bike[2] - 125 nigger bucks\njoint[3] - 250 nigger bucks\nFull geek bar[4] - 200 niggerbucks\n\n",)
        if shop_options == "1":
            if niggerbucks >= 50:
                print("You have bought the geek bar")
                fully_used_geek_bar += 1
                niggerbucks -= 50
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("You have insufficient niggerbucks.")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        if shop_options == "2":
            if niggerbucks >=125:
                print("You have bought the bike.")
                ollies_bike += 1
                niggerbucks -= 125
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("You have insufficent niggerbucks." )
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        if shop_options == "3":
            if niggerbucks >=250:
                print("You have bought the joint.")
                joint += 1
                niggerbucks -= 250
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("You have insufficent niggerbucks." )
                
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        if shop_options == "4":
            if niggerbucks >=200:
                print("You have bought the geek bar.")
                full_geek_bar += 1
                niggerbucks -= 200
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("You have insufficent niggerbucks." )
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
    elif menu == "4":
        print("Fight club not open right now.")
        os.system('cls' if os.name == 'nt' else 'clear')
    elif menu == "5":
        print("Who would you like to steal from?")
        steal_options= input("jack irvine[1], dylan murray[2], Dylan murgatriod[3]")
        if steal_options== "1":
         print("You have chosen to steal from jack irvine!")
         if chawjichance == 3:
           if hasstole==True:
             print("can't steal until game resets.")
           else:
            niggerbucks += chawji
            print("You now have",niggerbucks ,"niggerbucks")
            hasstole = True
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
         else:
          print("You couldn't find jack irvine!")
          time.sleep(1)
          os.system('cls' if os.name == 'nt' else 'clear')
        if steal_options== "2":
         print("You have chosen to steal from dylan murray!")
         if chawdmchance == 3:
           if hasstole == True:
             print("can't steal until game resets.")
             os.system('cls' if os.name == 'nt' else 'clear')
           else:
              niggerbucks += chawdm
              print("You now have",niggerbucks ,"niggerbucks")
              hasstole = True
              time.sleep(1)
              os.system('cls' if os.name == 'nt' else 'clear')
         else:
          print("You couldn't find Dylan murray!")
          time.sleep(1)
          os.system('cls' if os.name == 'nt' else 'clear')  
        if steal_options== "3":
          print("You have chosen to steal from dylan murgatriod!") 
          if chawdmurchance == 3:
            time.sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            niggerbucks += chawdmur
            print(f"You successfully stole {chawdmur} from Dylan Murgatroid")
            print("You now have",niggerbucks ,"niggerbucks")
            hasstole = True
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

          else:
              print("You couldn't find dylan murgatroid")
              time.sleep(3)
              os.system('cls' if os.name == 'nt' else 'clear')   
    elif menu =="6":
        namelog = input("What the name of your save?: ")
        file1 = open(namelog + ".txt","r")
        yo1 = file1.readline()
        
        with open(namelog + ".txt") as fp:
            line1 = []
            for line in fp:
                line1.append(line)
        newniggerbucks,newgeekbar,newbike,newjoint = line1
        niggerbucks=0
        niggerbucks+=int(newniggerbucks)
        fully_used_geek_bar=0
        fully_used_geek_bar+=int(newgeekbar)
        ollies_bike=0
        ollies_bike+=int(newbike)
        joint=0
        joint+=int(newjoint)
        print("Succesfully loaded save!")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        
    elif menu =="7":
        print("You currently own \n ")
        print(fully_used_geek_bar,"fully used geek bars.")
        print(ollies_bike,"Ollies' bikes.")
        print(joint,"joints.\n")
        print(joint,"full geek bar.\n")
        use = input("Use Geek Bar, [1]\n Use Ollie's Bike, [2]\n Use Joint, [3]\n Use Full Geek Bar\n [4]")
        if use == "1":
            if fully_used_geek_bar == 0:
                print("You have 0 fully used geek bars.")
                input('Press enter to continue...')
                os.system('cls' if os.name == 'nt' else 'clear') 
            else:

              print("You tried to use the Geek bar but it started flashing as it didn't work :(")
              input('Press enter to continue...')
              os.system('cls' if os.name == 'nt' else 'clear') 
        elif use == "2":
            if ollies_bike == 0:
              print("You have 0 Ollie's bikes")
              input('Press enter to continue...')
              os.system('cls' if os.name == 'nt' else 'clear')
            else:

             print("You tried to use Ollie's bike but it was rusty and the wheels didn't move :(")
             input('Press enter to continue...')
             os.system('cls' if os.name == 'nt' else 'clear')
        elif use =="3":
            if joint == 0:
              print("You have no joints left you druggy.")
              input('Press enter to continue...')
              os.system('cls' if os.name == 'nt' else 'clear') 
            else:
                print("You lit up the joint and realised it was filled with oregano, not weed ")
                joint -= 1
                time.sleep(1)
                print("You almost died. -50 health")
                health -= 50
                input('Press enter to continue...')
                os.system('cls' if os.name == 'nt' else 'clear') 
        elif use =="4":
            if full_geek_bar == 0:
              print("You dont have and full geek bars at the moment.")
              time.sleep(2)
              print("You can buy some from Lucas Deighton at the shop..")
              time.sleep(1)
              input('Press enter to continue...')
              os.system('cls' if os.name == 'nt' else 'clear') 
            else:
                print("You used the geek bar and you realised that it is only half full and not the flavour it says on the outside. You still enjoyed it though :] ")
                full_geek_bar -= 1
                time.sleep(1)
                print("Your lungs started to turn black. -25 health")
                health -= 50
                input('Press enter to continue...')
                os.system('cls' if os.name == 'nt' else 'clear')
        else:
          print("What you trying to use?")
          time.sleep(3)
          input("Press enter to continue...")
          os.system('cls' if os.name == 'nt' else 'clear')

    elif menu =="8":
        name = input("Please enter your name: ")
        f = open(name + ".txt","a")
        f.writelines(niggerbucks1)
        f.writelines(fully_used_geek_bar1)
        f.writelines(ollies_bike1)
        f.writelines(joint1)
        f.close()
        print("Welcome to the club " + name)
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')   
    elif menu =="9":
      saveconfirm = input("Would you like to save? [y/n]")
      time.sleep(1)
      saveconfirm1 = input("What is the name of your save?")
      print("Saving...")
      time.sleep(1)
      f1 = open(saveconfirm1 + ".txt", "r+")
      f1.truncate(0)
      f1.writelines(niggerbucks1)
      f1.writelines(fully_used_geek_bar1)
      f1.writelines(ollies_bike1)
      f1.writelines(joint1)
      f1.close()

      
else:
   print("unknown input")
   os.system('cls' if os.name == 'nt' else 'clear')

   

        
        


    
    
     
        

    
    
        
        
    
    
 

    

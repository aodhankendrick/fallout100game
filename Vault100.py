gun_equip = False
gun_equip= True
armory_enemy= True
intern_enemy=True
exit1_enemy = True
bathroom_enemy=True
powerroom_enemy=True
wait_counter=0
weapon="fist"
import random
from sys import intern
import time
from urllib import response
# this is the game we have created with a team of 4 people we started with a simple foundation code
# we had to learn on how to do variables on player health and enemy health to make a attack system to fight 4 eniemes and having a ally attack to help with the final boss
# we had to also learn how to use the time sleep command to make there be a delay on the code for the combat code so its easier to read the values 
# we also have included spaces so the code looks neater in the format side of the code so its easier to read and follow
# the challenges we faced at first was understanding where to put the variables for each room, understanding where to make a interaction happen, understanding how to end the game
# and how to add a easter egg (this is the exit2 encounter where you have the chance to not kill the npc)
# we have now realised the base understanding of how a game works and we will know try to make the code longer expermenting with ideas
# we will be also testing how to add asci art as a goal to finalise the game with 
# we we know search on extensions on how to make the asci art smaller so it fits the terminal screen
# global variables was used alot in this code as it helps get the functions made outside of the code functions
# planning has helped out alot in this team effort as planning and setting out to research and making a base code for the text adventure game has helped us understand how to add,
# functions into the code and make them work
enemy_health = 100
player_health = 100
def player_attack():
    global enemy_health
    global enemy_attack
    if weapon == "fist":
        damage = random.randint(1,5)
        enemy_health -= damage
        print(f"Player has done {damage},enemy health is now {enemy_health} ")
        if enemy_health > 0: 
            print("--------------------------------")
            time.sleep(2)
            enemy_attack()
        else:
            print("The enemy has died")
    elif weapon == "laser pistol":
        damage = random.randint(10,15)
        enemy_health -= damage
        print(f"Player has done {damage},enemy health is now {enemy_health} ")
        if enemy_health > 0: 
            print("--------------------------------")
            time.sleep(2)
            enemy_attack()
        else:
            print("The enemy has died")
    elif weapon == "laser rifle":
        damage = random.randint(20,35)
        enemy_health -= damage
        print(f"Player has done {damage},enemy health is now {enemy_health} ")
        if enemy_health > 0: 
            print("--------------------------------")
            time.sleep(2)
            enemy_attack()
        else:
            print("The enemy has died")
            
            
def ally_attack():
    global enemy_health
    damage = random.randint(20,35)
    enemy_health -= damage
    print(f"Ally has done {damage} enemy health is now {enemy_health}")
    if enemy_health > 0: 
        print("--------------------------------")
        time.sleep(2)
        enemy_attack()

def enemy_attack():
    global player_health
    damage = random.randint(6,25)
    player_health -= damage
    print(f"Enemy has done {damage} player health is now {player_health} ")
    if player_health > 0: 
        print("--------------------------------")
        time.sleep(2)
        player_attack()
    
    else:
        print("The player has died")


def hallway():
    setting = input("You are in hallway Vault 100 Would you like to go to the power room, intern room, bathroom, armory, exit1, exit2 or panic room? ")
    if setting == "intern room":
        internroom()
    elif setting == "bathroom":
        bathroom()
    elif setting == "power room":
        powerroom()
    elif setting == "armory":
        armory()
    elif setting == "panic room":
        panicroom()
    elif setting == "exit1":
        exit1()
    elif setting == "exit2":
        exit_2()
    else:
        print("invalid response! ")
        hallway()
def armory():
    global armory_enemy
    global weapon
    global wait_counter
    if armory_enemy == True:
        print("You see another panicked vault dweller who has gotten to a laser rifle first leaving you with a laser pistol. ")
        response=input("Do you let him leave or shoot him? ")
        if response == "let him" or  response == "let him leave":
            print("You let him leave ")
            weapon="laser pistol"
            armory_enemy=False
        elif response == "shoot" or response == "shoot him":
            print("You shoot him in the back and take his laser rifle from him. ")
            weapon="laser rifle"
            armory_enemy=False
        else:
            print("Invalid response! ")
            armory()
    elif armory_enemy == False:
        print("The room is empty.")
    response=input("Do you wait here or return to the hall? ")
    if response == "return" or response == "return to hall" or response == "hall":
        hallway()
    if response == "wait" or response== "wait here":
        wait_counter=wait_counter+1
        print("Nothing happens")
        armory()
    else:
        print("Invalid response")
        armory()
    
        
def internroom():
    global intern_enemy
    global enemy_attack
    global wait_counter
    global enemy_health
    if intern_enemy == True:
        enemy_health=70             
        print("Sitting in the room is a ghoul overseer who jumps to attack you. ")
        def enemy_attack():
            global player_health
            damage = random.randint(20,25)
            player_health -= damage
            print(f"Enemy has done {damage} player health is now {player_health} ")
            if player_health > 0: 
                print("--------------------------------")
                time.sleep(2)
                player_attack()
            else:
                print("""
                    █░█░█▀█░█░█░░░░░░░█░█░█▀█░█░█░█▀▀░░░░░░░█▀▄░▀█▀░█▀▀░█▀▄
░░                   █░░█░█░█░█░░░░░░░█▀█░█▀█░▀▄▀░█▀▀░░░░░░░█░█░░█░░█▀▀░█░█
░░                   ▀░░▀▀▀░▀▀▀░░░░░░░▀░▀░▀░▀░░▀░░▀▀▀░░░░░░░▀▀░░▀▀▀░▀▀▀░▀▀░
                """)
                quit()
        player_attack()
        intern_enemy=False
        print("You find a keycard on the overseers desk")
    else:
        print("The room is empty")
        response=input("Do you wait here or return to the hall? ")
        if response == "return" or response == "return to hall" or response == "hall":
            hallway()
        if response == "wait" or response== "wait here":
            wait_counter=wait_counter+1
            if wait_counter>3:
                print("You wait for too long and allow the supermutant to ambush you. You get clocked over the head and die")
                quit()
            else:
                print("Nothing happens")
                internroom()
        else:
            print("Invalid response")
            internroom()

def bathroom():
    global bathroom_enemy
    global enemy_attack
    global wait_counter
    global enemy_health
    if bathroom_enemy == True:
        enemy_health =5
        print("""
             ,--.     .--.
            /    \. ./    \\
           /  /\/  "  \/\  \\
          / _/ /~~~v~~~\ \_ \\
         /    /####|####\    \\
        ;  /\{#####|#####}/\  \\
        |_/  {#####|#####}  \_:
        |    {#####|#####}    |
        |   /{#####|#####}\   |
        |  / {#####|#####} \  |
        | /  {#####|#####}  \ |
        |  \ \#####|#####/ /  |
        |   \ \####|####/ /   |
         \   \ \###|###/ /   /
          \  /   ~~~~~   \  /  
        """)
        print("Crawling in the bathroom there is a radroach it sees you and attacks you. ")
        def enemy_attack():
            global player_health
            damage = random.randint(1,5)
            player_health -= damage
            print(f"Enemy has done {damage} player health is now {player_health} ")
            if player_health > 0:
                print("---------------------------------")
                time.sleep(2)
                player_attack()
            else:
                print("""
                    █░█░█▀█░█░█░░░░░░░█░█░█▀█░█░█░█▀▀░░░░░░░█▀▄░▀█▀░█▀▀░█▀▄
░░                   █░░█░█░█░█░░░░░░░█▀█░█▀█░▀▄▀░█▀▀░░░░░░░█░█░░█░░█▀▀░█░█
░░                   ▀░░▀▀▀░▀▀▀░░░░░░░▀░▀░▀░▀░░▀░░▀▀▀░░░░░░░▀▀░░▀▀▀░▀▀▀░▀▀░
                """)
                quit()
        player_attack()
        bathroom_enemy=False
        print("You find a Stimpack in the bathroom")
    response=input("Do you wait here or return to the hall? ")
    if response == "return" or response == "return to hall" or response == "hall":
        hallway()
    if response == "wait" or response== "wait here":
        wait_counter=wait_counter+1
        if wait_counter>3:
            print("You wait for too long and allow the supermutant to ambush you. You get clocked over the head and die")
            quit()
        else:
            print("Nothing happens")
            bathroom()
    else:
        print("Invalid response")
        bathroom()

def powerroom():
    global powerroom_enemy
    global enemy_attack
    global wait_counter
    global enemy_health
    if powerroom_enemy == True:
        enemy_health= 10            
        print("You walk into the power room and to your suprise you see a disgusting mole rat chewing the wires! It turns around and fixes its gaze to you.")
        print ("""
        
                           (\,/)
                            oo   ''\'//,        _
                          ,/_;~,        \,    / '
           ikas           "'   \    (    \    !
                                ',|  \    |__.'
                                '~  '~----'' 
    """)
        
    
        
        
        

        def enemy_attack():
            global player_health
            damage = random.randint(10,10)
            player_health -= damage
            print(f"Enemy has done {damage} player health is now {player_health} ")
            if player_health > 0: 
                print("--------------------------------")
                time.sleep(2)
                player_attack()
            else:
                print("""
                    █░█░█▀█░█░█░░░░░░░█░█░█▀█░█░█░█▀▀░░░░░░░█▀▄░▀█▀░█▀▀░█▀▄
░░                   █░░█░█░█░█░░░░░░░█▀█░█▀█░▀▄▀░█▀▀░░░░░░░█░█░░█░░█▀▀░█░█
░░                   ▀░░▀▀▀░▀▀▀░░░░░░░▀░▀░▀░▀░░▀░░▀▀▀░░░░░░░▀▀░░▀▀▀░▀▀▀░▀▀░
                """)
                quit()
        player_attack()
        powerroom_enemy=False
    else:
        print("The room is empty")
    response=input("Do you wait here or return to the hall? ")
    if response == "return" or response == "return to hall" or response == "hall":
        hallway()
    if response == "wait" or response== "wait here":
        wait_counter=wait_counter+1
        if wait_counter>3:
            print("You wait for too long and allow the supermutant to ambush you. You get clocked over the head and die")
            quit()
        else:
            print("Nothing happens")
            powerroom()
    else:
        print("Invalid response")
        powerroom()

def exit1():
    global exit1_enemy
    global enemy_attack
    global enemy_health
    if intern_enemy == False:
        print("You use the keycard and open the door")
        enemy_health=200           
        print("Standing over the exit is the super mutant he guards the way out this is the final battle, he attacks you. ")
        print("""        ((*                       
                        %#(((,                      
                        %(##%                       
                    .*#&%%#,.&%%(*               
                /...,.  ,#. ./&&###&              
                ,*#%&#,,,,*,,/##&&&&%              
                (#%& %&#((%%##%% &%#/              
            ##&&&    %####%%%%    &(,,            
            (&%@     ((//(/(((      (.            
            ((%     %&@&###%&&%%    % /           
            (. .   &&%%%%(#%&%%%%  . .(           
                @   &%%(&%&&%%&%%%%   @             
                    #%&/&&%&%&&&&,(                 
                    ###%%&   ##(,,                 
                    #%&%       ###(                
                    %&&%#     %#%%#                
                    @@@@@     @@&&&@               
                    @@@@       @@@@                
                    @@@@       @@&@@               
                    @@@@         @&%&@ 
        """)
        def enemy_attack():
            global player_health
            damage = random.randint(20,50)
            player_health -= damage
            print(f"Enemy has done {damage} player health is now {player_health}")
            if player_health > 0: 
                print("--------------------------------")
                time.sleep(2)
                player_attack()
            else:
                print("""
                    █░█░█▀█░█░█░░░░░░░█░█░█▀█░█░█░█▀▀░░░░░░░█▀▄░▀█▀░█▀▀░█▀▄
░░                   █░░█░█░█░█░░░░░░░█▀█░█▀█░▀▄▀░█▀▀░░░░░░░█░█░░█░░█▀▀░█░█
░░                   ▀░░▀▀▀░▀▀▀░░░░░░░▀░▀░▀░▀░░▀░░▀▀▀░░░░░░░▀▀░░▀▀▀░▀▀▀░▀▀░
                """)
                quit()
        player_attack()
    else:
        print("The door is locked you need to find a keycard")
        hallway()
    if enemy_health > 0:
                print(f" You have escaped the vault successfully and safely, well maybe with a few scratches, but nothing you can't handle! well done {name},But your journey has just began as the only survivor of vault 100, it is your duty to go out and look for survivor's and other civilizations, but do be careful the horrors outside the vault are much more dangerous and terrifying.Good luck in your travels survivor." )
                quit()
                exit1_enemy=False

def exit_2():
    global weapon
    global enemy_attack
    global player_attack
    global enemy_health
    if weapon == "laser pistol":
        print("The door to this exit seems to be blocked by something heavy. Coming up behid you is the vault dweller who you spared in the armory. \"Let me give you a hand.\" You both push the door open.")
        print("As you both exit the vault you see a supermutant coming up to the other exit so you ambush him." )
        print ("""        (*                       
                        %#(((,                      
                        %(##%                       
                    .*#&%%#,.&%%(*               
                /...,.  ,#. ./&&###&              
                ,*#%&#,,,,*,,/##&&&&%              
                (#%& %&#((%%##%% &%#/              
            ##&&&    %####%%%%    &(,,            
            (&%@     ((//(/(((      (.            
            ((%     %&@&###%&&%%    % /           
            (. .   &&%%%%(#%&%%%%  . .(           
                @   &%%(&%&&%%&%%%%   @             
                    #%&/&&%&%&&&&,(                 
                    ###%%&   ##(,,                 
                    #%&%       ###(                
                    %&&%#     %#%%#                
                    @@@@@     @@&&&@               
                    @@@@       @@@@                
                    @@@@       @@&@@               
                    @@@@         @&%&@ 
                """)
        enemy_health = 200
        def player_attack():
            global enemy_health
            global enemy_attack
            damage = random.randint(10,15)
            enemy_health -= damage
            print(f"Player has done {damage},enemy health is now {enemy_health}")
            if enemy_health > 0: 
                print("--------------------------------")
                time.sleep(2)
                ally_attack()
        def enemy_attack():
            global player_health
            damage = random.randint(20,50)
            player_health -= damage
            print(f"Enemy has done {damage} player health is now {player_health}" )
            if player_health > 0: 
                print("--------------------------------")
                time.sleep(2)
                player_attack()
            else:
                print("""
                    █░█░█▀█░█░█░░░░░░░█░█░█▀█░█░█░█▀▀░░░░░░░█▀▄░▀█▀░█▀▀░█▀▄
░░                   █░░█░█░█░█░░░░░░░█▀█░█▀█░▀▄▀░█▀▀░░░░░░░█░█░░█░░█▀▀░█░█
░░                   ▀░░▀▀▀░▀▀▀░░░░░░░▀░▀░▀░▀░░▀░░▀▀▀░░░░░░░▀▀░░▀▀▀░▀▀▀░▀▀░
                """)
                quit()

        player_attack()
        
        exit1_enemy=False
        if enemy_health <= 0:
                print(f" You have escaped the vault successfully and safely, well maybe with a few scratches, but nothing you can't handle! well done {name},But your journey has just began as the only survivor of vault 100, it is your duty to go out and look for survivor's and other civilizations, but do be careful the horrors outside the vault are much more dangerous and terrifying.Good luck in your travels survivor." )
                quit()
    else:
        print("The door to this exit seems to be blocked by something heavy. There seems to be no way through. ")
        hallway()
        
def panicroom():
    global player_health
    global bathroom_enemy
    global wait_counter
    if bathroom_enemy==True:
        print("You find some quiet in this room that seems safe from intruders.")
    else:
        response=input("This seems like a safe place to heal, would you like to use your stimpack to heal 50hp? ")
        if response=="yes" or response=="y":
            if player_health>=50:
                player_health=100
            else:
                player_health=player_health+50
            print(f"You heal to {player_health}")
        if response=="no" or response=="n":
            print("You save your stimpack for later.")
    response=input("Do you wait here or return to the hall? ")
    if response == "return" or response == "return to hall" or response == "hall":
        hallway()
    if response == "wait" or response== "wait here":
            wait_counter=wait_counter+1
            if wait_counter>3:
                print("You wait for too long and allow the supermutant to ambush you. You get clocked over the head and die")
                quit()
            else:
                print("Nothing happens")
                panicroom()
    else:
        print("Invalid response")
        panicroom()


print(""""
██    ██  █████  ██    ██ ██   ████████      ██  ██████   ██████              
██    ██ ██   ██ ██    ██ ██      ██        ███ ██  ████ ██  ████             
██    ██ ███████ ██    ██ ██      ██         ██ ██ ██ ██ ██ ██ ██             
 ██  ██  ██   ██ ██    ██ ██      ██         ██ ████  ██ ████  ██             
  ████   ██   ██  ██████  ███████ ██         ██  ██████   ██████ 
""")
print("""In 2099, the storm of world war had come again. In two brief hours, most of the planet was reduced to cinders. And from the ashes of nuclear devastation, a new civilization would struggle to arise.
A few were able to reach the relative safety of the large underground Vaults. You was part of that group that entered Vault 100. Imprisoned safely behind the large Vault door, under a mountain of stone, a generation has lived without knowledge of the outside world.
Life in the Vault is about to change.
You awake from your sleep to loud alarms coming from within the vault! with constant reminder from the vault announcer repeating "Warning! the vault is under attack, please exit".
You stand up from your bed and approach the terminal to your room door.""")


name= input("Enter your name: ")
print(f"greetings{name}! Welcome to your adventure in  vault 100! ")
start=input ("Would you rather play the game or perish? ")
if start =="play":
    print("Great!Lets play the game!")
    hallway()
else:
    print("Lame. Okay you\'re dead now...")
    quit()



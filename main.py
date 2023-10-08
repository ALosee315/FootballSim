"""
Functions
"""
#Searches the designated file for the name of the player (case insensitive)
def searchForName(nm,file):
    line = file.readline()
    while line:
        #Clear the line of whitespace
        plr = str.strip(line)

        if nm.lower() == plr.lower():
            return True
        line = f.readline()
        if not line:
            break
    return False

"""
Variables
"""
border = "--------------------------------------------------------"
"""
Game Start
"""
print(border)
print("Welcome to football sim 2023")
print(border)

print("What is your name?") #Ask for plr's name
print(border)
name = input()
print(border)

f = open("players.txt","r")
#Search through the player database to see if it's a new player
if searchForName(name,f):
  #If player name was matched in player database
  print("Welcome back",name+"!")  
else:
    #If no match was found add the player to the database
    f.close()
    f = open("players.txt","a")
    f.write(name+"\n")
    print("Nice to meet you",name+"!")
    f.close


f.close()






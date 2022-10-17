#Played Before, Yes/No Checker, Game Information Component version 3
#Version 3 of this Component is the same as Version 2 of this Component but a Story Line was added

#import time is used that time.sleep can be used. time.sleep is used so the User has time to read certain things and this
#creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
import time

#Yes/No Checker
#Check If the User's input is valid
def yes_no_checker(question):
    valid = False
    while not valid:
        #The User response will be lowercased
        response = input(question).lower()

        #If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response

        #If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response

        #If user response is anything other than yes or no, User will be asked to answer yes or no.
        else:
            print("<error> please answer Yes/No (Y/N). ")
            print()

#Story Line Function
#Story Line is used to garner and raise the interest of new User's
#time.sleep used so the User has time to read certain things and this
#creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
def story_line():
    print("Where am I? ")
    time.sleep(2)
    print("What is this place? ")
    time.sleep(2)
    print("Oh... You are awake ")
    time.sleep(2)
    print("Let me introduce myself. My name is Blackbeard. Captain of the Vessel Queen Anne’s Revenge.  ")
    time.sleep(2)
    print("This morning I found you stowed away on my ship. ")
    time.sleep(2)
    print("Fret not I will spare your life.  ")
    time.sleep(2)
    print("For now... ")
    time.sleep(2)
    print("Recently, I have noticed an increase in Plastic Pollution in my beloved Ocean. ")
    time.sleep(2)
    print("As such, I have taken it upon myself to educate people I meet on the damages Plastic Pollution is doing\n"
          "to the Ocean and possible solutions people can take to prevent Plastic Pollution. ")
    time.sleep(2)
    print("Since I have spared your life, I expect you to be one of these people. ")
    time.sleep(2)
    print("Today you will be tasked with the challenge of defeating an Ancient Mystical Sea Creature while learning\n"
          "about Plastic Pollution.  ")
    time.sleep(2)
    print("Below is the following information you will need to know to defeat your chosen Ancient Mystical Sea Creature")
    print()
    time.sleep(2)


#Game information
#Instructs the User on how the Global Citizen Game works and how to play the Global Citizen Game
def game_information():
    print("*****Game information*****")
    print("The Global Citizen Game is a fun, engaging Quiz type game where you learn about the damage Plastic Pollution is doing to the Ocean. \n"
          "By playing this Game you will be able to become more aware of this Global environmental problem and you will learn postive ways/actions \n"
          "you can take te reduce plastic waste. \n"
          "As soon as the game starts you will be asked what Game Mode you want to play. To win this Game you have to defeat a boss. \n"
          "There are three different options/bosses you can choose from. (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD]) \n" 
          "In the Leviathan Game Mode: You will be given 100 Health Points while the Leviathan will have 100 Health Points \n"
          "In the Kraken Game Mode: You will be given 100 Health Points while the Leviathan will have 200 Health Points \n"
          "In the Kraken Game Mode: You will be given 100 Health Points while the Leviathan will have 300 Health Points \n"
          "After you have chosen your Game Mode you will be displayed a passage and then asked a related question \n"
          "around the topic of Plastic Pollution in the Ocean and solutions you personally can take to stop this. \n"
          "Each Question you get right you will damage the boss' health and subtract 20 from their Health Points \n"
          "Conversely, each question you get wrong the boss will damage your health and subtract 20 from your Health Points \n"
          "To WIN the Game you have to get the boss' Health Points to 0. You will LOSE the Game if the boss gets your Health Points to 0. \n"
          "This is a lot to take in but the game is very intuitive and there should be clear instructions for you to play\n"
          "if you get anything wrong. \n"
          "OK Good Luck! Go have some fun! Let the Game begin! \n")
    return""

#Looped for testing purposes
#Looped to make it easier to get test cases
#The 'xxx' is the exit code to stop the loop
for item in range(1,20):

    #Main Routine
    #The User will be asked if they have played the game before
    #If the User answers Yes the Game Continues
    #If the User answers No the Game Instructions are outputed to the User
    #If the User answers an invalid input an Error message will be outputed to
    #the User instructing the User to input the valid value
    played_before = yes_no_checker("Have you played this game before? ")

    if played_before == "no":
        story_line()
        game_information()
        print()

    elif played_before == "yes":
        print("program continues")
        print()
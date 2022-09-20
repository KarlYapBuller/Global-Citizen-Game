#Played Before, Yes/No Checker, Game Information Component version 1
#Version 1 of this Component does not include the Game Information
#but has an area for where it should go for the Global Citizen Game
#Will be added in further developments of this component in the future when idea of game is further synthesized

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

#Game information
#Instructs the User on how the Global Citizen Game works and how to play the Global Citizen Game
def game_information():
    print("*****Game information*****")
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
        game_information()
        print()

    elif played_before == "yes":
        print("program continues")
        print()
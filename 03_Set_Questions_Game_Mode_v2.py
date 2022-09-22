#How many questions and Game Mode Component version 2

#Game Mode Input Checker Function
def game_mode_input_checker(question):
    while True:

        #Error message
        error_message = "Error please input an Integer between 1 and 3 (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])"

        try:
            #It is an float input in the case the User inpurs a valid input but just with a .0
            response = float(input(question))

            #If User's response is 1 return the response
            if response == 1:
                return response

            #If User's response is 2 return the response
            elif response == 2:
                return response

            #If User's response is 3 return the response
            elif response == 3:
                return response

            #If User's response is not 1,2,3 print the <ERROR> message
            else:
                print(error_message)
                print()
                continue

        #If the User inputs an invalid value print the <ERROR> message
        except ValueError:
            print(error_message)
            print()

#Main routine goes here

game_loop = ""
while game_loop == "":

    #Number of question answered
    number_of_questions_answered = 0
    number_of_leviathan_questions = 5
    number_of_kraken_questions = 10
    number_of_hydra_questions = 20

    #Asks the User what game mode they want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])
    game_mode = game_mode_input_checker("What game mode do you want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])? ")
    print()

    #Game Mode 1. Leviathan [EASY]
    if game_mode == 1:

        #Set to 5 Questions/loops because Game Mode 1. Leviathan is the Easy difficulty
        for item in range(0, 5):
            #Prints out the Question Number
            print("*****Question {} of {}*****".format(number_of_questions_answered + 1, number_of_leviathan_questions))
            #This peice of code stipulates that each time the User answer
            #the questions the the number of questions answered would increase by 1
            number_of_questions_answered += 1
        #Breaks the Game Loop
        break

    #Game Mode 2. Kraken [MEDIUM]
    elif game_mode == 2:

        #Set to 10 Questions/loops because Game Mode 2. Kraken is the Medium difficulty
        for item in range(0, 10):
            #Prints out the Question Number
            print("*****Question {} of {}*****".format(number_of_questions_answered + 1, number_of_kraken_questions))
            number_of_questions_answered += 1
        #Breaks the Game Loop
        break
    #Game Mode 3. Hydra [HARD]
    elif game_mode == 3:

        #Set to 20 Questions/loops because Game Mode 3. Hydra is the Hard difficulty
        for item in range(0, 20):
            #Prints out the Question Number
            print("*****Question {} of {}*****".format(number_of_questions_answered + 1, number_of_hydra_questions))
            number_of_questions_answered += 1
        #Breaks the Game Loop
        break

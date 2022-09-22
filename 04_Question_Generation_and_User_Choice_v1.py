#Question generation and User Choice component version 4
#This piece of code fixes the <ERROR> in version 3 of this component as it fixes
#The problem of the same question not being asked again when the
#User inputs an invalid value and the Error message appears to the User

import random

#Input Checker
def input_checker(question):
    while True:
        try:
            #It is an float input in the case the User input the correct answer but just with a .0
            response = float(input(question))
            return response
        #The Error message is printed out to the User
        except ValueError:
            print("<ERROR> Please input an Integer\n")
            continue

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


#Number of question answered
number_of_questions_answered = 0
user_health = 100
leviathan_health = 100

game_loop = ""
while game_loop == "":

    # Asks the User what game mode they want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])
    game_mode = game_mode_input_checker(
        "What game mode do you want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])? ")
    print()

    if game_mode == 1:

        while user_health and leviathan_health != 0:
            #Prints out the Question Number
            print("*****Question {}*****".format(number_of_questions_answered +1))

            #Number 1 that is in the first position before
            #The addition is a random integer between 0 and 20
            number_1 = random.randint(0,20)
            #Number 2 that is in the first position before
            #The addition is a random integer between 0 and 20
            number_2 = random.randint(0,20)
            #The answer is equal to Number 1 + Number 2
            answer = number_1 + number_2

            #The question asked to the User
            #The Input Checker is a float input in the case the User input the correct answer but just with a .0
            response = input_checker(("What is {} + {}?  ".format(number_1, number_2)))

            #If the User's response is equal to the answer (Number 1 + Number 2) the User gets the question 'Correct'
            if response == answer:
                result = "Correct"
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1
                leviathan_health -= 20
                print("Your Health: {}".format(user_health))
                print("Leviathan Health: {}".format(leviathan_health))
                print()

            #If the User's response is not equal to the answer (Number 1 + Number 2) the User gets the question 'Incorrect'
            else:
                result = "Incorrect"
                print("Result: {} | Your Answer: {} | Correct Answer: {}".format(result, response, answer))
                print()
                number_of_questions_answered += 1
                user_health -= 20
                print("Your Health: {}".format(user_health))
                print("Leviathan Health: {}".format(leviathan_health))
                print()

            if leviathan_health == 0:
                print("You Win!")
                break

            if user_health == 0:
                print("You Lose!")
                break

    if leviathan_health == 0 or user_health == 0:
        break


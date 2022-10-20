#Round Looping version 2
#This piece of code intergrates the Game History and Statistics Component
#The Game History part of the Component where it showed what the User had inputted
#was not integrated as it did not fit with the Game as it would have possibly caused confusion
#without the prose and question being there
#In conjunction with this the Function name and according variables were changed with
#the Game History part being taken out

#import random is used for the random shuffling of the quiz questions and answers dictionary
import random
#ascii_lowercase is used to get letters that label the unlabbled list of answers. You combine letters and alternatives with zip() and store them in a dictionary
from string import ascii_lowercase


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

#User Choice Checker Function
def user_choice_checker(question):
    while True:

        #Error message
        error_message = "<Error> please input a, b, c or d"

        try:
            #It is an float input in the case the User inpurs a valid input but just with a .0
            response = str(input(question)).lower().strip()

            #If User's response is a return the response
            if response == "a":
                return response

            #If User's response is b return the response
            elif response == "b":
                return response

            #If User's response is c return the response
            elif response == "c":
                return response

            # If User's response is d return the response
            elif response == "d":
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

def game_statistics():
    print()

    #Game Statistics
    #Calculate Game Statistics
    #The number of questions answered correct and incorrect is displayed to the User
    #The percentage of how many questions the User has answered correct and how many questions they have answered incorrect
    print("Questions Answered Correct: {} ({:.0f}%) \t|\t Questions Answered Incorrectly: {} ({:.0f}%) \t".format(questions_answered_correct,
                                                                                                                  percent_correct,
                                                                                                                  questions_answered_incorrect,
                                                                                                                  percent_incorrect))
    print()

#In this dictionary the key holds the question and the value is a list that holds the answer and answer alternatives (wrong answers) to the given question
#The firt answer in the list is the correct answer
quiz_questions_and_answers = {
    "According to the United Nations, at least 800 species worldwide are affected by marine debris and as much as 80 percent of that litter is plastic. \n\n"
    "What is the approximate number of species affected by plastic pollution in the Ocean? ": [
        "800", "8000", "Eight", "Eighty"
    ],
    "It is estimated that up to 13 million metric tons of plastic end up in the ocean each year—the equivalent of a rubbish \n"
    "or garbage truck loads worth every minute. \n\n"
    "What is the estimated number of metric tons of plastic that ends up in the ocean each year? ": [
        "13,000,000", "1,300,000", "130,000,000", "1,300"
    ],
    "Plastic in the ocean can be damaging for Fish, seabirds, sea turtles, and marine mammals \n"
    "as it can cause them to become entangled in or ingest plastic debris, causing suffocation, starvation, and drowning. \n\n"
    "Why is Plastic in the ocean bad for aquatic life? ": [
        "Plastic in the ocean can affect the health of aquatic life and in some cases cause the aquatic life to die", "Plastic in the ocean is actually beneficial for aquatic life not bad",
        "Plastic in the ocean has no effect on aquatic life", "Plastic in the ocean is not bad for aquatic life it is favourable"
    ],
    "Billions of Pounds of plastic can be found in swirling convergences that make up about 40 percent of the world's ocean surfaces. \n"
    "At current rates plastic is expected to outweigh all the fish in the sea by 2050. \n\n"
    "By what year do Scientists predict that plastic will outweigh all the fish in the ocean? ": [
        "2050", "2075", "2020", "3000"
    ],
    "Compiled data showing the length of time for man-made marine debris to biodegrade in the sea from the \n"
    "US’ National Oceanic and Atmospheric Administration (NOAA) and Woods Hole Sea Grant, estimates that it takes the ocean 450 years to break down the plastic. \n\n"
    "What is the estimated number of years for the ocean to break down plastic? ": [
        "450 years", "250 years", "500 years", "200 years"
    ],
    "Plastic in the ocean is very harmful to sea turtles. Research indicates that half of sea turtles worldwide have ingested plastic. \n"
    "Some starve after doing so, mistakenly believing they have eaten enough because their stomachs are full. \n\n"
    "How does plastic pollution in the ocean affect sea turtles? ": [
        "Some Sea Turtles can starve after eating the plastic believing they have eaten enough because their stomachs are full",
        "Sea Turtles lose their ability to swim in the ocean", "Sea Turtles lose their ability to see", "Sea Turtles gain the ability to swim fast in the ocean"
    ],
    "Plastic waste kills up to a million seabirds a year. When seabirds ingest plastic, it takes up room in their stomachs, sometimes causing starvation. \n"
    "Many seabirds are found dead with their stomachs full of this waste. Scientists estimate that 60 percent of all seabird species have eaten pieces of plastic, \n"
    "a figure they predict will rise to 99 percent by 2050. \n\n"
    "What is the current estimated percentage of seabird species that have eaten pieces of plastic? ": [
        "60%", "30%", "50%", "90%"
    ],
    "Consumption of plastic by sea creatures causes severe digestive problems, mainly untreated. Many sea animals eat plastic, mistaking it for food. \n"
    "It decreases the capacity of their stomachs, causing starvation. Reports suggest that plastic consumption by all types of fish amounts to several tons yearly. \n"
    "In addition to causing intestinal injury and death of these fish, this also spreads the risk across the food chain to bigger fish and marine mammals. \n"
    "Why does aquatic life eat plastic? ": [
        "They mistake the plastic for food", "They find plastic tasty", "They could not be bothered finding food", "They want to expand their diet "
    ],
    "Plastic pollution in the seas affects human beings in different ways. In addition to the risks from polluted marine waters, \n"
    "ingestion of plastic by fish and other aquatic beings also, in turn, causes harm to people who consume marine food. \n"
    "Plastic contains a lot of substances which might otherwise be hazardous. When fishing activities are carried out, there is every chance that fishes infected \n"
    "with such harmful substances might find their way into our households, causing health problems to the end consumers. \n"
    "Studies have found that toxins in plastics cause several health issues, including cancers, immune system problems, and congenital disabilities. \n\n"
    "Is it true that Plastic can travel up the food chain through fish and then can be eaten by humans? ": [
        "Yes! It is true", "No! It is false", "I don’t know", "I’m not sure"
    ],
    "The amount of garbage in the seas also pollutes the oceanic waters, just like plastic harms marine life in several ways. \n"
    "Disposing of hazardous materials, including toxic substances such as Bisphenol A, commonly found in many plastic commodities, pollutes the water badly. \n"
    "Since Bisphenol A doesn’t get diluted in water, it results in grave environmental problems. Similarly, the debris \n"
    "uses oxygen as it degrades, resulting in a low level of oxygen in the seas. As oxygen levels go down, it badly affects the survival \n"
    "of marine animals, including whales, dolphins and penguins. \n\n"
    "What is the name of a toxic substance that is found in many plastic’s that pollutes the water in the ocean badly? ": [
        "Bisphenol A", "Paracetamol", "Hydrochloric Acid", "Ascorbic Acid"
    ],
    "Plastic waste in the oceans also threatens the life of birds and other beings that depend on the oceanic life forms for their food requirements. \n"
    "Most of the time, these beings suffer because of ingestion of plastic or because of suffocation, especially birds, by merely being tricked by the \n"
    "brighter colours of plastic junk. The birds also often get caught in the debris and die due to \n"
    "suffocation. According to several kinds of research, 44% of all seabird species, along with cetaceans, oysters, mussels, corals and sea turtles, \n"
    "have been documented to have plastic debris in or around their bodies. \n\n"
    "What is the percentage of Seabird species that have been documented to have plastic in or around their body?": [
        "44%", "20%", "3%", "81%"
    ],
    "Under the influence of solar UV radiation, wind, currents and other natural factors, plastic in the ocean breaks down into small \n"
    "particles called microplastics (particles smaller than 5 mm) or nanoplastics (particles smaller than 100 nm). \n"
    "The small size makes them easy for marine life to ingest accidentally. \n\n"
    "What is the name for the small particles that the ocean has broken down from plastic? ": [
        "Microplastics or Nanoplastics", "Nanoparticles", "The Atom", "Ions"
    ],
    "Plastic waste can encourage the growth of pathogens in the ocean. According to a recent study, scientists concluded that corals that come into contact with plastic have \n"
    "an 89 percent chance of contracting disease, compared with a 4 percent likelihood for corals that do not. \n\n"
    "What is the percentage chance of a coral reef contracting a disease after coming in contact with plastic? ": [
        "89%", "8.9%", "57%", "70%"
    ],
    "Studies estimate there are now 15–51 trillion pieces of plastic in the world's oceans — from the equator to the poles, from Arctic ice sheets to the sea floor. \n"
    "Not one square mile of surface ocean anywhere on earth is free of plastic pollution. \n\n"
    "What is the estimated range of the pieces of plastic in the world’s ocean? ": [
        "15-51 trillion pieces of plastic", "15-51 million pieces of plastic", "3-10 trillion pieces of plastic", "10-17 trillion pieces of plastic"
    ],
    "A way to prevent Plastic Pollution is to reduce Your Use of Single-Use Plastics. Wherever you live, the easiest and most direct \n"
    "way that you can get started is by reducing your own use of single-use plastics. Single-use plastics include plastic bags, water bottles, \n"
    "straws, cups, utensils, dry cleaning bags, take-out containers, and any other plastic items that are used once and then discarded. \n"
    "The best way to do this is by refusing any single-use plastics that you do not need (e.g. straws, plastic bags, takeout utensils, takeout containers), \n"
    "and purchasing, and carrying with you, reusable versions of those products, including reusable grocery bags, produce bags, bottles, utensils, coffee cups, \n"
    "and dry cleaning garment bags.  \n\n"
    "From the possible choice below, which item would be a good choice to help reduce your use of single-use Plastic? ": [
        "Reusable grocery bag", "Plastic bags", "Takeout utensils", "Takeout containers"
    ],
    "Another way to help prevent Plastic Pollution is to support Legislation to limit Plastic Production and Waste. \n"
    "As important as it is to change our individual behaviors, such changes alone are insufficient to stop ocean plastic pollution. \n"
    "We also need legislation that reduces plastic production, improves waste management, and makes plastic producers responsible for the waste they generate. \n"
    "There are a variety of ways that you can support local, national, and international legislation that provide critical solutions to reduce plastic pollution. \n"
    "An example in the United States is the 2021 Break Free From Plastic Pollution Act, which is a comprehensive federal bill that aims to \n"
    "address the plastic pollution crisis, and there are a number of state level initiatives to introduce \n"
    "extended producer responsibility (EPR) legislation that makes plastic producers and distributors responsible for their products and packaging at the end of life. \n\n"
    "Is it true, that you can help prevent Plastic Pollution in the Ocean by Support legislation that limits Plastic Production and Waste? ": [
        "Yes, it is True", "No, it is False", "I do not know", "I have no idea"
    ],
    "A way to prevent Plastic Pollution is to Recycle Properly. This should go without saying, but when you use single-use (and other) plastics that can be recycled, \n"
    "always be sure to recycle them. At present, just 9% of plastic is recycled worldwide. \n"
    "Recycling helps keep plastics out of the ocean and reduces the amount of “new” plastic in circulation. \n\n"
    "Which of the following is an example which shows how to recycle plastic properly? ": [
        "Putting plastic in the correct recycling bin", "Throwing pieces of plastic out of the car window", "Dumping plastic in waterways", "Dumping plastic in drains"
    ],
    "A way to help prevent Plastic Pollution is to participate in or Organize a Beach or River Cleanup. \n"
    "By participating in, or organizing a cleanup of your local beach or waterway you help remove \n"
    "plastics from the ocean and prevent them from getting there in the first place. \n"
    "This is one of the most direct and rewarding ways to fight ocean plastic pollution. \n"
    "You can simply go to the beach or waterway and collect plastic waste on your own or with friends or family, \n"
    "or you can join a local organization’s cleanup. \n\n"
    "Which of the following is a way for you to help prevent Plastic Pollution? ": [
        "Participate in or Organize a Beach or River Cleanup", "Throwing your Plastic into waterways", "Using single-use plastic", "Using plastic straws"
    ],
    "A way to prevent Plastic Pollution is to avoid Products containing Microbeads. Tiny plastic particles, called “microbeads,” have become a \n"
    "growing source of ocean plastic pollution in recent years. Microbeads are found in some face scrubs, toothpastes, and bodywashes, and they readily \n"
    "enter our oceans and waterways through our sewer systems and affect hundreds of marine species. \n"
    "Avoid products containing plastic microbeads by looking for “polythelene” and “polypropylene” on the ingredient labels of your cosmetic products. \n\n"
    "What is the name of the tiny plastic particles that you should avoid to help prevent Plastic Pollution? ": [
        "Microbeads", "Nanobeads", "Kilobeads", "Centibeads"
    ],
    "A way to prevent Plastic Pollution is to spread the word. \n"
    "If you stay informed on issues related to plastic pollution you are then able to help make others aware of the problem. \n"
    "You can start by explaining to your friends and family about how they can be part of the solution. Furthermore, you can even host a \n"
    "viewing party for one of the many plastic pollution focused documentaries, like A Plastic Ocean, \n"
    "Garbage Island: An Ocean Full of Plastic, Bag It, Addicted to Plastic, Plasticized, \n"
    "or Garbage Island to help explain the problem of plastic pollution visually. \n\n"
    "Why is spreading the word to other people of the problem Plastic Pollution is causing in the Ocean so important? ": [
        "So other people can be aware of the great danger Plastic is causing in the Ocean and \n"
        "after becoming aware people can act accordingly to help play their part in the solutions",
        "Who knows", "I have no clue", "I thought Plastic was a good thing"
    ],
    "A way to prevent Plastic Pollution is by supporting Organizations that help address the problem of Plastic Pollution. \n"
    "There are many non-profit organizations working to reduce and eliminate ocean plastic pollution in a variety of different ways. "
    "These organizations rely on donations from people like you to continue their important work. \n"
    "Even small donations can make a big difference! \n\n"
    "Does donating small donations even as little as $1 help support Organizations that help address the problem of Plastic Pollution? ": [
        "Yes!", "No", "Do not ask me", "It beats me"
    ],
    "A way to prevent Plastic Pollution is by minimising bathroom & cleaning products. \n"
    "Minimising bathroom and household cleaning products can result in significant plastic reductions. \n"
    "Simply cutting the number of products you have (e.g. by deciding on your ‘essential’ cosmetics and just sticking to those few items) \n"
    "will make a huge difference over time. Swapping products that come in plastic bottles for unpackaged alternatives (such as shampoo bars), \n"
    "switching wipes for reusable cloths, and choosing reusable menstrual products instead of disposables all help greatly too. \n"
    "A cupboard full of different cleaning products designed to tackle a different part of your home is really not necessary. \n"
    "A re-purposed spray bottle filled with 1 part white vinegar 2 parts warm water is just as effective, \n"
    "contains less harmful chemicals and results in far less plastic waste. \n\n"
    "What is an action you can take to help prevent Plastic Pollution in the Ocean? ": [
        "Buying less single-use bathroom and cleaning products and swapping them out for reusable/refillable options",
        "Buying single-use plastic water bottles", "Buying products containing microbeads", "Buying single-use plastic bathroom and cleaning products"
    ],
    "A way to prevent Plastic Pollution is by purchasing second hand instead of buying new. \n"
    "Purchasing second hand items instead of buying new avoids the plastic packaging that inevitably comes with new purchases. \n"
    "It also means that perfectly good things that are no longer required by their current owners will not potentially end up in the ocean. \n"
    "Furniture, books, clothes, toys, children’s clothes, baby gear, electronics, musical instruments, cars, \n"
    "bikes and sports equipment are all great things to look for second hand. \n"
    "Not only is it good for the planet, it will be good for your pocket too. \n\n"
    "Is purchasing second hand instead of buying new a good way to help prevent Plastic Pollution in the Ocean? ": [
        "Yes", "No", "Who knows", "How should I know"
    ],
    "A way to prevent Plastic Pollution is by buying fewer, high quality items that are made to last. \n"
    "When you do need to buy something new, it’s best to invest in fewer, \n"
    "high quality items designed to last. Buying better things, less frequently involves less plastic packaging, and often \n"
    "less plastic on the products themselves, or if they are made of plastic, the lifetime will be longer. \n\n"
    "Is buying fewer, high quality items that are made to last a good way to help prevent Plastic Pollution in the Ocean? ": [
        "Yes", "No", "I do not know", "I am not sure"
    ],
    "A way to prevent Plastic Pollution is by choosing products made from recycled materials. \n"
    "Choosing products made from recycled materials results in less demand for new plastic to be manufactured, while supporting this emerging consumer sector \n"
    "which is working hard to ‘close the loop’, keeping plastic in use rather than having it end up as worthless waste. \n"
    "We can help make a difference by creating demand for products made from recycled materials, giving plastic waste a value, \n"
    "so it is less likely to end up in our environment. \n\n"
    "Which of the following is an action you can take to help prevent Plastic Pollution? ": [
        "Buying products made from recycled plastic", "Buying single-use plastic straws", "Buying plastic cutlery", "Buying single-use plastic water bottles"
    ],
    "A way to prevent Plastic Pollution is by considering sharing or hiring products made of plastic instead of owning. \n"
    "Growing up in a consumer society, this one can be hard to get our heads round, but the truth is, we don’t always need to own things \n"
    "and with an ever-growing population on our planet with depleting finite resources, it’s not wise for us to aspire to this either. \n"
    "So why not consider sharing or hiring instead of owning – especially with items you don’t use often such as \n"
    "lawnmowers, tools and other quality household, garden and leisure items. \n\n"
    "Is sharing or hiring products made of plastic a good idea to help prevent Plastic Pollution? ": [
        "Yes", "No", "I have not got a clue", "I have not got the faintest idea"
    ]








}

#User Health
user_health = 100
#Leaviathen Health
leviathan_health = 100
#Kraken Health
kraken_health = 200
#Hydra Health
hydra_health = 300

game_loop = ""
while game_loop == "":

    #Number of questions answered
    number_of_questions_answered = 0

    #Questions answered correct
    questions_answered_correct = 0

    #Questions answered incorrect
    questions_answered_incorrect = 0

    #List is used to turn to dictionary of quiz questions and answers into a list
    list_of_quiz_questions_and_answers = list(quiz_questions_and_answers.items())
    #The keys and corresponding values in the list are moved to random possitions in the list
    random.shuffle(list_of_quiz_questions_and_answers)
    #Turn the shuffled list of quiz questions and answers back into a dictionary
    shuffled_list_of_quiz_questions_answers = dict(list_of_quiz_questions_and_answers)

    # Asks the User what game mode they want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])
    game_mode = game_mode_input_checker(
        "What game mode do you want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])? ")
    print()

    if game_mode == 1:

        print("Game Mode: Leviathan")

        while user_health and leviathan_health != 0:

            # Iterate through the dictionary (quiz_questions_and_answers) to get the key, value pair and also the index (used for the Question number)
            # Enumarate is used to give the value pairs in the quiz_questions_and_answers dictionary an index number
            # The index value from which the counter is to be started is at 1 for converstion into letters for the label in the answer alternatives
            for question_number, (question, unlabled_list_of_answers) in enumerate(
                    shuffled_list_of_quiz_questions_answers.items(), start=1):
                # Print Question Number
                print("\nQuestion {}:".format(question_number))
                # Ask Question to the User
                print("{}?".format(question))
                # The correct answer to the given question is the first answer in the list of answers
                correct_answer = unlabled_list_of_answers[0]

                # sorted is used to change the order of the items in the list of answers
                # string.ascii_lowercase is used to get letters that label the list of answers
                # You combine letters and alternatives with zip() and store them in the dictionary
                labeled_list_of_answers = dict(zip(ascii_lowercase, sorted(unlabled_list_of_answers)))

                # label is the a, b, c, d that appears underneath the queston and corresponds to a value in the dictionaries (list of answers)
                for label, list_of_answers in labeled_list_of_answers.items():
                    print("{}) {}".format(label, list_of_answers))

                # Ask the User what their Choice will be to the given question
                user_answer = user_choice_checker("\nChoice? ")

                answer = labeled_list_of_answers.get(user_answer)

                #If the User's answer is equal to the correct answet the User gets the question right
                #Print Correct
                #-20 from the Leviathen Health
                #Print User Health and Leviathen Health
                #The number of questions answered increases by 1
                #The number of questions answered correct increases by 1
                #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                #divided by the number of questions answered times by 100
                #The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                #the Game History and Statistics function
                if answer == correct_answer:
                    print("Correct!")
                    leviathan_health -= 20
                    print("Your Health: {}".format(user_health))
                    print("Leviathan Health: {}".format(leviathan_health))
                    number_of_questions_answered += 1
                    questions_answered_correct += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

                #If the User's answer is not equal to the correct answer the User get the question wrong
                #Print Wrong and tell the User the correct answer
                #-20 from User Health
                #Print User Health and Leviathen Health
                #The number of questions answered increases by 1
                #The number of questions answered incorrect increases by 1
                #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                #divided by the number of questions answered times by 100
                #The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                #the Game History and Statistics function
                else:
                    print("Wrong!")
                    print("The answer is {}".format(correct_answer))
                    user_health -= 20
                    print("Your Health: {}".format(user_health))
                    print("Leviathan Health: {}".format(leviathan_health))
                    number_of_questions_answered += 1
                    questions_answered_incorrect += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

                #If User is able to knock down the Leviathen Health to 0 they Win the Game
                #Game Mode loop is broken
                if leviathan_health == 0:
                    print("You Win!")
                    break
                #If User health is knocked down to 0 they Lose the Game
                #Game Mode loop is broken
                if user_health == 0:
                    print("You Lose!")
                    break

    if game_mode == 2:

        print("Game Mode: Kraken")

        while user_health and kraken_health != 0:

            # Iterate through the dictionary (quiz_questions_and_answers) to get the key, value pair and also the index (used for the Question number)
            # Enumarate is used to give the value pairs in the quiz_questions_and_answers dictionary an index number
            # The index value from which the counter is to be started is at 1 for converstion into letters for the label in the answer alternatives
            for question_number, (question, unlabled_list_of_answers) in enumerate(
                    shuffled_list_of_quiz_questions_answers.items(), start=1):
                # Print Question Number
                print("\nQuestion {}:".format(question_number))
                # Ask Question to the User
                print("{}?".format(question))
                # The correct answer to the given question is the first answer in the list of answers
                correct_answer = unlabled_list_of_answers[0]

                # sorted is used to change the order of the items in the list of answers
                # string.ascii_lowercase is used to get letters that label the list of answers
                # You combine letters and alternatives with zip() and store them in the dictionary
                labeled_list_of_answers = dict(zip(ascii_lowercase, sorted(unlabled_list_of_answers)))

                # label is the a, b, c, d that appears underneath the queston and corresponds to a value in the dictionaries (list of answers)
                for label, list_of_answers in labeled_list_of_answers.items():
                    print("{}) {}".format(label, list_of_answers))

                # Ask the User what their Choice will be to the given question
                user_answer = user_choice_checker("\nChoice? ")

                answer = labeled_list_of_answers.get(user_answer)

                #If the User's answer is equal to the correct answet the User gets the question right
                #Print Correct
                #-20 from the Kraken Health
                #Print User Health and Kraken Health
                #The number of questions answered increases by 1
                #The number of questions answered correct increases by 1
                #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                #divided by the number of questions answered times by 100
                #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
                #the Game History and Statistics function
                if answer == correct_answer:
                    print("Correct!")
                    kraken_health -= 20
                    print("Your Health: {}".format(user_health))
                    print("Hydra Health: {}".format(kraken_health))
                    number_of_questions_answered += 1
                    questions_answered_correct += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

                #If the User's answer is not equal to the correct answer the User get the question wrong
                #Print Wrong and tell the User the correct answer
                #-20 from User Health
                #Print User Health and Kraken Health
                #The number of questions answered increases by 1
                #The number of questions answered incorrect increases by 1
                #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                #divided by the number of questions answered times by 100
                #The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                #the Game History and Statistics function
                else:
                    print("Wrong!")
                    print("The answer is {}".format(correct_answer))
                    user_health -= 20
                    print("Your Health: {}".format(user_health))
                    print("Hydra Health: {}".format(kraken_health))
                    number_of_questions_answered += 1
                    questions_answered_incorrect += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

                #If User is able to knock down the Kraken Health to 0 they Win the Game
                #Game Mode loop is broken
                if kraken_health == 0:
                    print("You Win!")
                    break
                #If User health is knocked down to 0 they Lose the Game
                #Game Mode loop is broken
                if user_health == 0:
                    print("You Lose!")
                    break

    if game_mode == 3:

        print("Game Mode: Hydra")

        while user_health and hydra_health != 0:

            # Iterate through the dictionary (quiz_questions_and_answers) to get the key, value pair and also the index (used for the Question number)
            # Enumarate is used to give the value pairs in the quiz_questions_and_answers dictionary an index number
            # The index value from which the counter is to be started is at 1 for converstion into letters for the label in the answer alternatives
            for question_number, (question, unlabled_list_of_answers) in enumerate(
                    shuffled_list_of_quiz_questions_answers.items(), start=1):
                # Print Question Number
                print("\nQuestion {}:".format(question_number))
                # Ask Question to the User
                print("{}?".format(question))
                # The correct answer to the given question is the first answer in the list of answers
                correct_answer = unlabled_list_of_answers[0]

                # sorted is used to change the order of the items in the list of answers
                # string.ascii_lowercase is used to get letters that label the list of answers
                # You combine letters and alternatives with zip() and store them in the dictionary
                labeled_list_of_answers = dict(zip(ascii_lowercase, sorted(unlabled_list_of_answers)))

                # label is the a, b, c, d that appears underneath the queston and corresponds to a value in the dictionaries (list of answers)
                for label, list_of_answers in labeled_list_of_answers.items():
                    print("{}) {}".format(label, list_of_answers))

                # Ask the User what their Choice will be to the given question
                user_answer = user_choice_checker("\nChoice? ")

                answer = labeled_list_of_answers.get(user_answer)

                #If the User's answer is equal to the correct answet the User gets the question right
                #Print Correct
                #-20 from the Hydra Health
                #Print User Health and Kraken Health
                #The number of questions answered increases by 1
                #The number of questions answered correct increases by 1
                #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                #divided by the number of questions answered times by 100
                #The Percent Corcrect and Percent Incorrect is used to calculate the Game Statisitcs in
                #the Game History and Statistics function
                if answer == correct_answer:
                    print("Correct!")
                    hydra_health -= 20
                    print("Your Health: {}".format(user_health))
                    print("Hydra Health: {}".format(hydra_health))
                    number_of_questions_answered += 1
                    questions_answered_correct += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

                #If the User's answer is not equal to the correct answer the User get the question wrong
                #Print Wrong and tell the User the correct answer
                #-20 from User Health
                #Print User Health and Hydra Health
                #The number of questions answered increases by 1
                #The number of questions answered incorrect increases by 1
                #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                #divided by the number of questions answered times by 100
                #The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                #the Game History and Statistics function
                else:
                    print("Wrong!")
                    print("The answer is {}".format(correct_answer))
                    user_health -= 20
                    print("Your Health: {}".format(user_health))
                    print("Hydra Health: {}".format(hydra_health))
                    number_of_questions_answered += 1
                    questions_answered_incorrect += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100

                #If User is able to knock down the Hydra Health to 0 they Win the Game
                #Game Mode loop is broken
                if hydra_health == 0:
                    print("You Win!")
                    break
                #If User health is knocked down to 0 they Lose the Game
                #Game Mode loop is broken
                if user_health == 0:
                    print("You Lose!")
                    break

    print()
    #Ask the User if the want to see their Game History and Statistics
    see_statistics = yes_no_checker("Do you want to see your Game Statistics (Y/N)? ")

    #If the User inputs 'yes' they want to see their Game History and Statistics
    #Their Game History and Statistics will be displayed
    if see_statistics == "yes":
        game_statistics()
        print()

    #Breaks the Game Loop
    #If User is able to knock down the Leviathen Health to 0 or If User health is knocked down to 0
    if leviathan_health == 0 or user_health == 0:
        break

    #Breaks the Game Loop
    #If User is able to knock down the Kraken Health to 0 or If User health is knocked down to 0
    if kraken_health == 0 or user_health == 0:
        break

    #Breaks the Game Loop
    #If User is able to knock down the Hydra Health to 0 or If User health is knocked down to 0
    if hydra_health == 0 or user_health == 0:
        break

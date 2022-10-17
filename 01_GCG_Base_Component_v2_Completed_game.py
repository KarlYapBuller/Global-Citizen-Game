#Global Citizen Game Version 2 After Usability Testing

#import random is used for the random shuffling of the quiz questions and answers dictionary
import random
#ascii_lowercase is used to get letters that label the unlabbled list of answers. You combine letters and alternatives with zip() and store them in a dictionary
from string import ascii_lowercase
#import time is used in specific places so the User has time to read certain things and this
#creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
import time

#Yes/No Checker Function
#Check If the User's input is valid
def yes_no_checker(question):
    valid = False
    while not valid:
        #The User response will be lowercased
        response = input(question).lower().strip()

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

#Game Information Function
#Instructs the User on how the Global Citizen Game works and how to play the Global Citizen Game
def game_information():
    statement_generator("📚 Game Information 📚", "*")
    print()
    print("The Global Citizen Game is a fun, engaging Quiz type game where you learn about the damage Plastic Pollution is doing to the Ocean. \n"
          "By playing this Game you will be able to become more aware of this Global environmental problem and you will learn positive ways/actions \n"
          "you can take to reduce plastic waste. \n"
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
            response = float(input(question)).strip()

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

#Game History and Statistics Function
def game_statistics():
    print()

    statement_generator("Statistics", "%")
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

#Statement Generator Function
#Decorates the statements in the Lucky Unicorn game
def statement_generator(statement, decoration):

    #The of the statement is the chosen decoration times by 3
    sides = decoration * 3

    #The statement outputed to the User is the chosen statement with
    #the sides on the left and right of the statement
    statement = "{} {} {}".format(sides, statement, sides)
    #The decotration on the top and bottom of the the statement is
    #the chosen decoration and it is the length of the statement
    top_bottom = decoration * len(statement)

    #top_bottom and statement variables are outputed to the User
    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Quiz Sources Function
#Contains the sources URL in which the information in the
#passages of the Global Citizen Game Quiz is from on the Internet
def quiz_sources():
    statement_generator("Quiz Sources", "|")
    print()
    print("https://www.pewtrusts.org/en/research-and-analysis/articles/2018/09/24/plastic-pollution"
          "-affects-sea-life-throughout-the-ocean#:~:text=It%20is%20estimated%20that%20up,suffocation%2C%20starvation%2C%20and%20drowning.  \n"
          "https://www.biologicaldiversity.org/campaigns/ocean_plastics/ \n"
          "https://www.weforum.org/agenda/2018/11/chart-of-the-day-this-is-how-long-everyday"
          "-plastic-items-last-in-the-ocean/#:~:text=But%20it%20takes%20the%20ocean,to%20biodegrade%20in%20the%20sea. \n"
          "https://www.marineinsight.com/environment/how-is-plastic-ruining-the-ocean/ \n"
          "https://www.iucn.org/resources/issues-brief/marine-plastic-pollution \n"
          "https://www.oceanicsociety.org/resources/7-ways-to-reduce-ocean-plastic-pollution-today/ \n"
          "https://www.seeturtles.org/plastic-ocean-tips \n"
          "https://www.lessplastic.org.uk/9-ways-you-can-reduce-ocean-plastic/ \n"
          "https://www.nrdc.org/stories/10-ways-reduce-plastic-pollution  \n")

#Health Bar Function
def user_health_bar():
  #Get the number to divide by to convert health to dashes
  dash_convert = int(max_user_health/health_dashes)
  #Convert health to dash count
  current_dashes = int(user_health/dash_convert)
  #Get the health remaining to fill as space
  remaining_health = health_dashes - current_dashes

  # Convert current dashes to 8 dashes as a string
  health_display = '-' * current_dashes
  # Convert the remaining health to spaces as a string
  remaining_display = ' ' * remaining_health

  #Print User Health to Indicate to User that this is their Health and their Health Bar
  print("|" + health_display + remaining_display + "|")

def boss_health_bar():
  #Get the number to divide by to convert health to dashes
  dash_convert = int(max_boss_health/health_dashes)
  #Convert health to dash count
  current_dashes = int(boss_health/dash_convert)
  #Get the health remaining to fill as space
  remaining_health = health_dashes - current_dashes

  # Convert current dashes to 8 dashes as a string
  health_display = '-' * current_dashes
  # Convert the remaining health to spaces as a string
  remaining_display = ' ' * remaining_health

  # Print User Health to Indicate to User that this is the Boss' Health and the Boss' Health Bar
  print("|" + health_display + remaining_display + "|")

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
    "In addition to causing intestinal injury and death of these fish, this also spreads the risk across the food chain to bigger fish and marine mammals. \n\n"
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
        "Bisphenol A, Paracetamol, Hydrochloric Acid, Ascorbic Acid "
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
    "A way to prevent Plastic Pollution is to avoid Products containing Microbeads. Tiny plastic particles, called “microbeads,” have become a "
    "growing source of ocean plastic pollution in recent years. Microbeads are found in some face scrubs, toothpastes, and bodywashes, and they readily "
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

#Main routine goes here

#Welcomes the User to the Quiz Quest Game
statement_generator("👋 Welcome to the Global Citizen Game 👋", "-")
print()

#Heading for 'ask the User if they have played before'
#This heading is used to draw the User attention to the given question and to get the
#User to realise that this is an important part of the game and that they need to input an answer
statement_generator("▶ Played Before ▶", "!")
print()

#Asks the User if they have played the Game before
#If the User answers Yes the Game Continues
#If the User answers No the Game Instructions are outputed to the User
#If the User answers an invalid input an Error message will be outputed to
#the User instructing the User to input the valid value
played_before = yes_no_checker("Have you played this game before (Y/N)? ")
print()

#If the User answers No the Game Instructions are outputed to the User
if played_before == "no":
    game_information()
    print()
    #time.sleep used so the User has time to read certain things and this
    #creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
    time.sleep(0.75)

#User Health
user_health = 100
#Boss Health
#Leviathan Health = 100, Kraken Health = 200, Hydra Health = 300
#Each respective Boss Health will be changed if the User selects that Boss' Game Mode
#This was done so that there did not need to be a Health Bar for each respective Boss,
#and it makes the Game more robust if other Boss' were to be added
boss_health = 0
# Max User Health
max_user_health = 100
#Max Boss Health
max_boss_health = 0
# Max Displayed dashes
health_dashes = 50

#Game Loop
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

    #Heading for 'Game Mode'
    #This heading is used to draw the User attention to the given question and to get the
    #User to realise that this is an important part of the game and that they need to input an answer
    statement_generator("Game Mode", "=")
    print()

    # Asks the User what game mode they want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])
    game_mode = game_mode_input_checker(
        "What boss do you want to go against (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])? ")
    print()

    if game_mode == 1:

        statement_generator("Game Mode: LEVIATHAN 🐍", "!")

        #Change Boss Health and Max Bass Health (for Health Bar) to 100 since User chose the Leviathan Game Mode
        boss_health += 100
        max_boss_health += 100

        while user_health and boss_health != 0:

            # Iterate through the dictionary (quiz_questions_and_answers) to get the key, value pair and also the index (used for the Question number)
            # Enumarate is used to give the value pairs in the quiz_questions_and_answers dictionary an index number
            # The index value from which the counter is to be started is at 1 for converstion into letters for the label in the answer alternatives
            for question_number, (question, unlabled_list_of_answers) in enumerate(
                    shuffled_list_of_quiz_questions_answers.items(), start=1):
                #Displays to the User the Question Number
                print()
                statement_generator(f"Question {question_number}", "#")
                print()
                #Ask Question to the User
                print(f"{question}?")
                # The correct answer to the given question is the first answer in the list of answers
                correct_answer = unlabled_list_of_answers[0]

                # sorted is used to change the order of the items in the list of answers
                # string.ascii_lowercase is used to get letters that label the list of answers
                # You combine letters and alternatives with zip() and store them in the dictionary
                labeled_list_of_answers = dict(zip(ascii_lowercase, sorted(unlabled_list_of_answers)))

                # label is the a, b, c, d that appears underneath the queston and corresponds to a value in the dictionaries (list of answers)
                for label, list_of_answers in labeled_list_of_answers.items():
                    print(f"{label}) {list_of_answers}")

                # Ask the User what their Choice will be to the given question
                user_answer = user_choice_checker("\nChoice? ")
                print()

                answer = labeled_list_of_answers.get(user_answer)

                #If the User's answer is equal to the correct answer the User gets the question right
                #Print Correct
                #-20 from the Leviathen Health
                #Print User Health and Leviathen Health with respective Health Bars
                #The number of questions answered increases by 1
                #The number of questions answered correct increases by 1
                #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                #divided by the number of questions answered times by 100
                #The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                #the Game History and Statistics function
                if answer == correct_answer:
                    result = "Correct!"
                    print(f"Result ✨: {result}| Your Answer 🤓: {user_answer} | Correct Answer ✅: {correct_answer}")
                    print()
                    boss_health -= 20
                    print(f"USER HEALTH 🧑: {user_health} HP")
                    user_health_bar()
                    print(f"LEVIATHAN HEALTH 🐍: {boss_health} HP")
                    boss_health_bar()
                    number_of_questions_answered += 1
                    questions_answered_correct += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100
                    print()

                #If the User's answer is not equal to the correct answer the User get the question wrong
                #Print Wrong and tell the User the correct answer
                #-20 from User Health
                #Print User Health and Leviathen Health with respective Health Bars
                #The number of questions answered increases by 1
                #The number of questions answered incorrect increases by 1
                #Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                #divided by the number of questions answered times by 100
                #The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                #the Game History and Statistics function
                else:
                    result = "Wrong!"
                    print(f"Result ✨: {result} | Your Answer 🤓: {user_answer} | Correct Answer ✅: {correct_answer}")
                    print()
                    user_health -= 20
                    print(f"               USER HEALTH 🧑: {user_health} HP")
                    user_health_bar()
                    print(f"             LEVIATHAN HEALTH 🐍: {boss_health} HP")
                    boss_health_bar()
                    number_of_questions_answered += 1
                    questions_answered_incorrect += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100
                    print()

                #time.sleep used so the User has time to read certain things and this
                #creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
                time.sleep(0.75)

                #If User is able to knock down the Leviathen Health to 0 they Win the Game
                #Game Mode loop is broken
                if boss_health == 0:
                    statement_generator("😊 YOU WIN 😊", "!")
                    break
                #If User health is knocked down to 0 they Lose the Game
                #Game Mode loop is broken
                if user_health == 0:
                    statement_generator("😭 YOU LOSE 😭", "!")
                    break

    if game_mode == 2:

        statement_generator("Game Mode: KRAKEN HEALTH 🐙", "!")

        #Change Boss Health and Max Bass Health (for Health Bar) to 200 since User chose the Kraken Game Mode
        boss_health += 200
        max_boss_health += 200

        while user_health and boss_health != 0:

            # Iterate through the dictionary (quiz_questions_and_answers) to get the key, value pair and also the index (used for the Question number)
            # Enumarate is used to give the value pairs in the quiz_questions_and_answers dictionary an index number
            # The index value from which the counter is to be started is at 1 for converstion into letters for the label in the answer alternatives
            for question_number, (question, unlabled_list_of_answers) in enumerate(
                    shuffled_list_of_quiz_questions_answers.items(), start=1):
                #Displays to the User the Question Number
                print()
                statement_generator(f"Question {question_number}", "#")
                print()
                #Ask Question to the User
                print(f"{question}?")
                # The correct answer to the given question is the first answer in the list of answers
                correct_answer = unlabled_list_of_answers[0]

                # sorted is used to change the order of the items in the list of answers
                # string.ascii_lowercase is used to get letters that label the list of answers
                # You combine letters and alternatives with zip() and store them in the dictionary
                labeled_list_of_answers = dict(zip(ascii_lowercase, sorted(unlabled_list_of_answers)))

                # label is the a, b, c, d that appears underneath the queston and corresponds to a value in the dictionaries (list of answers)
                for label, list_of_answers in labeled_list_of_answers.items():
                    print(f"{label}) {list_of_answers}")

                # Ask the User what their Choice will be to the given question
                user_answer = user_choice_checker("\nChoice? ")
                print()

                answer = labeled_list_of_answers.get(user_answer)

                # If the User's answer is equal to the correct answer the User gets the question right
                # Print Correct
                # -20 from the Kraken Health
                # Print User Health and Kraken Health with respective Health Bars
                # The number of questions answered increases by 1
                # The number of questions answered correct increases by 1
                # Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                # divided by the number of questions answered times by 100
                # The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                # the Game History and Statistics function
                if answer == correct_answer:
                    result = "Correct!"
                    print(f"Result ✨: {result}| Your Answer 🤓: {user_answer} | Correct Answer ✅: {correct_answer}")
                    print()
                    boss_health -= 20
                    print(f"USER HEALTH 🧑: {user_health} HP")
                    user_health_bar()
                    print(f"KRAKEN HEALTH 🐙: {boss_health} HP")
                    boss_health_bar()
                    number_of_questions_answered += 1
                    questions_answered_correct += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100
                    print()

                # If the User's answer is not equal to the correct answer the User get the question wrong
                # Print Wrong and tell the User the correct answer
                # -20 from User Health
                # Print User Health and Kraken Health with respective Health Bars
                # The number of questions answered increases by 1
                # The number of questions answered incorrect increases by 1
                # Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                # divided by the number of questions answered times by 100
                # The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                # the Game History and Statistics function
                else:
                    result = "Wrong!"
                    print(f"Result ✨: {result} | Your Answer 🤓: {user_answer} | Correct Answer ✅: {correct_answer}")
                    print()
                    user_health -= 20
                    print(f"               USER HEALTH 🧑: {user_health} HP")
                    user_health_bar()
                    print(f"             KRAKEN HEALTH 🐙: {boss_health} HP")
                    boss_health_bar()
                    number_of_questions_answered += 1
                    questions_answered_incorrect += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100
                    print()

                #time.sleep used so the User has time to read certain things and this
                #creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
                time.sleep(0.75)

                # If User is able to knock down the Kraken Health to 0 they Win the Game
                # Game Mode loop is broken
                if boss_health == 0:
                    statement_generator("😊 YOU WIN 😊", "!")
                    break
                # If User health is knocked down to 0 they Lose the Game
                # Game Mode loop is broken
                if user_health == 0:
                    statement_generator("😭 YOU LOSE 😭", "!")
                    break

    if game_mode == 3:

        statement_generator("Game Mode: HYDRA HEALTH 🐉", "!")

        #Change Boss Health and Max Bass Health (for Health Bar) to 300 since User chose the Hydra Game Mode
        boss_health += 300
        max_boss_health += 300

        while user_health and boss_health != 0:

            # Iterate through the dictionary (quiz_questions_and_answers) to get the key, value pair and also the index (used for the Question number)
            # Enumarate is used to give the value pairs in the quiz_questions_and_answers dictionary an index number
            # The index value from which the counter is to be started is at 1 for converstion into letters for the label in the answer alternatives
            for question_number, (question, unlabled_list_of_answers) in enumerate(
                    shuffled_list_of_quiz_questions_answers.items(), start=1):
                #Displays to the User the Question Number
                print()
                statement_generator(f"Question {question_number}", "#")
                print()
                #Ask Question to the User
                print(f"{question}?")
                # The correct answer to the given question is the first answer in the list of answers
                correct_answer = unlabled_list_of_answers[0]

                # sorted is used to change the order of the items in the list of answers
                # string.ascii_lowercase is used to get letters that label the list of answers
                # You combine letters and alternatives with zip() and store them in the dictionary
                labeled_list_of_answers = dict(zip(ascii_lowercase, sorted(unlabled_list_of_answers)))

                # label is the a, b, c, d that appears underneath the queston and corresponds to a value in the dictionaries (list of answers)
                for label, list_of_answers in labeled_list_of_answers.items():
                    print(f"{label}) {list_of_answers}")

                # Ask the User what their Choice will be to the given question
                user_answer = user_choice_checker("\nChoice? ")
                print()

                answer = labeled_list_of_answers.get(user_answer)

                # If the User's answer is equal to the correct answer the User gets the question right
                # Print Correct
                # -20 from the Hydra Health
                # Print User Health and Hydra Health with respective Health Bars
                # The number of questions answered increases by 1
                # The number of questions answered correct increases by 1
                # Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                # divided by the number of questions answered times by 100
                # The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                # the Game History and Statistics function
                if answer == correct_answer:
                    result = "Correct!"
                    print(f"Result ✨: {result}| Your Answer 🤓: {user_answer} | Correct Answer ✅: {correct_answer}")
                    print()
                    boss_health -= 20
                    print(f"USER HEALTH 🧑: {user_health} HP")
                    user_health_bar()
                    print(f"HYDRA HEALTH 🐉: {boss_health} HP")
                    boss_health_bar()
                    number_of_questions_answered += 1
                    questions_answered_correct += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100
                    print()

                # If the User's answer is not equal to the correct answer the User get the question wrong
                # Print Wrong and tell the User the correct answer
                # -20 from User Health
                # Print User Health and Hydra Health with respective Health Bars
                # The number of questions answered increases by 1
                # The number of questions answered incorrect increases by 1
                # Percent Correct and Percent Incorrect is equal the number of questions answered correct/incorrect
                # divided by the number of questions answered times by 100
                # The Percent Correct and Percent Incorrect is used to calculate the Game Statisitcs in
                # the Game History and Statistics function
                else:
                    result = "Wrong!"
                    print(f"Result ✨: {result} | Your Answer 🤓: {user_answer} | Correct Answer ✅: {correct_answer}")
                    print()
                    user_health -= 20
                    print(f"               USER HEALTH 🧑: {user_health} HP")
                    user_health_bar()
                    print(f"             HYDRA HEALTH 🐉: {boss_health} HP")
                    boss_health_bar()
                    number_of_questions_answered += 1
                    questions_answered_incorrect += 1
                    percent_correct = questions_answered_correct / number_of_questions_answered * 100
                    percent_incorrect = questions_answered_incorrect / number_of_questions_answered * 100
                    print()

                #time.sleep used so the User has time to read certain things and this
                #creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
                time.sleep(0.75)

                #If User is able to knock down the Hydra Health to 0 they Win the Game
                #Game Mode loop is broken
                if boss_health == 0:
                    statement_generator("😊 YOU WIN 😊", "!")
                    break
                #If User health is knocked down to 0 they Lose the Game
                #Game Mode loop is broken
                if user_health == 0:
                    statement_generator("😭 YOU LOSE 😭", "!")
                    break

    print()
    #Ask the User if the want to see their Game and Statistics
    see_statistics = yes_no_checker("Do you want to see your Game Statistics (Y/N)? ")

    #If the User inputs 'yes' they want to see their Game History and Statistics
    #Their Game History and Statistics will be displayed
    if see_statistics == "yes":
        game_statistics()
        print()

    #time.sleep used so the User has time to read certain things and this
    #creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
    time.sleep(0.75)

    #Ask the User if the want to see the Sources used to create this Game
    see_sources = yes_no_checker("Do you want to see the Sources used to create this Game (Y/N)? ")
    print()

    #If the User inputs 'yes' they want to see the Sources
    #The Sources used will be displayed
    if see_sources == "yes":
        quiz_sources()
        print()

    # time.sleep used so the User has time to read certain things and this
    # creates an atmosphere where the User does not feel rushed and overwhelmed about everything going on
    time.sleep(0.75)

    #Breaks the Game Loop
    #If User is able to knock down the Leviathen Health, Kraken Health or Hydra Health to 0
    #or If User health is knocked down to 0
    if boss_health == 0 or user_health == 0:
        break

#Heading for 'Thanks'
#This heading is used to draw the User attention and thank the User for playing the Quiz Quest Game
statement_generator("🙏 Thank You 🙏", "-")
print()

#Thanks the User for playing the Global Citizen Game
print("Thank You for playing the Global Citizen Game. \n"
      "By playing this Game you have become more aware of the Global environmental problem of Plastic Pollution \n"
      "and you may have learned positive ways/actions you can take to reduce plastic waste. \n"
      "Good Job 😊")


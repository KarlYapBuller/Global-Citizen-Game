#See Sources version 1
#Uses the yes_no_checker function from the 02_Played_Before_Yes_No_Checker_Game_Information_v1/v2/v3

#Yes/No Checker
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

#Quiz Sources Function
#Contains the sources URL in which the information in the
#passages of the Global Citizen Game Quiz is from on the Internet
def quiz_sources():
    print("Quiz Sources")
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

#Looped for testing purposes
#Looped to make it easier to get test cases
#The 'xxx' is the exit code to stop the loop
for item in range(1,20):
    # Ask the User if the want to see the Sources used to create this Game
    see_sources = yes_no_checker("Do you want to see the Sources used to create this Game (Y/N)? ")
    print()

    #If the User inputs 'yes' they want to see the Sources
    #The Sources used will be displayed
    if see_sources == "yes":
        quiz_sources()
        print()

    elif see_sources == "no":
        print("program continues")
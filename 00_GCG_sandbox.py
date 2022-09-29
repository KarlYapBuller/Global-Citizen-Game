health = 80      # Current Health (float so division doesn't make an int)
maxHealth = 200    # Max Health
healthDashes = 20  # Max Displayed dashes

def do_health():
  dashConvert = int(maxHealth/healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
  currentDashes = int(health/dashConvert)              # Convert health to dash count: 80/10 => 8 dashes
  remainingHealth = healthDashes - currentDashes       # Get the health remaining to fill as space => 12 spaces

  healthDisplay = '-' * currentDashes                  # Convert 8 to 8 dashes as a string:   "--------"
  remainingDisplay = ' ' * remainingHealth             # Convert 12 to 12 spaces as a string: "            "
  percent = str(int((health/maxHealth)*100)) + "%"     # Get the percent as a whole number:   40%

  print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
  print("         " + percent)                         # Print the percent

do_health()

l = list(QUESTIONS.items())
random.shuffle(l)
d = dict(l)
print(d)
#Change QUESTIONS to d in the for loop


def game_mode_input_checker(question):
  while True:

    # Error message
    error_message = "Error please input an Integer between 1 and 3 (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])"

    try:
      # It is an float input in the case the User inpurs a valid input but just with a .0
      response = float(input(question))

      # If User's response is 1 return the response
      if response == 1:
        return response

      # If User's response is 2 return the response
      elif response == 2:
        return response

      # If User's response is 3 return the response
      elif response == 3:
        return response

      # If User's response is not 1,2,3 print the <ERROR> message
      else:
        print(error_message)
        print()
        continue

    # If the User inputs an invalid value print the <ERROR> message
    except ValueError:
      print(error_message)
      print()

game_loop = ""
while game_loop == "":

    # Asks the User what game mode they want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])
    game_mode = game_mode_input_checker(
        "What game mode do you want to play (1. Leviathan [EASY] 2. Kraken [MEDIUM] 3. Hydra [HARD])? ")
    print()

    if game_mode == 1:

        while user_health and leviathan_health != 0:

            if leviathan_health == 0:
                print("You Win!")
                break

            if user_health == 0:
                print("You Lose!")
                break

    if leviathan_health == 0 or user_health == 0:
        break
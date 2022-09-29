health = 80      # Current Health (float so division doesn't make an int)
maxHealth = 200    # Max Health
healthDashes = 20  # Max Displayed dashes

def health_bar():
  dashConvert = int(maxHealth/healthDashes)            # Get the number to divide by to convert health to dashes (being 10)
  currentDashes = int(health/dashConvert)              # Convert health to dash count: 80/10 => 8 dashes
  remainingHealth = healthDashes - currentDashes       # Get the health remaining to fill as space => 12 spaces

  healthDisplay = '-' * currentDashes                  # Convert 8 to 8 dashes as a string:   "--------"
  remainingDisplay = ' ' * remainingHealth             # Convert 12 to 12 spaces as a string: "            "
  percent = str(int((health/maxHealth)*100)) + "%"     # Get the percent as a whole number:   40%

  print("|" + healthDisplay + remainingDisplay + "|")  # Print out textbased healthbar
  print("         " + percent)                         # Print the percent

health_bar()
#Heatlh Bar Component Version 1
# Current Health is a float so division does not make an integer
user_health = 50
# Max Health
max_health = 100
# Max Displayed dashes
health_dashes = 20

#Health Bar Function
def health_bar():
  #Get the number to divide by to convert health to dashes
  dash_convert = int(max_health/health_dashes)
  #Convert health to dash count
  current_dashes = int(user_health/dash_convert)
  #Get the health remaining to fill as space
  remaining_health = health_dashes - current_dashes

  # Convert current dashes to 8 dashes as a string
  health_display = '-' * current_dashes
  # Convert the remaining health to spaces as a string
  remaining_display = ' ' * remaining_health

  # Print out textbased healthbar
  print("|" + health_display + remaining_display + "|")
  # Print the User's Health
  print("          {}".format(user_health))

#Print the Health Bar
health_bar()
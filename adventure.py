import os
os.system('clear')
print("         _    _      _                            _                      ")
print("        | |  | |    | |                          | |                     ")
print("        | |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___                ")
print("        | |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \               ")
print("        \  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) |              ")
print("         \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/               ")
print("")
print("")
print("")
print("")
print("  sSSSSs    sSSs_sSSs      sSSs   .S    S.    .S     S.    .S   .S_sSSs  ")
print(" d%%%%SP   d%%SP~YS%%b    d%%SP  .SS    SS.  .SS     SS.  .SS  .SS~YS%%b ")
print("d%S'      d%S'     `S%b  d%S'    S%S    S%S  S%S     S%S  S%S  S%S   `S%b")
print("S%S       S%S       S%S  S%|     S%S    S%S  S%S     S%S  S%S  S%S    S%S")
print("S&S       S&S       S&S  S&S     S%S SSSS%S  S%S     S%S  S&S  S%S    S&S")
print("S&S       S&S       S&S  Y&Ss    S&S  SSS&S  S&S     S&S  S&S  S&S    S&S")
print("S&S       S&S       S&S  `S&&S   S&S    S&S  S&S     S&S  S&S  S&S    S&S")
print("S&S sSSs  S&S       S&S    `S*S  S&S    S&S  S&S     S&S  S&S  S&S    S&S")
print("S*b `S%%  S*b       d*S     l*S  S*S    S*S  S*S     S*S  S*S  S*S    S*S")
print("S*S   S%  S*S.     .S*S    .S*P  S*S    S*S  S*S  .  S*S  S*S  S*S    S*S")
print(" SS_sSSS   SSSbs_sdSSS   sSS*S   S*S    S*S  S*S_sSs_S*S  S*S  S*S    S*S")
print("  Y~YSSY    YSSP~YSSY    YSS'    SSS    S*S  SSS~SSS~S*S  S*S  S*S    SSS")
print("                                        SP                SP   SP        ")
print("                                        Y                 Y    Y         ")

guest = input("What is your name? ")
print("Welcome " + guest + "!")
print("")

option = 0
while option != 'q':
  os.system('clear')
  print("")
  print("What adventure do you want today?")
  print("Enter 1 for dragon riding")
  print("Enter 2 for dragon poo duty")
  print("Enter q to leave Goshwin")
  print("")

  option = input("Your choice? ")
  print("")

  if option == '1':
    print("Excellent! I hope you brought a saddle.")
    print("")

    color = input("What color dragon would you like to ride? ")
    print(color + " is an excellent choice")
  elif option == '2':
    print("Excellent! Dragon poo is quite smelly.")
    print("")

    tool = input("Would you like to use a spork or a chopsticks to pick up dragon poo? ")
    print("Dang, we just ran out of " + tool +". You'll have to use your hand instead.")
    print("")
  elif option == 'q':
    print("I'm sorry to see you leave. The next boat off the island leaves in 30 minutes. Don't get eaten by a dragon before you go.")
  else:
    print("Sorry, we don't have that adventure around here. Maybe you should go visit the land of boring cats.")
  
  if option != 'q':
    print("")
    input("Press Enter to continue")

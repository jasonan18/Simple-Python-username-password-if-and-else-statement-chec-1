def usernameCreation():
  global username     
  # global is used in front of strings within the functions to make sure that they can be used everywhere and not just within the specified function
  username = str(input("Set your username: "))
  print("Your username is " + username)
  usernameCharLimit = len(username)
  if (username == '') or (username == ' '):
    print("Please try again. Usernames cannot be blank.")
    usernameCreation()
  if (usernameCharLimit < 4):
    print("Please try again. Your username needs to have at least 4 characters.")
    usernameCreation()

  

def passwordCreation():
  global password  
  password = str(input("Set your password: "))
  passwordCharLimit = len(password)
  print("Your password is " + password)
  if (password == '') or (password == ' '):
    print("Please try again. Passwords cannot be blank.")
    passwordCreation()
  if (passwordCharLimit < 8):
    print("Please try again. Your password needs to be at least 8 characters.")
    passwordCreation()

# I could just do an else statement saying "please try again" which would reduce the code, but since you create your own login and password, I wanted to go further and create code which compares your incorrect username or password.
def login():
  global usernameCheck 
  global passwordCheck
  usernameCheck = str(input("\nusername : "))
  passwordCheck = str(input("password : "))
  if (usernameCheck == username) and (passwordCheck == password):
    print("You've logged in successfully! Welcome, " + username + ".")
  elif (usernameCheck == username) and (passwordCheck != password):
    print("This is the incorrect password. Please try again")
    passwordCheck = str(input("password : "))
    if (passwordCheck == password):
      print("You've logged in successfully! Welcome, " + username + ".")
    else:
      print("Please try again.")
      login()
  elif (usernameCheck != username) and (passwordCheck == password):
    print("Your username has been inputted incorrectly. Please try again.")
    usernameCheck = str(input("username : "))
    if (usernameCheck == username):
      print("You've logged in successfully! Welcome, " + username + ".")
    else:
      print("Please try again.")
      login()

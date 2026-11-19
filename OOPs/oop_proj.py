class chatbook:
  def __init__(self):
    self.email=''
    self.password=''
    self.loggedIn=False
    self.menu()

  def menu(self):
    ch = input("""What do you want?
    1. press 1 for signUp
    2. press 2 for signIn
    3. press 3 for post
    4. press 4 to send post to friend
    5. press anything to exit
    
    ->""")

    if ch == "1":
      self.signUp()
    elif ch == "2":
      self.signIn()
    elif ch == "3":
      self.post()
    elif ch == "4":
      self.send_to_friend()
    else:
      exit()

  def signUp(self):
    self.email = input("enter the email: ")
    self.password = input("enter the password: ")
    print("User signed Up\n")
    self.menu()


  def signIn(self):
    if self.email=='':
      print("signUp first\n")
      self.menu()
    else:
      uname = input("enter your email: ")
      pwd = input("enter your password: ")
      if self.email==uname and self.password == pwd:
        print("User signed In\n")
        self.loggedIn= True
      else: 
        print("Please input correct credentials!\n")
      self.menu()

  def post(self):
    if self.loggedIn:
      content = input("\nwrite the content for your post: \n")
      print(f"Your post: {content}\n")
    else:
      print("First logIn to your account!\n")
    self.menu()

  def send_to_friend(self):
    if self.loggedIn:
      frnd = input("\nTo whom you want to send the post:")
      print(f"The post has been sent to the {frnd}\n")
    else:
      print("First logIn to your account!\n")
    self.menu()


user1 = chatbook()
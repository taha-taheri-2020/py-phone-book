class Phone_number:
  def __init__(self,phone,text):
    self.phone = phone
    self.text  = text
while True:
  user_input = input("Enter your command: (a: add, d: delete, e: edit, g: get, q: quit) ")

  if user_input == "a":
    pass
  elif user_input == "d":
    pass
  elif user_input == "e" :
    pass
  elif user_input == "g":
    phones = open("phones.txt","r")
    print(phones.read())
    phones.close()
  elif user_input == "q":
    exit(0)
  else:
    print("this command is not exist in this app")

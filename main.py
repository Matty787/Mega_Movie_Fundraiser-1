print("Hello world")

def not_blank(question):
  valid = False

  while not valid:
    response = input(question)

    if response != "":
      return response
    else:
      print("Sorry - this can't be blank, "
                 "please enter your name")


# Main routine goes here


#Start loop

# initialise loop so that is runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:

  #Get details...
  name = input("Name: ")
  count += 1
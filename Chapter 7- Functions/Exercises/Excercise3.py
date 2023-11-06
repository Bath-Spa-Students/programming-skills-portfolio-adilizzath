def make_shirt (size,message):
  print ("The size and the message for the given shirt is: ", size, message)
  
# Call the make_shirt function with specific size and message arguments.
make_shirt(5,"BSU")

#OR

# Alternatively, interactively get the shirt size and message from the user using input().
# Store the values entered by the user in the siz and msg variables.
siz = int(input ("Enter your shirt size: "))
siz=int(input("enter your shirt size :" ))
msg=input ("enter the message! :")

# Call the make_shirt function with the values entered by the user.
make_shirt(siz,msg)
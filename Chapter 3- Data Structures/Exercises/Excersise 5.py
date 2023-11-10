# First section: Inviting guests using a loop
names = ["adhil", "Alen", "Karthikeyan", "Shaan"]
for i in names:
    print(i + ", we are gladly inviting you to join us at a dinner party.")

# Second section: Inviting guests individually with messages
Guests = ["adhil", "shad", "rubi"]
msg1 = "Hello " + Guests[0] + ", you are invited to the dinner."
msg2 = "Hello " + Guests[1] + ", you are invited to the dinner."
msg3 = "Hello " + Guests[2] + ", you are invited to the dinner."

# Printing individual invitations
print(msg1)
print(msg2)
print(msg3)

# Modifying the guest list and updating an invitation message
print("\nSadly, " + Guests[2] + " cannot come to the party.")
Guests[2] = "rubi"  # Correcting the name

msg1 = "\nHello " + Guests[0] + ", you are invited to the dinner."
msg2 = "\nHello " + Guests[1] + ", you are invited to the dinner."

# Printing updated invitations
print(msg1)
print(msg2)

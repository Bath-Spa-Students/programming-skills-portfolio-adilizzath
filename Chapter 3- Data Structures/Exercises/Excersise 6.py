guests=["connor","desmond","shay"]

print("Hey i would like to call you for dinner mr.",guests[0])
print("Mr."+guests[1]+",you are invited to our dinner")
print("Mr."+guests[2]+",i would like to call you for dinner")

#or

print("As per the restaurant,there is a space only for two guests")
#remove guest from the list using pop() until only two names remain
for _ in range (len(guests) - 2):
    removed_guest= guests.pop()
    print(f"sorry,{removed_guest},i cant invite you to dinner.")

#Print a message to the two people who are still in your list
for guest in guests:
    print(f"{guest},you are still invited to dinner.")

#Use del to remove the last two names from your list

del guests[:]

#print your list to make sure its empty
print("Guest list:",guests)
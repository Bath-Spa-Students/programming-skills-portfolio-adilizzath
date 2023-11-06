#create a list of dictionaries representing different pets

my_pets=[
    {"kind":"dog","owner":"Arun"},
    {"kind":"cat","owner":"Adhil"},
    {"kind":"fish","owner":"Daisy"},
    {"kind":"parrot","owner":"Aman"},
]

#loop through the list and print information about each pet

for pet in my_pets:
    print(f"kind of animal:{pet['kind']}")
    print(f"Owner's name:{pet['owner']}\n")

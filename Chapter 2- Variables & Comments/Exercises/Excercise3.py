#Tidy up the code to make it easier to understand

#Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.

#Print the name once, so the whitespace around the name is displayed. 

#Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

person_name = "\t   \nmohamed adil\t   \n"

# Print the name with whitespace
print("Name with whitespace:")
print(person_name)

# Print the name using lstrip(), rstrip(), and strip()
print("\nName using lstrip():")
print(person_name.lstrip())

print("\nName using rstrip():")
print(person_name.rstrip())

print("\nName using strip():")
print(person_name.strip())


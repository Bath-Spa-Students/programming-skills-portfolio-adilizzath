# Initial string with leading and trailing whitespaces
person_name = "\t   \nmohamed adil\t   \n"

# Print the name with whitespace
print("Name with whitespace:")
print(person_name)

# Print the name using lstrip(), rstrip(), and strip()

# Using lstrip() to remove leading whitespaces
print("\nName using lstrip():")
print(person_name.lstrip())

# Using rstrip() to remove trailing whitespaces
print("\nName using rstrip():")
print(person_name.rstrip())

# Using strip() to remove both leading and trailing whitespaces
print("\nName using strip():")
print(person_name.strip())

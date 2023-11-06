#defining a Function
def describe_city (name, country="INDIA"):
 print(f'{name} is in {country}')

# Call the function for three different cities
describe_city("Thrissur")
describe_city ("Chennai")
describe_city("New Year", "America")
# This will use new default country value
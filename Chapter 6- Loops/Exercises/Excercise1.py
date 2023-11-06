# a variable that stores pizza toppings
toppings=[]

while True:
    #prompt the user to add toppings
    topping=input("Enter the pizza topping:(or type quit to quit the code)")

#if the user type quit the code will break
    if topping == 'quit':
        break
#add the topping to the list "toppings"
    toppings.append(topping)

print("these are your toppings")
for i in toppings:
    print(i)
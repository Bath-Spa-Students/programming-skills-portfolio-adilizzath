# first ask for the user age 
age=int(input("enter our age: "))

#create loop which shows the ticket price on the basis of age 

for i in age:
    if i<3:
         print("your ticket is free!")
    elif i>3 and i<12:
         print("your ticket cost 10$")
    else:
         print("your ticket cost 15$")
    

# Price of a USB stick in pounds
usb_price = 6

# Amount in pounds the person has
pound = 50

# Calculating how many USB sticks can be bought
shecanget = pound // usb_price

# Calculating the amount of change the person will receive
p_change = pound - shecanget * usb_price

# Printing the results
print("Sticks she can buy:", shecanget)
print("The amount she will get back:", p_change)

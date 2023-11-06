# create a list of sandwich orders with 'pastrami' appearing atleast 3 times 

sandwich_orders=['tuna','turkey','pastrami','bacon','ham','cheese','pastrami','club','vegeterian','pastrami']

# create a empty list of store finished sandwiches
finished_sandwiches=[]

#print a message about running out of pastrami
print("sorry,pastrami is out of stock")

#remove all occurences of 'pastrami' from sandwich orders 
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

#loop through the list of sandwich orders
while sandwich_orders:
    current_order=sandwich_orders.pop(0) #get the first order
    print(f"i made your {current_order}sandwich.")
    finished_sandwiches.append(current_order)

#print the list of finished sandwiches
print("\nlist of finished sandwiches:")
for sandwich in  finished_sandwiches:
    print(sandwich)


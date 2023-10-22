names=["adhil","Alen","Karthikeyan","Shaan"]
for i in names:
    print(i,",We are galdly inviting you to join us on a dinner party")

#or

Guests=["adhil","shad","rubi"]
msg1=("hello "+ Guests[0]+",you are invited to the dinner")
msg2=("hello "+ Guests[1]+",you are invited to the dinner")
msg3=("hello "+ Guests[2]+",you are invited to the dinner")

print(msg1)
print(msg2)
print(msg3)

print("\nsadly "+Guests[2]+",cannot come to the party")
Guests[2]="rubi"

msg1=("\nhello "+Guests[0]+",you are invited to the dinner")
msg2=("\nhello "+Guests[1]+",you are invited to the dinner")

print(msg1)
print(msg2)


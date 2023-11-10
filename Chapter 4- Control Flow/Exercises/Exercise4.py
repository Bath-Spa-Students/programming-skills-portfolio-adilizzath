age = 30  # You can change this value to test different ages.

if age < 2:
    print("The person is a baby.")  # If age is less than 2, the person is considered a baby.
elif age < 4:
    print("The person is a toddler.")  # If age is between 2 (inclusive) and 4 (exclusive), the person is a toddler.
elif age < 13:
    print("The person is a kid.")  # If age is between 4 (inclusive) and 13 (exclusive), the person is a kid.
elif age < 20:
    print("The person is a teenager.")  # If age is between 13 (inclusive) and 20 (exclusive), the person is a teenager.
elif age < 65:
    print("The person is an adult.")  # If age is between 20 (inclusive) and 65 (exclusive), the person is an adult.
else:
    print("The person is an elder.")  # If age is 65 or older, the person is considered an elder.

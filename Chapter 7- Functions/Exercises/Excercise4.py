def make_shirt (size="large", message="I love Python"):
 print(f"Creating a {size} shirt with the message: {message}")

# Make a large shirt with the default message
make_shirt ()

# Make a medium shirt with the default message
make_shirt(size="medium")

# Make a shirt of any size with a different message
make_shirt(size="small", message="Python is the best programming language!")
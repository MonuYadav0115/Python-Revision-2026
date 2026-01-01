
# List and Tuple Generator

# Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.

User = input("enter here:")

list = User.split(",")

tuple = tuple(list)

print("List here:",list)

print("Tuple here:",tuple)
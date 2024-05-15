# Ask user
userInput = input("Enter the number or range to check.\n")

# Function to check if number is even or odd
def checkEven(theNumber):
    if int(theNumber) % 2 == 0:
        print(f"{theNumber} is even")
    else:
        print(f"{theNumber} is odd")

# Parse user input
items = userInput.split("-")
if "-" in userInput:
    for itemem in range(int(items[0]), int(items[1]) + 1):
        checkEven(itemem)
else:
    checkEven(userInput)

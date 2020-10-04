# definition of converting a string to a list
def Convert(string):
    li = list(string.split(" "))
    return li


# Getting user input
Equation = input("What would you like to calculate? ")

# Variable hellhole
EqList = (Convert(Equation))
num1 = int(EqList[0])
num2 = int(EqList[2])
operator = EqList[1]

# Defining which operator and calculating
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    result = num1 / num2

print("")

# Print the result with bold text
print("\033[1m" + str(result) + "\033[0m")

def add(number_1, number_2):
    return number_1 + number_2

def substract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def division(number_1, number_2):
    return number_1 / number_2

def mainMenu():
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiply")
    print("4. Division")

def getValidNumber(inputStr):
    while True:
        try:
            number = float(input(inputStr))
            return number
        except Exception as e:
            print("You must input a number")

iterator = True
print("*** Welcome to Python simple calculator ***\n")
while iterator:
    number_1 = getValidNumber("Enter first number: ")
    number_2 = getValidNumber("Enter second number: ")
    mainMenu()

    while True:
        userOption = getValidNumber("Enter the operation: ")

        if userOption in [1,2,3,4]:
            break
        else:
            print("Invalid option.")

    if userOption == 1:
        print(add(number_1, number_2))

    elif userOption == 2:
        print(substract(number_1, number_2))

    elif userOption == 3:
        print(multiply(number_1, number_2))

    elif userOption == 4:
        print(division(number_1, number_2))

    else:
        print("Invalid option.")

    
    while True:
        loop = input("Do you want to continue (Y/N): ")
        loop = loop.lower()
        if loop == "y":
            break
        elif loop == "n":
            iterator = False
            print("Thank you for using the Python simple calculator ❤️")
            break
        else:
            print("Invalid input")

    
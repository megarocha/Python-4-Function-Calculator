def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


print("Choose an operation you would like to use: \n"
      "1). to Add \n"
      "2). to Subtract \n"
      "3). to Multiply \n"
      "4). to Divide \n")

choice = int(input("Select an operation: 1, 2, 3, 4"))

number1 = float(input("Enter a number you want to use: "))
number2 = float(input("Enter another number you want to use: "))

if choice == 1:
    print(number1, "+", number2, "=", add(number1, number2))

elif choice == 2:
    print(number1, "-", number2, "=", subtract(number1, number2))

elif choice == 3:
    print(number1, "*", number2, "=", multiply(number1, number2))

elif choice == 4:
    print(number1, "/", number2, "=", divide(number1, number2))

else:
    print("The operator you have chosen is currently not available. \n"
          "Please try again.")
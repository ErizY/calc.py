number1_str = input(" First number: ")
number1 = int(number1_str)

number2_str = input("Second number: ")
number2 = int(number2_str)

operation = input("Operation [+, -, *, /]: ")

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2
elif operation == "*":
    combination = number1 * number2
elif operation == "/":
    if number2 == 0:
        combination = "you can't divide by zero"
    else:
        combination = number1 / number2
else:
    combination = "ERROR ... '" + operation + "' unrecognised"

combination_str = str(combination)
print("Answer: " + combination_str)

print()
input("Press return to continue ...")

import re


def calc(first_number: float, second_number: float, operator: str):
    if(operator == "+"):
        return first_number + second_number
    elif(operator == "-"):
        return first_number - second_number
    elif(operator == "*"):
        return first_number * second_number
    elif(operator == "/"):
        return first_number / second_number
    else:
        print("The given formular is invalid")
        exit()


formular = input("Enter your formular (+, -, *, /): ").replace(" ", "")
formular_parts = formular.replace(
    "+", " +").replace("-", " -").replace("*", " *").replace("/", " /").split(" ")

result = None

for part in formular_parts:
    if result == None:
        result = float(part)
    else:
        operator = part[0]
        try:
            part_as_float = float(re.sub("[^0-9]", "", part))
        except ValueError:
            print("The given formular is invalid")
            exit()
        result = calc(result, part_as_float, part[0])

print("Result is {0}".format(result))

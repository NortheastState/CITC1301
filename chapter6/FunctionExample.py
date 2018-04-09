# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program illustrate how to define and use
#               functions. It will also demonstrate how to
#               return values from a function.
#
# ===============================================================

# here is a simple function definition that does not return any values
#   and does not use any parameters
def renderHeader():
    print("{0:*^40}".format(""))
    print("{0:^40}".format("Project Header"))
    print("{0:^40}".format("Ms. Foobar"))
    print("{0:*^40}".format(""))


def isfloat(value):
    results = True
    try:
        float(value)
    except ValueError:
        results = False
    return results


def validateNumber(number):
    results = True
    if isfloat(number):
        results = True
    elif number.isdigit():
        results = True
    else:
        results = False
    return results

# use main to check input values
def main():
    while True:
        number = input("Please enter a valid number: ")
        if validateNumber(number):
            break
        else:
            continue

    age = validateNonNegativeNumber("Please enter your age: ")
    kids = validateNonNegativeNumber("Please enter the number of children you have: ")        
    salary = validateNonNegativeNumber("Please enter your yearly earnings, in dollars: ")     

# Here is an example of code reuse. There may be many times that you
#   would ant to validate input to be a positive number
def validateNonNegativeNumber(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 0:
            print("Sorry, your response must not be negative.")
            continue
        else:
            break
    return value


renderHeader()
main()

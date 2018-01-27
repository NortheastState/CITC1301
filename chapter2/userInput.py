# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program shows how to get input from the user
#              and use that input in a program
#
# ===============================================================

def main():
    # in python we can use the input function to get user input
    # and also prompt the user with a message
    firstName = input("Enter your first name please: ")

    print("Thank you " + str(firstName))

    hoursWorked = input("Enter the number of hours that you worked this week: ")
    wageRate = input("Enter your wage rate per hour: ")

    total = float(hoursWorked) * float(wageRate)
    print("Your check will be: ${0:.2f}".format(total))

main()
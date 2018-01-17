#===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program asks the user for three test scores,
#              then calculates the average of those test scores.
#              It is not required to set the number of significant
#              digits after the decimal point. We will learn that
#              when formatting output.
#
#===============================================================


def main():
    print("*******************************************************")
    print("This program computes the average of three test scores.")
    print("*******************************************************")
    print()

    # create three variables to store the three test scores enter by the user
    # and prompt the user for the three test scores
    # Note the eval for converting all numbers entered into respective variable values.
    # If we "Cast" the values then we would have to get the user input on 3
    # separate lines. Also, remember that eval() is unsafe to use.
    testOne, testTwo, testThree = eval(input("Enter three test scores, each one separated by a comma: "))

    # find the average by adding all test scores and dividing by 3
    # Unlike some other languages, integer division results in a floating
    # point number
    average = (testOne + testTwo + testThree) / 3

    # output the results
    print("The average of the test scores is: " + str(average))


main()


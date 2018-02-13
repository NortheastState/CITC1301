# ===============================================================
#
#        Name: David Blair
#        Date: 02/13/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program shows an example of how you might
#              use conditionals to do bounds checking
#
# ===============================================================

# the main function handles getting input from the user
# and outputting the results back to the user
def main():
    # prompt user for a valid grade
    grade = input("Enter a grade between 0 and 100: ")
    # check input to between 0 and 100
    if grade < 0:
        print("Invalid entry")
    elif grade > 100:
        print("Invalid entry")
    else:
        # print the results of converting a numeric grade to a letter grade
        print(calculateLetterGrade(grade))

# process the grade passed in by converting the numeric grade to a letter grade
# and then returning that letter grade to the calling function
def calculateLetterGrade(grade):
    # declaring the local variable letterGrade is not
    # required for python but is good programming style
    letterGrade = ""
    if grade >= 90:
        letterGrade = "A"
    elif grade >= 80:
        letterGrade = "B"
    elif grade >= 70:
        letterGrade = "C"
    elif grade >= 65:
        letterGrade = "D"
    else:
        letterGrade = "F"
    return letterGrade

main()
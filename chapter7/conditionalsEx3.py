# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program explores conditionals using elif
#
# ===============================================================


def showProgramHeader():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Conditional Constructs 3"))
    print("++++++++++++++++++++++++++++++++++++++++")


def main():
    print("\n\t")
    letterGrade = ""
    grade = input("\tEnter a test grade 0 - 100: ")

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

showProgramHeader()
print("\tThe letter grade conversion is: " + main())

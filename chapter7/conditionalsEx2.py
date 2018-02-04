# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program explores conditionals using else
#
# ===============================================================

def showProgramHeader():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Conditional Constructs 2"))
    print("++++++++++++++++++++++++++++++++++++++++")


def main():
    print("\n\n\t")
    letterGrade = ""
    grade = input("Enter a test grade 0 - 100: ")

    if grade >= 90:
        letterGrade = "A"
    else:
        letterGrade = "Not A"

    return letterGrade


showProgramHeader()
print(main())


# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program introduces conditional constructs
#
# ===============================================================


def showProgramHeader():
    print("++++++++++++++++++++++++++++++++++++++++")
    print("{0:^40}".format("Conditional Constructs"))
    print("++++++++++++++++++++++++++++++++++++++++")


def main():
    print("\n\n\t")
    madeA = False
    grade = input("Enter a test grade 0 - 100: ")
    if grade >= 90:
        print("That is an A, good job.")
        madeA = True

    return madeA


showProgramHeader()
results = main()

if results != True:
    print("The test grade was not an A.")

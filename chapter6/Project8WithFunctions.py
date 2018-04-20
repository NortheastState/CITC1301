
def findMax(grades):
    maxVal = len(grades)
    if maxVal > 0:
        temp = grades[0]
        for i in range(maxVal):
            if temp < grades[i]:
                temp = grades[i]

        print("{0:>28} {1}".format("Highest grade recorded:", temp))


def findMin(grades):
    maxVal = len(grades)
    if maxVal > 0:
        temp = grades[0]
        for i in range(maxVal):
            if temp > grades[i]:
                temp = grades[i]

        print("{0:>28} {1}".format("Lowest grade recorded:", temp))


def findAvg(grades):
    maxVal = len(grades)
    if maxVal > 0:
        temp = 0
        for i in range(maxVal):
            temp = temp + grades[i]

        avg = float(temp) / len(grades)
        print("{0:>28} {1:3.2f}".format("Average grade:", avg))


def loadGrades():

    grades = []
    numberOfValues = input("\t\tHow many values will you enter? ")
    print()
    if numberOfValues.isdigit():
        numGrades = int(numberOfValues)

        for i in range(numGrades):

            strGrade = input("\t\tEnter grade " + str(i + 1) + ": ")
            if strGrade.isdigit():
                intGrade = int(strGrade)
                grades.append(intGrade)
            else:
                exit(0)

    return grades


agrades = loadGrades()
if len(agrades) > 0:
    findMax(agrades)
    findMin(agrades)
    findAvg(agrades)


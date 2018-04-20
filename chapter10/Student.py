# ===============================================================
#
#        Name: David Blair
#        Date: 04/14/2018
#      Course: CITC 1301
#     Section: A70
# Description: This file is an example of a class in Python.
#
# ===============================================================


class Student:

    firstName = ''
    lastName = ''
    studentID = ''
    #  grades = []  # Careful, mutable types are shared between all object (static)

    def __init__(self, firstName, lastName, studentID):
        self.firstName = firstName
        self.lastName = lastName
        self.studentID = studentID
        self.grades = []

    def getFirstName(self):
        return self.firstName

    def setFirstName(self, firstName):
        self.firstName = firstName

    def getLastName(self):
        return self.lastName

    def setLastName(self, lastName):
        self.lastName = lastName

    def getStudentID(self):
        return self.studentID

    def setStudentID(self, studentID):
        self.studentID = studentID

    def addAGrade(self, grade):
        self.grades.append(grade)

    def getGrades(self):
        return self.grades

    def getGradeAverage(self):
        total = 0
        average = 0.0
        if len(self.grades) > 0:
            for grade in self.grades:
                total += grade
            average = total / len(self.grades)
        return average

    def getMaxGrade(self):
        temp = 0
        if len(self.grades) > 0:
            temp = self.grades[0]
            for grade in self.grades:
                if temp < grade:
                    temp = grade
        return temp

    def getMinGrade(self):
        temp = 0
        if len(self.grades) > 0:
            temp = self.grades[0]
            for grade in self.grades:
                if temp > grade:
                    temp = grade
        return temp

    def toString(self):
        return "First Name: " + self.firstName + ", Last Name: " + self.lastName + ", ID: " + self.studentID \
               + ", Grades: " + str(self.grades)

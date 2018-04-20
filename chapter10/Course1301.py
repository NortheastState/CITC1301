# ===============================================================
#
#        Name: David Blair
#        Date: 04/14/2018
#      Course: CITC 1301
#     Section: A70
# Description: You can think of this Python file as a "driver"
#               that tests the Student class. It can also be
#               thought of as a container that hold a course
#               full of Students.
#
# ===============================================================
from Student import Student


def main():
    # create a Python list
    courseCISP1301 = []

    # create a few new Student objects from the class template
    student1 = Student("Foo", "Bar", "A1")
    student2 = Student("Bo", "Cephus", "A2")
    student3 = Student("Curtis", "Loew", "A3")

    # add students to the list
    courseCISP1301.append(student1)
    courseCISP1301.append(student2)
    courseCISP1301.append(student3)

    while True:
        sID = input("Enter the student ID you want to add a grade: ")
        # now add a few grades for Student with ID of 90012345
        for student in courseCISP1301:
            if student.getStudentID() == sID:
                gradeItem = int(input("Enter a grade: "))
                student.addAGrade(gradeItem)
        done = input("Type 'Y' to enter another grade? ")
        if done != 'Y':
            break

    print()
    # output all students
    for student in courseCISP1301:
        print(student.toString(), student.getGradeAverage(), student.getMaxGrade(), student.getMinGrade())


main()

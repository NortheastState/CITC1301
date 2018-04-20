# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program illustrates how to use Python loops
#
# ===============================================================


def forLoopExample(alist):
    mylist = alist
    for i in range(len(mylist)):
        print(mylist[i])

    print()
    for i in range(2, 5):  # range from 2 thru 5
        print(mylist[i])

    print()
    for i in range(2, 10, 2):  # range start at 2, go to 10, increment by 2
        print(mylist[i])


def forEachLoopExample(alist):
    mylist = alist
    print()
    for value in mylist:  # print the value in each cell, one at a time
        print(value)


def whileLoopExample(alist):
    counter = len(alist)
    print()
    while counter > 0:  # the "while" loops as long as it evaluates to true
        counter = counter - 1
        print(alist[counter])


def whileBreakContinue():
    total = 0
    while True:
        results = input("Enter a value, or (Q)uit: ")
        if results == 'Q':
            break
        else:
            print("you entered", total)
            continue


def main(mylist):
    forLoopExample(mylist)
    forEachLoopExample(mylist)
    print()


alist = [1, 6, 3, 2, 9, 50, 24, 11, 2]
main(alist)

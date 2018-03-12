# ===============================================================
#
#        Name: David Blair
#        Date: 03/10/2018
#      Course: CITC 1301
#     Section: A70
# Description: Read in a file one line at a time or
#              read a file into a list
#
# ===============================================================


def readFromFileUsingReadLines():

    try:
        # create a file object to write to test.txt file
        # note the "r" in the parameter list.
        myFile = open("test.txt", "r")

        # read in all contents of file
        data = myFile.readlines()

        # print out the contents
        # but since all data is in a list, we can access
        # the lines using the array syntax
        print()
        print(len(data))
        print(data[0])
        print(data[1])

        # I can use a for loop to look through the list
        fileLen = len(data)
        for i in range(fileLen):
            print(data[i])

        myFile.close()

    except:

        print("There was a problem with a file read operation")


def readFromFileUsingReadLine():

    try:
        # create a file object to write to test.txt file
        # note the "r" in the parameter list.
        myFile = open("test.txt", "r")

        # read in a line at a time using a for loop
        for line in myFile:
            print(line)

        myFile.close()

    except:

        print("There was a problem with a file read operation")


def main():
    readFromFileUsingReadLines()
    print()
    readFromFileUsingReadLine()


main()
# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program does what? 
#
# ===============================================================


def main():

    myGreeting = "Hello Foobar!"    # create a string variable

    print("[0]:", myGreeting[0])    # print the first character
    print("[2]:", myGreeting[2])    # print the THIRD character
    print("String Length:", len(myGreeting))    # get the string length
    strLength = len(myGreeting)     # notice the string length is N - 1
    print("[len]:", myGreeting[strLength - 1])  # print the last character

    print()
    print("[-1]:", myGreeting[-1])  # negative indexes are also allowed

    print("[-3]:", myGreeting[-3])  # negative indexes are also allowed

    # The following code will throw an IndexError exception
    # print("What happens when accessing cells over N - 1 [100]: ", myGreeting[100])

main()

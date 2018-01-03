#===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program explores some of the python math
#              library.
#
#===============================================================

import math

#---------------------------------------------------------------
#         Method: main
#     Parameters: None
#    Description: Class examples - more fun with math
#--------------------------------------------------------------
def main():

    #lets look at a simple for loop
    #that uses several of the math methods
    for value in [10,20,30,40,50, 60, 70, 80, 90]:
        print("radians for", value, "is", math.radians(value))
        print("sine for", value, "is", math.sin(math.radians(value)))
        print(value, "to the 1/2 power is", math.pow(value, .5))
        print("the factorial of", int(value / 10), "is", math.factorial(int(value / 10)))
        print()

    #here are two often used constants
    print("the value of pi is:", math.pi)
    print("the value of e is", math.e)

main()


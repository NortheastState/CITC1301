#===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program outputs a simple hello message to
#              the console window using a variable.
#
#===============================================================


#---------------------------------------------------------------
#         Method: main
#     Parameters: greeting: String
#    Description: Print a greeting to the console window from
#                 the parameter passed into the method.
#--------------------------------------------------------------
def main(greeting: object):
    print(greeting)

# create a variable to hold the input from the user
inputGreeting = input("Please enter a greeting: ")

# call the main method sending the greeting
main(inputGreeting)


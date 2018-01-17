#===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program shows how to get input from the user
#              using the console window. It also will demonstrate
#              using the assignment operator.
#
#===============================================================

# A variable is a named memory location where we can use to
# hold information that we can use anywhere in the scope it
# is declared.

# The assignment statement has the following form
# <variable> = <expression>
# variables
hourlyWage = 11.35
hoursWorked = 40.0

# process
weeklyIncome = hourlyWage * hoursWorked

# output results
print("Initial weekly income:", weeklyIncome)


# If we change the value that is in the variable, the
# old value is blown-away, or replaced with the new value
hourlyWage = 12.55

# process
weeklyIncome = hourlyWage * hoursWorked

# output results
print("Weekly income after raise:", weeklyIncome)

# Getting input from the user from a console window
# is accomplished using the built in method "input"
# Here is the statement form:
# <variable> = input(<prompt>)
# The program will pause and wait for the user to enter
# some text before proceeding.
# Example:
firstName = input("Please enter your first name: ")
print("You entered:", firstName)

# It is important to note that the value returned by the input
# method is a text value, or a string. So if I try to do something
# arithmetic with the returned value, I will get a "Can't convert" error.
# Example:
anAmount = input("Enter an amount: ")
# we must "CAST" the input to an integer in order to do math.
print(int(anAmount) + 3)

# it is important to realize that case matter in python
# So firstName and FirstName are two different variable names
# print(FirstName) causes and error for example

# eval()
# There is a python method call eval() that will convert the input
# into a number. But, due to security reasons, we will not use
# eval(), instead, we will cast the input into whatever we need.
# We will need a way to test the input before we try to cast it
# to a particular data type. We will do this later.



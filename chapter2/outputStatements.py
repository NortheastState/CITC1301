#===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program give some examples of outputing
#              to the console window.
#
#===============================================================

# The print method shown below is a python built-in method
# We can use it to output expression results or just plain text.
# Here, the results from 3 * 4 will be printed to the console
print(3 * 4)

# Notice the difference between this print statement and the
# one above
print("3 * 4")

# Notice how every print statement is followed by a newline
# that you do not have to put in yourself. Also notice below
# that each parameter is seperated by a space in the console output
# without you having to place a space in the string.
# This: "The answer is:", 5 * (3 / 12.6)
# Instead of this: "The answer is :", 5 * (3 / 12.6)
print("The answer is:", 5 * (3 / 12.6), "and is a floating point value")

# Calling the print method with any parameters will simply place
# an empty line (endline) in the console window
print()

# The print method comes with an "end" parameter that if not
# explicitly stated, defaults to "\n". This is a special
# symbol that when is placed in a string, causes the console
# to output an "endline" character. For example:
print("Hello\nWorld")

# We can override that default behavior (the endline) by using
# the keyword "end" and setting it equal to what we would rather
# do. An example is replacing the newline character with a space.
# Notice that even though we have two print statements below,
# The output to the console is a single line.
print("Who dat?")
print("Foobar!")

# We can output variables in "print". A variable is just
# a "named memory location" where we can store information of
# one kind or another. We will investigate variables in depth
# a bit later in the course
myVar1 = 12.34
myVar2 = "is a floating point value."

print("Here are two variables:", myVar1, myVar2)

# lastly, we can embed string literals with the newline character
# as shown below. Then place the string-literal into a variable
# and print that variable to the console
myVar3 = "\ntest\nusing\nembedded\nnewline\ncharacters"
print(myVar3)
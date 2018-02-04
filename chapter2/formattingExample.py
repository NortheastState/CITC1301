
# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program demonstrates how to use the print
#              function, ljust(), rjust(), and format()
#
# ===============================================================

# Lets see some ways to use the print and repr functions

def main():

    # using string functions rjust and ljust
    print("Foo".rjust(20))
    print("Bar".ljust(20) + "concatenated String Here")

    # the print function adds a newline character at the end of each string
    print("Geeks")
    print("rock!")

    # but you can alter the default ending newline character of the print
    print("Geeks", end=' ')
    print("rock!")

    # you can change the end character to what ever you like
    print("Geeks", end='$')
    print("rock!")
    print()


    # each of the curly brace sets define the location of the variable that is in format
    # starting at 0. So in this case, the number of each variable is 0, 1, 2
    print("{0} {1} {2}".format(1, 2.12, "Foobar"))

    # I could have used them in different order if I wanted to, and add other characters
    # inside the string literal
    print("Two:{2}, One:{1}, and Zero:{0}".format("Foo", "Bar", 42))

    print() # add a line

    # Aliging text use < > ^ *^ for left, right, centered, centered with fill character
    print("{0:<20}{0:>20}{0:^20}{0:-^20}".format(" Mr. Foobar "))

    print()

    # Showing floating point (f) numbers with a sign and precision
    print("{0:f} {1:f}".format(3.14159, -3.14159)) # only shows negative sign
    print("{0:+f} {1:+f}".format(3.14159, -3.14159)) # always show the sign
    print("{0:+.2f} {1:+.2f}".format(3333.14159, -3.14159)) # show sign with precision

    # show sign with a whole number, left or right aligned, field width 10 characters
    print("{0:<+10d} {1:>+10d}".format(3123, -3123))

    print("${0:,}".format(123456234234789))

    print()

    # using escape characters are easy
    print("Print\nA new line")
    print("\t\tTab over\ta few \t\t\ttimes")
    print("\"The best way to predict the future is to invent it\" by Alan Kay")
    print("The link is 'http:\\\\northeaststate.edu'") # i can embed single quotes in double

main()


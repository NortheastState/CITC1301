# ===============================================================
#
#        Name: David Blair
#        Date: 03/10/2018
#      Course: CITC 1301
#     Section: A70
# Description: Looking at the split function
#              and other string functions
#
# ===============================================================


def main():
    # example of a line of text that needs processed
    input1 = "1N002:10:Volvo:Bumper:2018:08:01:Fort Worth:TX"

    # here we create a string array with each cell being
    # the string between the colon delimiters
    varArray = input1.split(":")

    # let's test what we have by printing the entire array
    print()
    print(varArray)

    #  print each cell individually
    print()
    print(varArray[0])  # print first cell
    print(varArray[1])  # print second cell
    print(varArray[2])  # print third cell
    print(varArray[3])  # print forth cell
    print(varArray[4])  # print fifth cell
    print(varArray[5])  # print sixth cell
    print(varArray[6])  # print seventh cell
    print(varArray[7])  # print eighth cell
    print(varArray[8])  # print ninth cell

    # ---------------------------------

    var1 = "foobar, being captain of the universe, is always prepared to fight evil."

    print()
    print(var1.capitalize())    # cap first letter of first word
    print(var1.title())         # cap first letter of all words
    print(var1.lower())         # all letters are lowercase
    print(var1.upper())         # all letters are uppercase
    print(var1.center(100))     # center text in 100 field width
    print(var1.count('a'))      # count total number of 'a'
    print(var1.find('a'))       # find first 'a'
    print(var1.find('a', 5))    # find first 'a' start looking at index 5

    print()
    print("foobar".isalnum())   # True
    print("f00bar".isalnum())   # True
    print("12345".isalnum())    # True

    print("foobar".isalpha())   # True
    print("f00bar".isalpha())   # False
    print("12345".isalpha())    # False

    print("foobar".isdigit())   # False
    print("f00bar".isdigit())   # False
    print("12345".isdigit())    # True


main()

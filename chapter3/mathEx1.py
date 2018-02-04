# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program explores some of the python data
#              types.
#
# ===============================================================

# ---------------------------------------------------------------
#         Method: main
#     Parameters: None
#    Description: Class examples - fun with data types
# --------------------------------------------------------------


def main():


    # immutable data types:
    # int
    # float
    # complex*
    # str
    # bytes*
    # tuple*
    # frozenset*
    # bool

    # mutable data types:
    # array*
    # bytearray*
    # list*
    # set*
    # dict*

    # * - these data types will be explored later

    print(type("Foobar"))  # str
    print(type(3 * 10))  # int
    print(type(3.0 * 10))  # float
    print(type(3.0 * 10.0))  # float
    print(type(10 / 5))  # float
    print(type(10 // 5))  # int
    print(type(10 % 3))  # int
    print(type(True))  # bool
    print(type(False))  # bool
    print(type(10 < 3))  # bool
    print(type(5.3 == 5.3))  # bool

    # type conversion
    print(int(4.21))  # truncates to 4
    print(int(4.50))  # truncates to 4
    print(int(4.62))  # truncates to 4
    print(int("4"))   # converts to int
    print(float("4.50"))  # converts to float
    print(bool("True"))  # converts to bool
    print(float(4))  # 4.0

    # round to integer value
    print(round(4.4))  # 4
    print(round(4.5))  # 4
    print(round(4.51))  # 5
    print(round(4.6))  # 5

    # rounding using second parameter for number of decimal places
    pi = 3.141592653589793
    print(round(pi)) # with no second parameter
    print(round(pi, 2))  # with 2 decimal places
    print(round(pi, 5))  # with 5 decimal places
    print(abs(-1.234))  # 1.234

main()


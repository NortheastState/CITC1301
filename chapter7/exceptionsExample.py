# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program shows how to handle program exceptionss
#              for expected and unexpected input values.
#
# ===============================================================


def main():

    try:

        var1 = int(input("Enter an integer value: "))
        var2 = var1 / 0
        print(var2)

    except NameError as err:
        print("Value was not a number!", err)

    except ValueError as err:
        print("Value error, oops", err)

    except ZeroDivisionError as err:
        print("There was a divide by zero error!", err)

    except:
        print("Something else happened")


if __name__ == '__main__':
    main()



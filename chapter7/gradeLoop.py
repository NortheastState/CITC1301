
def main():
    for i in range(3):
        try:
            var1 = input("Enter a grade: ")
            intVar = int(var1)
            if intVar > 100:
                print("You entered a grade greater than 100, try again.")
            if intVar >= 90:
                print("A")
            elif intVar >= 80:
                print("B")
        except TypeError as err:
            print(err.message)
        except ValueError as err:
            print(err.message)
        except NameError as err:
            print(err.message)
        except:
            print(err.message)


def whileLoopTest():
    done = False
    total = 0.0
    counter = 0
    while not done:
        varABC = input("Enter test grade or Done: ")
        if varABC == "D" or varABC == "d":
            done = True
        varInt = int(varABC)
        if varInt > 100:
            print("Grade must be less than 100")
        elif varInt < 0:
            print("Grade must be zero or greater")
        else:
            counter = counter + 1
            total = total + varInt

    print()


def processString(var2):
    for i in range(len(var2)):
        print(var2[i])
        print(ord(var2[i]))




whileLoopTest()
#processString("Foobar")
#main()


# ===============================================================
#
#        Name: David Blair
#        Date: 03/10/2018
#      Course: CITC 1301
#     Section: A70
# Description: Examples of string the operation: substring
#
# ===============================================================


def main():
    var = "Computer programming rocks like 5 o'clock"
    print()
    print(var[0:7])  # Compute
    print(var[1:7])  # ompute
    print(var[2:7])  # mpute
    print(var[3:6])  # put

    print(var[:7])   # same as 0 start
    print(var[21:])   # print from 21 to the end
    print(var[:])    # print start to end

main()

# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program tests pass-by-reference using a
#               a list of integers, swapping two values in the
#               list, then printing out the list after calling
#               the swap function.
#
#               Note that "pass-by-reference" is also known as
#               "call-by-reference" like wise, "pass-by-value"
#               is also called "call-by-value"
#
# ===============================================================


def swap(values, ndx1, ndx2):
    temp = values[ndx1]
    values[ndx1] = values[ndx2]
    values[ndx2] = temp


def main():
    alist = []
    alist.append(5)
    alist.append(4)
    alist.append(7)
    alist.append(1)
    alist.append(3)
    return alist


mylist = main()

# print the order of integers before calling swap( )
print(mylist)
swap(mylist, 0, 1)

# print the order of integers after calling swap( )
# It is clear that the first two values were changed
print(mylist)

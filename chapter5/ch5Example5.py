# ===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: Working with Python lists
#
# ===============================================================


def main():
    lst1 = [1, 2, 3]
    lst2 = [1, 3, 6, 10, "foobar"]
    lst3 = lst1 + lst2      # here I can append on list to the other

    print(lst3)     # lists can be printed using the print function

    print()
    print(lst3.count(1))    # count the number of "1"s in the list
    lst3.append(22)         # append 22 to the list
    print(lst3)
    lst3.insert(2, "barfoo")  # insert text at location 2
    print(lst3)
    print(lst3.pop())       # remove the last item added to list
    print(lst3)
    lst3.remove("foobar")   # remove an item by "name"
    print(lst3)
    lst3.reverse()          # reverse the list
    print(lst3)
    lst3.remove("barfoo")
    lst3.sort()             # sort list number then letters
    print(lst3)


main()
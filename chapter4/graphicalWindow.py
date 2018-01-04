#===============================================================
#
#        Name: David Blair
#        Date: 01/01/2018
#      Course: CITC 1301
#     Section: A70
# Description: This program is a introduction to graphic user
#              interfaces using a wrapper class called
#              graphics.py which wraps up TKinter python class.
#
#              NOTE: There are many graphics engines for python
#              but tkinter (stands for "Tk interface" is one
#              of the most portable, meaning it will run on
#              Linux and Raspbian, Mac, and Windows all without
#              too much fuss. Plus, Tkinter is mature and well
#              tested, abd IDLE is written with Tkinter.
#
#===============================================================

#---------------------------------------------------------------
#         Method: main
#     Parameters: None
#    Description: Create a simple gui window and show it
#--------------------------------------------------------------

#--------------------------------------------------------------
# Linux:
# sudo apt-get install python3-tk

# Windows:
# Python 3.x should come with Tkinter - hooray!

# Mac:
# Download and Install Python 3.x
# Download and install tkinter 8.5 (64 bit) - from ActiveState
#--------------------------------------------------------------

# import the following module to use Tkinter
import tkinter

# now lets call the test method that comes with the install
tkinter._test()

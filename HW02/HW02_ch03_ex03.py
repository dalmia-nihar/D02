#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:

# print('+', '-')

# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:

# print('+', end=' ')
# print('-')

# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body


def line1(x):
	print ("+" + "-" * x + "+" + "-" * x + "+")

def line2(x):
	print ("|" + " " * x + "|" + " " * x + "|")

def do_twice(f,x):
	f(x)
	f(x)


def do_four(f,x):
	do_twice(f,x)
	do_twice(f,x)


def two_by_two():
	line1(2)
	do_twice(line2,2)
	line1(2)
	do_twice(line2,2)
	line1(2)
	



def four_by_four():
	line1(4)
	do_four(line2,4)
	line1(4)
	do_four(line2,4)
	line1(4)




# Write your functions above:
################################################################################
def main():
    """Call your functions within this function.
    When complete have two function calls in this function:
    two_by_two()
    four_by_four()
    """
    print("Hello World!")
    
    two_by_two()
    four_by_four()


if __name__ == "__main__":
    main()
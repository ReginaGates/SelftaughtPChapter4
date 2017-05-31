"""
Regina Gates
Programming Challenges
5/28/17

The Self-Taught Programmer
Cory Althoff
Chapter 4 Problem Set
"""

#Problem set

#1.
#Takes input, squares a number

def square_it():
    n = input("Enter a number to be squared: \n")
    int_n = int(n)

    result = int_n**2
    print("The square of your number is:")
    print(result)

square_it()

print("\n----------")

#2. Write a function that accepts a string as a parameter and prints it.

your_name = input("What is your name?\n")

def print_str(string):
    
    print(string)

print("Hello, ")

print_str(your_name)

print("\n----------")
    
#converts input number to a string.
def func_str():
    n = input("Enter a number: \n")
    str_n = str(n)
    print("Your string is: ")
    print(str_n)

func_str()

print("\n----------")

#3. Write a function that takes in 3 required params and 2 optional params.

prin = input("Please enter your principle: \n")
per = input("Please enter your compounding period: \n")
empty = input("Please enter the number 1, because Mr. Althoff said I needed another parameter: \n")

"""Errors: needed to convert to int data type.
"""
int_prin = int(prin)
int_per = int(per)
int_empty = int(empty)

def many_params(p, n, i, r=.043, t=6):

    """Need to put asterisk between numbers being multiplied."""
    a=p*i*(1 + (r/n))**(n*t)

    print("Your balance after 6 years will be: \n")
    print(a)

many_params(int_prin, int_per, int_empty)
print("\n----------")
#---------Lists

print("What items do you have?")
my_list = ["apples","oranges","strawberries"]
for item in my_list:
    print("I have " + item + ".")

#-----------

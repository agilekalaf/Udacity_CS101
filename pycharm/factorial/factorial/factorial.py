__author__ = 'gregbelanger'
# File factorial.py
# Simple example program to calculate the factorial of a number
# that is inputted by the user

#returns the factorial of the argument number
def factorial(number):
    if number <= 1: #base case
        return 1
    else:
        return number * factorial(number-1)
    
    #product = 1
    #for i in range(number):
    #    product = product * (i+1)
    #return product

user_input = input("Please enter in a non-negative integer to take the factorial of:")
factorial_of_user_input = factorial(user_input)
print factorial_of_user_input
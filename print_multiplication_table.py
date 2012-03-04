'''
Created on Mar 4, 2012

@author: gregbelanger
'''
#2 GOLD STARS

#Define a procedure,
#print_multiplication_table,
#that takes as input a positive whole
#number, and prints out a multiplication,
#table showing all the whole number
#multiplications up to and including the
#input number. The order in which the
#equations are printed must match exactly.

#print_multiplication_table(2)
#1 * 1 = 1
#1 * 2 = 2
#2 * 1 = 2
#2 * 2 = 4

def print_multiplication_table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            sum1 = i * j
            print("#" + str(i) + " * " + str(j) + " = " + str(sum1))
            j = j + 1
        i = i + 1
        
print_multiplication_table(3)
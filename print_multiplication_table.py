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
    '''
    >>> print_multiplication_table(0)

    >>> print_multiplication_table(1)
    1 * 1 = 1
    >>> print_multiplication_table(2)
    1 * 1 = 1
    1 * 2 = 2
    2 * 1 = 2
    2 * 2 = 4
    >>> print_multiplication_table(3)
    1 * 1 = 1
    1 * 2 = 2
    1 * 3 = 3
    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    3 * 1 = 3
    3 * 2 = 6
    3 * 3 = 9
    '''
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            sum1 = i * j
            print(str(i) + " * " + str(j) + " = " + str(sum1))
            j = j + 1
        i = i + 1
        
#print_multiplication_table(3)
if __name__ == '__main__':
    import doctest
    doctest.testmod(report=True,verbose=True,exclude_empty=True)


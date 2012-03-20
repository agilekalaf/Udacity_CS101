'''
Created on Mar 10, 2012

@author: gregbelanger
'''
#Define a procedure, greatest,
#that takes as input a list
#of positive numbers, and
#returns the greatest number
#in that list. If the input
#list is empty, the output
#should be 0.

#greatest([4,23,1]) => 23
#greatest([]) => 0

def greatest(p):
    if p == []:
        return 0
    greatest = 0
    for e in p:
        if e > greatest:
            greatest = e
    return greatest


list1 = []
print(greatest(list1))
    
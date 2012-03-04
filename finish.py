'''
Created on Mar 3, 2012

@author: gregbelanger
'''
n = 13
while n != 1:
    if n % 2 == 0: # n is even
        n = n/2
    else:
        n = 3*n + 1
print("Done")
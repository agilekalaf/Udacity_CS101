'''
Created on Mar 3, 2012

@author: gregbelanger
'''

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
        
def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a,b,c):
    if a == biggest(a,b,c):
        return bigger(b,c)
    elif b == biggest(a,b,c):
        return bigger(a,c)
    else:
        return bigger(a,b)


print(median(10,5,1))
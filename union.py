'''
Created on Mar 7, 2012

@author: gregbelanger
'''
#Define a procedure, union,
#that takes as inputs two lists.
#It should modify the first input
#list to be the set union of the two
#lists.

#a = [1,2,3]
#b = [2,4,6]
#union(a,b)
#a => [1,2,3,4,6]
#b => [2,4,6]
def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)
            #print(e)
    return a

a = [1,2,3]
b = [2,4,6]
#a = a + b
"""print(a)
print(b in a)
print(a + b)
print(a)
a.append(b[2])
"""
#print(a)
#print(union(a,b))
#print(b[2])
print(union(a,b))
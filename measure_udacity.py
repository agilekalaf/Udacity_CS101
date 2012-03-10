'''
Created on Mar 7, 2012

@author: gregbelanger
'''
def measure_udacity(p):
    count = 0
    for e in p:
        if e[0] == 'U':
            count  = count + 1
    return count

myList = ['Dave','Sebastian','Katy']
myList2 = ['Umika','Umberto']
print(measure_udacity(myList))
print(measure_udacity(myList2))
"""s = myList[1]
print(s.find("U",0))"""

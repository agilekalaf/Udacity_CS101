'''
Created on Mar 7, 2012

@author: gregbelanger
'''
def sum_list(p):
    sum1 = 0
    for e in p:
        sum1 = sum1 + e
    return sum1
        
        
mylist = [1,4,7]
print(sum_list(mylist))
'''
Created on Mar 10, 2012

@author: gregbelanger
'''
def product_list(p):
    sum1 = 1
    for e in p:
        sum1 = e * sum1
    return sum1
list1 = [1,2,3,4,5]
print(product_list(list1))
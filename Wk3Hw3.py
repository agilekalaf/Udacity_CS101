'''
Created on Mar 10, 2012

@author: gregbelanger
'''
def product_list(p):
    sum = 1
    for e in p:
        sum = e * sum
    return sum
list = [1,2,3,4,5]
print(product_list(list))
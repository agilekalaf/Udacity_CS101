'''
Created on Mar 10, 2012

@author: gregbelanger
'''
p = [1,0,1]

p[0] = p[0] + p[1]
p[1] = p[0] + p[2]
p[2] = p[0] + p[1]

print(p)
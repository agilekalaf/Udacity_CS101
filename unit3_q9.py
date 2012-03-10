'''
Created on Mar 5, 2012

@author: gregbelanger
'''


"""print(p[0])
p[0] = 'Y'
print(p)
p.append('!')
print(p)

spy = [0,0,7]
agent = spy
spy[2] = agent[2]+1
print(spy[2])"""

def print_all_elements(p):
    """i = 0
    while i <= (len(p)-1):
        print(p[i] + " " + str(i)) 
        i = i + 1"""
    for e in p:
        print(e)

p = [1,2,[3,4]]
#print(len(p))
print(print_all_elements(p))

'''
Created on Mar 5, 2012

@author: gregbelanger
'''
p = ['h','e','l','l','o']

print(p[0])
p[0] = 'Y'
print(p)
p.append('!')
print(p)

spy = [0,0,7]
agent = spy
spy[2] = agent[2]+1
print(spy[2])
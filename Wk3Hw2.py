'''
Created on Mar 10, 2012

@author: gregbelanger
'''
def proc1(p):
    p[0] = p[1]
    return p
    
def proc2(p):
    p = p + [1]
    return p
     
def proc3(p):
    q = p
    p.append(3)
    q.pop()
    return p

def proc4(p):
    q = []
    while p:
        q.append(p.pop())
    while q:
        p.append(q.pop())
    return p
        
p = [1,2,3]
#print(proc1(p))
#print(proc2(p))
print(proc3(p))
print(proc4(p))


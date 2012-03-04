'''
Created on Mar 3, 2012

@author: gregbelanger
'''
def proc(a,b):
    if test(a):
        return b
    return a

def proc1(x,y):
    if test(x):
        return y
    else:
        return x
    
def proc2(a,b):
    if not test(b):
        return a
    else:
        return b

def proc3(a,b):
    result = a
    if test(a):
        result = b
    return result

def proc4(a,b):
    if not test(a):
        b = 'udacity'
    else:
        return b
    return a

def test(num):
    return True

#print(test(4))

print(proc(3,4))
print(proc1(3,4))
print(proc3(3,4))
print(proc4(3,4))
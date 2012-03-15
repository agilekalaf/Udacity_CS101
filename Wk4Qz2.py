'''
Created on Mar 15, 2012

@author: gregbelanger
'''

index = [['udacity', ['http://udacity.com', 'http://npr.org']], ['computing', ['http://acm.org']]]

def lookup(index,keyword):
    for e in index:
        if e[0] == keyword:
            return e[1]
        else:
            return []
        
print(lookup(index,'udacity'))
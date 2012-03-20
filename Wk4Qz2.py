'''
Created on Mar 15, 2012

@author: gregbelanger
'''

index1 = [['udacity',['http://udacity.com','http://npr.org']],['computing',['http://acm.org']]]
index4 = [['computing',['http://acm.org']],['udacity',['http://udacity.com','http://npr.org']]]
index2 = ['udacity',['http://udacity.com','http://npr.org']]
index3 = ['computing', ['http://acm.org']]
index5 = [['udacity',['http://udacity.com']],['computing',['http://acm.org']],['udacity',['http://npr.org']]]

def lookup(index,keyword):
    for entry in index:
        #lists = e
        if entry[0] == keyword:
            return entry[1]
    return []
      
def lookup1(index, keyword):
    result = []
    for entry in index:
        if entry[0] == keyword:
            result.append(entry[1])
    return result

print(lookup(index1,'udacity'))
print(lookup1(index1,'udacity'))
print(lookup(index5,'udacity'))
print(lookup1(index5,'udacity'))

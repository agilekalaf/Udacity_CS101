'''
Created on Mar 13, 2012

@author: gregbelanger
'''
#index = []
index = []

print(index)

def add_to_index(index,keyword,url):
    if index == []:
        index.append([keyword,[url]])
        return
    else:
        for e in index:
                if e[0] == keyword:
                    e[1].append(url)
                    return
    index.append([keyword,[url]])
    
add_to_index(index,'udacity','http://udacity.com')
add_to_index(index,'computing','http://acm.org')
add_to_index(index,'udacity','http://npr.org')
print(index)
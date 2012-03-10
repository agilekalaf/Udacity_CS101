'''
Created on Mar 7, 2012

@author: gregbelanger
'''
def find_element(p,v):
    if v in p:
            return p.index(v)
    return -1
mylist = ['alpha','beta','gamma']
search = 'gamma'        
print(find_element(mylist,search))

print(search in mylist)
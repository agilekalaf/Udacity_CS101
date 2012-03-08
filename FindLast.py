'''
Created on Mar 3, 2012

@author: gregbelanger
'''
def find_last(target, search):
    start = target.find(search)
    if start == -1:
        return -1
    else:
        while True:
            if start != -1:
                pos = start
                start = target.find(search,start+1)
            else:
                return pos
            
        
    
        


print(find_last('aaaa','b'))
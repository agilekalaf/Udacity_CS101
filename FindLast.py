'''
Created on Mar 3, 2012

@author: gregbelanger
'''
def find_last(target, search):
    if target.find(search) == -1:
        print(-1)
    else:
        start = target.find(search)
        while start != -1:
            #print(start)
            start = target.find(search,start+1)
        print(target.find(search,start))
        return
        
        
    
        


find_last('asdasdasdasda','a')
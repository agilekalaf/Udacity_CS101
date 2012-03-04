'''
Created on Mar 4, 2012

@author: gregbelanger
'''
target = 'aaaaaaaaa'
search = 'a'
##
#position = target.find(search)
#print(position) #0
#nextPosition = target.find(search,position+1)
#print(nextPosition) #1
#nextPosition = target.find(search,nextPosition+1)
#print(nextPosition) #2
#nextPosition = target.find(search,nextPosition+1)
#print(nextPosition) #3
#nextPosition = target.find(search,nextPosition+1)
#print(nextPosition) #-1
#if nextPosition == -1:
#    print('end')
#nextPosition = target.find(search,nextPosition+1)
#print(nextPosition) #0
#nextPosition = target.find(search,nextPosition+1)
#print(nextPosition) # 1
if target.find(search) == -1:
    print(-1)
else:
    start = target.find(search)
    while start != -1:
        #print(start)
        start = target.find(search,start+1)
    print(target.find(search,start))
        
    
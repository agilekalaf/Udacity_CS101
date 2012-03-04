'''
Created on Mar 4, 2012

@author: gregbelanger
'''
def searchString(target,search):
    if target.find(search) == -1:
        return print("None")
    startString = target.find(searchS)
    while True:
        if nextString == -1:
            return #nextString
        print(target.find(search,nextString))
        nextString = (target.find(search)+1)
        print(target.find(search,nextString))
        nextString = (target.find(search,nextString)+1)
        print(target.find(search,nextString))
        nextString = (target.find(search,nextString)+1)
        print(target.find(search,nextString))
        nextString = (target.find(search,nextString)+1)
        print(target.find(search,nextString))
        

searchString('aaaa','a')
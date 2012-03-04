'''
Created on Mar 3, 2012

@author: gregbelanger
'''
def countdown(startNum):
    while startNum >= 1:
        print(startNum)
        startNum = startNum - 1
    print("Blastoff!")
    
    
countdown(1)
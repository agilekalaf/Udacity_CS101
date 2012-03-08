'''
Created on Mar 5, 2012

@author: gregbelanger
'''
spy = [0,0,7]

def replace_spy(l=[1,2,3]):
    l[2] = l[2] + 1
    return l#[num1,num2,num3]
    
replace_spy(spy)
print(spy)

list1 = [0,1]
list2 = [2,3]
list3 = list1 + list2

print(len(list3))

p = [1,2]
q = [3,4]
p.append(q)
print(len(p))
print(p)
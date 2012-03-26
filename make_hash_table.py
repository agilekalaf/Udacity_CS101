'''
Created on Mar 25, 2012

@author: gregbelanger
'''
def make_hashtable(nbuckets):
    hash_table = []
    for unused in range(0,nbuckets):
        hash_table.append([])
    return hash_table

print(make_hashtable(4))
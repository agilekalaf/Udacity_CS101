'''
Created on Mar 26, 2012

@author: gregbelanger
'''
#Define a procedure,

#hashtable_add(htable,key,value)

#that adds the key to the hashtable
#(in the correct bucket), with the
#correct value.

def hashtable_add(htable,key,value):
    hashtable_get_bucket(htable,key).append([key,value])
    return 0

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))]
    


def hash_string(keyword,buckets):
    out = 0
    for s in keyword:
        out = (out + ord(s)) % buckets
    return out

def make_hashtable(nbuckets):
    table = []
    for unused in range(0,nbuckets):
        table.append([])
    return table

word1 = 'alpha'
word2 = 'Projects'
value1 = 'Enterprise Room Reservation System'
ht = make_hashtable(4)
print(ht)
print(hash_string(word2,4))
hgb = hashtable_get_bucket(ht,word1)
print(hgb)
hashtable_add(ht,word2,value1)
print(ht)
hgb = hashtable_get_bucket(ht,word2)
print(hgb)
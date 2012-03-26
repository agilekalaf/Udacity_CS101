'''
Created on Mar 25, 2012

@author: gregbelanger
'''
def get_page(url):
    try:
        import urllib.request
        response = urllib.request.urlopen(url).read()
        return response
    except:
        return ""

def test_hash_function(func,keys,size):
    results = [0]*size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w,size)
            results[hv] += 1
            keys_used.append(w)
    return results

def hash_string(keyword,buckets):
    hv = 0
    for e in keyword:
        hv = (hv + (ord(e)))%buckets
    return hv

words = get_page('http://python.org/').split()
print(words)
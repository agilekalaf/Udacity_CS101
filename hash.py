'''
Created on Mar 21, 2012

@author: gregbelanger
'''
"""print(ord('a'))
print(chr(97))
print(15%12)

print(1%43)"""

def get_page(url):
    try:
        import urllib.request
        response = urllib.request.urlopen(url)
        html = response.read()
        return html
    except:
        return ""

def bad_hash_string(keyword,buckets):
    return ord(str(keyword[0]))%buckets


print(bad_hash_string("alpha",100))

def test_hash_function(func,keys,size):
    results = [0]*size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w,size)
            results[hv] += 1
            keys_used.append(w)
    return results

word1 = get_page("http://www.gutenberg.org/cache/epub/1661/pg1661.txt").split()
print(len(word1))
#print(words.split())
print(word1[2:3])
words = "alpha"
#counts = test_hash_function(bad_hash_string,word1,12)
#print(counts)



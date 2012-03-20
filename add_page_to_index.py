'''
Created on Mar 15, 2012

@author: gregbelanger
'''
#Define a procedure, add_page_to_index,
#that takes three inputs:

#   - index
#   - url (String)
#   - content (String)

#It should update the index to include
#all of the word occurences found in the
#page content by adding the url to the
#word's associated url list.


index = []

#add_page_to_index(index,'fake.text',"This is a test")
#print index => [['This', ['fake.text']], ['is', ['fake.text']], ['a', ['fake.text']], ['test', ['fake.text']]]

def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return
    index.append([keyword,[url]])

def add_page_to_index(index,url,content):
    for each_word in content.split():
        add_to_index(index,each_word,url)
    
    
    
contents = "This is a test"
url1 = 'fake.text'
#print(contents.split())
add_page_to_index(index,url1,contents)
add_page_to_index(index,'real.test',"This is NOT a real test")
print(index)

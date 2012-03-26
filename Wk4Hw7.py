'''
Created on Mar 19, 2012

@author: gregbelanger
'''
#2 Gold Stars

#One way search engines rank pages
#is to count the number of times a
#searcher clicks on a returned link.
#This indicates that the person doing
#the query thought this was a useful
#link for the query, so it should be
#higher in the rankings next time.

#(In Unit 6, we will look at a different
#way of ranking pages that does not depend
#on user clicks.)

#Modify the index such that for each url in a
#list for a keyword, there is also a number
#that counts the number of times a user
#clicks on that link for this keyword.

#The result of lookup(index,keyword) should
#now be a list of url entries, where each url
#entry is a list of a url and a number
#indicating the number of times that url
#was clicked for this query keyword.

#You should define a new procedure to simulate
#user clicks for a given link:

#record_user_click(index,word,url)

#that modifies the entry in the index for
#the input word by increasing the count associated
#with the url by 1.

#You also will have to modify add_to_index
#in order to correctly create the new data
#structure.

#Here is an example showing a sequence of interactions:


#index = crawl_web('http://www.udacity.com/cs101x/index.html')
#print lookup(index, 'good') => [['http://www.udacity.com/cs101x/index.html', 0], ['http://www.udacity.com/cs101x/crawling.html', 0]]
#record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
#print lookup(index, 'good') => [['http://www.udacity.com/cs101x/index.html', 0], ['http://www.udacity.com/cs101x/crawling.html', 1]]

def record_user_click(index,keyword,url):
    for each_entry in index:
        if each_entry[0] == keyword:
            print('found keyword')
            print(each_entry[1])
            for each_url in each_entry[1]:
                if each_url[0] == url:
                    print('found url')
                    print(each_url[0])
                    add_to_index(index,keyword,url,1)
                    return
    #return 0


def add_to_index(index, keyword, url, count):
    for entry in index:
        if entry[0] == keyword:
            #print('add-to-index keyword found' + str(entry[1]))
            for each_url in entry[1]:
                if not url in entry[1]:
                    entry[1].append([url,count])
                #entry[1].append(count)
                return
    # not found, add new keyword to index
    index.append([keyword,[[url,count]]])


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return  '<html> <body> This is a test page for learning to crawl! <p> It is a good idea to  <a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a> before you try to  <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. </p> </body> </html> '
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return  '<html> <body> I have not learned to crawl yet, but I am quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>. </body> </html>'
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '<html> <body> I cant get enough  <a href="http://www.udacity.com/cs101x/index.html">crawling</a>! </body> </html>'
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html> <body> The magic words are Squeamish Ossifrage! </body> </html>'
    except:
        return ""
    return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url,0)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None
index = crawl_web('http://www.udacity.com/cs101x/index.html')
print(lookup(index, 'good'))# => [['http://www.udacity.com/cs101x/index.html', 0], ['http://www.udacity.com/cs101x/crawling.html', 0]]
record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
print(lookup(index, 'good'))# => [['http://www.udacity.com/cs101x/index.html', 0], ['http://www.udacity.com/cs101x/crawling.html', 1]]
print(index)
index2 = [['http://www.udacity.com/cs101x/index.html', 0], ['http://www.udacity.com/cs101x/crawling.html', 0]]
print(index2[1])

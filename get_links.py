def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1:
        return None,0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"',start_quote+1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos:]
        else:
            #break
            print("no urls")
            break
        
def get_all_links(page):
    link_list = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            link_list.append(url)
            page = page[endpos:]
        else:
            #break
            print("no urls")
            break
    return link_list

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            #crawl
            tocrawl.append(get_all_links(page))
            crawled.append(page)
    return crawled


#url, end_pos = get_next_target('this is a <a href="http://udacity.com">link!</a>')
#url, end_pos = get_next_target('this" is a"')
#print(url)
#targetString = 'Hello World'
targetString = 'this is a <a href="http://udacity.com">link!</a>. if you like this site you will also like <a href="http://google.com">Google</a>.'
#print_all_links('this is a <a href="http://udacity.com">link!</a>. if you like this site you will also like <a href="http://google.com">Google</a>.')
print_all_links(targetString)
print(get_all_links(targetString))
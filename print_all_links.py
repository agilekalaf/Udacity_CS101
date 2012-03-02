'''
Created on Mar 1, 2012

@author: gregbelanger
'''
def print_all_links(page):
    while wewerwr:
        url,endpos = get_next_target(page)
        if url:
            print(url)
            page = page[endpos]
        else:
            
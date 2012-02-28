# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.

# page = contents of a web page
page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'
start_link = page.find('<a href="')
print start_link
url_begin = page.find('"',start_link) + 1
url_end = page.find('"',url_begin)
url = page[url_begin:url_end]
print url_begin
print url_end
print url
print "You are too cool!"
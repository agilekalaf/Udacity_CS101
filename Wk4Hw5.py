'''
Created on Mar 19, 2012

@author: gregbelanger
'''
#1 Gold Star

#The built-in <string>.split() procedure works
#okay, but fails to find all the words on a page
#because it only uses whitespace to split the
#string. To do better, we should also use punctuation
#marks to split the page into words.

#Define a procedure, split_string, that takes two
#inputs: the string to split and a string containing
#all of the characters considered separators. The
#procedure should output a list of strings that break
#the source string up by the characters in the 
#splitlist.

#out = split_string("This is a test-of the,string separation-code!", " ,!-")
#print out => ['This', 'is', 'a', 'test', 'of', 'the', 'string', 'separation', 'code']

#out = split_string("After  the flood   ...  all the colors came out.", " .")
#print out => ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

def split_string(source,splitlist):
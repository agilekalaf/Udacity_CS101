'''
Created on Mar 2, 2012

@author: gregbelanger
'''
def secret_formula(start_point):
    jelly_beans = start_point * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
#print ("We'd have %d beans, %d jars, and %d crab apples." % secret_formula(start_point))
beans, jars, crates = secret_formula(start_point)


def sort_words(words):
    """Sorts the words."""
    return sorted(words)

sentence = "All good \t things come to those who weight."

print(sort_words(sentence))

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

print(break_words(sentence))
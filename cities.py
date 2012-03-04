'''
Created on Mar 2, 2012

@author: gregbelanger
'''
cities = {'CA': 'San Francisco', 'MI': 'Detroit', 'FL': 'Jacksonville' }

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not found"

#ok pay attention
cities['_find'] = find_city

while True:
    print("State? ENTER to quit"),
    state = input("> ")
    
    if not state: break
    
    #study
    city_found = cities['_find'](cities, state)
    print(city_found)
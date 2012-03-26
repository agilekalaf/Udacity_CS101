'''
Created on Mar 21, 2012

@author: gregbelanger
'''
import time

def time_execution(code):
    start = time.clock()
    result = eval(code)
    run_time = time.clock() - start
    return result, run_time


def spin_loop(n):
    i = 0
    while i < n:
        i = i + 1
        
print(time_execution('spin_loop(10 ** 5)')[1])
print(time_execution('spin_loop(10 ** 6)')[1])
print(time_execution('spin_loop(10 ** 7)')[1])
print(time_execution('spin_loop(10 ** 8)')[1])
"""
print(time_execution('spin_loop(10 ** 5)')[1]) => 0.009672999999999987
print(time_execution('spin_loop(10 ** 6)')[1]) => 0.09676
print(time_execution('spin_loop(10 ** 7)')[1]) => 0.955915
print(time_execution('spin_loop(10 ** 8)')[1]) => 9.444236
linear increase in time as factors of ten increase
"""

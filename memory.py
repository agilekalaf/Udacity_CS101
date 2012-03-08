'''
Created on Mar 6, 2012

@author: gregbelanger
'''
print(2**10) #kilobyte
print(2**20) #megabyte
print(2**30) #gigabyte
print(2**40) #terabyte

# 1 byte = 8 bits
# 1 bit = light switch
#2GB RAM is 2**30*2*8 bits
dram = ((2**30)*2)*8 #no of bits in 2GB RAM
cost_of_dram = (2/dram)
print(dram)
print(cost_of_dram)

#cost per bit, latency, latency-distance
# light bulb = $.50 1 second, 300,000 km
# CPU =  $.001 <.4ns .12 m
# DRAM = n$.58  12ns 3.6m
# HDD = n$
# latency-distance = latency * speed of light (the amount of distance light travels in the latency time)
''' 
time = latency expressed in years ie: 12 ns is 3.80517503805175E-16
latency distance is time * lightyear * meters per year at speed of light
cost per bit is total bits divided by total cost



'''

def latency_distance(medium):
    speed_of_light = 300000 #km/s
    return medium * speed_of_light

light_bulb = 1
light_bulb_latency_distance_km = latency_distance(light_bulb)
print("The distance light travels in kilometers in one second " + str(light_bulb_latency_distance_km))

CPU = 4*10**-10
CPU_latency_distance = latency_distance(CPU)
print('The distance in meters light travels in .4 nanoseconds ' + str(CPU_latency_distance*1000) + ' meters')
print("The latency in nanoseconds of a CPU is " + str(CPU))

DRAM = 1.2*10**-8
#print(DRAM)
DRAM_latency_distance = latency_distance(DRAM)
print("The distance in meters that light travels in 12 nanoseconds " + str(DRAM_latency_distance*1000) + ' meters')
print("The latency in nanoseconds of a DRAM chip is " + str(DRAM))
cost_per_bit_DRAM = 10*(1000000000)/(2*(8*2**30))
print("COst per bit of DRAM " + str(cost_per_bit_DRAM) + " nanodollars")
cost_per_bit_HDD = (100*1000000000)/(8*2**40)
print('the cost per bit for a 1TB HDD is ' + str(cost_per_bit_HDD))
HDD = 7*10**-3
print('The distance in kilometers that light travels in 7ms is ' + str(latency_distance(HDD)))
print(1*10**-9)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:23:19 2017

@author: dm
"""


class Time:

    def __init__(self, seconds=0):
        self.s = seconds

#    def __str__(self):
 #       return "%s sec" % self.s

    def __repr__(self):
        return "Time(%s)" % self.s

time1 = Time(12)
time2 = Time(3456)
print (time1) 
print (time2)# Python wywołuje str()
print ([time1])
print ([time2])       # Python wywołuje repr()




### Wyniki

#runfile('/media/dm/SSD/PYTHON/3/3.7.py', wdir='/media/dm/SSD/PYTHON/3') domyslnie
#12 sec
#3456 sec
#[Time(12)]
#[Time(3456)]
#
#runfile('/media/dm/SSD/PYTHON/3/3.7.py', wdir='/media/dm/SSD/PYTHON/3') wykomentowany repr
#12 sec
#3456 sec
#[<__main__.Time object at 0x7fb7f1aea5f8>]
#[<__main__.Time object at 0x7fb7f1aea470>]
#
#runfile('/media/dm/SSD/PYTHON/3/3.7.py', wdir='/media/dm/SSD/PYTHON/3') #wykomentowane obie
#<__main__.Time object at 0x7fb8117ecda0>
#<__main__.Time object at 0x7fb7f1aea5f8>
#[<__main__.Time object at 0x7fb8117ecda0>]
#[<__main__.Time object at 0x7fb7f1aea5f8>]

#runfile('/media/dm/SSD/PYTHON/3/3.7.py', wdir='/media/dm/SSD/PYTHON/3') #wykomentowany str
#Time(12)
#Time(3456)
#[Time(12)]
#[Time(3456)]


#jak widac, przy autorskich obiektach musimy zdefiniowac podstawowe zachowania przy wyswietlaniu
#uwage zwraca wieksza uniwersalnosc repr, ktora przejmuje takze formatowanie str gdy nie jest zdefiniowane

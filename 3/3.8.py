#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:23:19 2017

@author: dm
"""


def sets():
    
    
    s = input("elements of sequence one: ")
    s2 = input("elements of sequence two: ")
    
    try:
        numbers = list(map(int, s.split()))    
        numbers2 = list(map(int, s2.split()))
    
        A = set(numbers)
        B = set(numbers2)
        
        C = A.intersection(B)
        D = A.union(B)
    
        print("intersection : ")
        print(C)
        print("sum : ")
        print(D)
        
        sets()
    except ValueError:
        command = str(s)
        command2 = str(s2)
        if command == "stop" or command2 == "stop":
            quit()
        print("Invalid number")
        sets()



sets()
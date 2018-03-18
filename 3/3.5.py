#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:23:19 2017

@author: dm
"""


def ruler():
    
    nb = input('Choose a ruler length: ')
    try:
        number = int(nb)
        T = "|"
        for i in range(number):
            T+=("....|")
        T+=("\n")
        for i in range(number + 1):
            if i <= 9 :
                T += str(i)
                T +=("    ")
            elif (i > 9 and i <= 99) :
                T += str(i)
                T +=("   ")
            elif (i > 99) :
                T += str(i)
                T +=("  ")
        print(T)
        ruler()
    except ValueError:
        command = str(nb)
        if command == "stop":
            quit()
        print("Invalid number")
        ruler()



ruler()
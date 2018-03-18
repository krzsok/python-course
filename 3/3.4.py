#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:23:19 2017

@author: dm
"""


def thirdpow():
    
    nb = input('Choose a number: ')
    try:
        number = int(nb)
        T = (number, number*number*number)
        print(T)
        thirdpow()
    except ValueError:
        command = str(nb)
        if command == "stop":
            quit()
        print("Invalid number")
        thirdpow()



thirdpow()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:23:19 2017

@author: dm
"""


def board():
    
    nb = input('Choose width ')
    nb2 = input('Choose heigth')
    try:
        width = int(nb)
        heigth = int(nb2)
        
        T = ""
        for i in range(heigth):
            for j in range(width):
                T+="+---+"
            T+="\n"
            for j in range(width):
                T+="|   |"
            
            T+="\n"
        for j in range(width):
                T+="+---+"
        
        print(T)
        board()
    except ValueError:
        command = str(nb)
        if command == "stop":
            quit()
        print("Invalid number")
        board()



board()
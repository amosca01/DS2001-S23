#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 12:24:40 2023

@author: abmosca
"""

 
def random_list_of_lists():
    '''
    name: random_list_of_lists
    parameters: none
    return type: list of lists 
    '''
    nums = [0, 3, 7]
    strs = ["m", "z", "x"]
    shapes = ["circle", "square", "rect"]
    
    return [nums, strs, shapes]
    
def main():
    
    lst_of_lsts = random_list_of_lists()
    print(lst_of_lsts)
    
    str_lst = lst_of_lsts[1]
    print(str_lst)
    
main()



    
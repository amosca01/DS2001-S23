#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicum 5 Sample solution 

Ab Mosca 02/17/23

"""

import math 

FILENAME = "cereal.csv"
NAME_IND = 0 
MFR_IND = 1 
TYPE_IND = 2 
CALORIES_IND = 3 
PROTEIN_IND = 4
FAT_IND = 5
SODIUM_IND = 6 
FIBER_IND = 7 
CARBO_IND = 8 
SUGARS_IND = 9 
POTASS_IND = 10 
VITAMINS_IND = 11 
SHELF_IND = 12 
WEIGHT_IND = 13 
CUPS_IND = 14
RATING_IND = 15 

def read_data(filename):
    '''
    name: read_data
    parameters: name of csv file
    return type: 2d list
    '''
    ds = []
    with open(filename, "r") as infile:
        headers = infile.readline()
        while True:
            row = infile.readline()
            if row == "":
                break
            ds.append(row.strip().split(','))
    return ds

def subset_data(ds, ind1, ind2, ind3):
    '''
    name: subset_data
    parameters: dataset, 3 indicies
    return type: 2d list 
    '''
    subset_ds = []
    
    for i in range(len(ds)):
        curr_row = ds[i]
        new_row = []
        for j in range(len(curr_row)):
            if (j == ind1):
                new_row.append(curr_row[j])
            if (j == ind2 or j == ind3):
                new_row.append(float(curr_row[j]))
        subset_ds.append(new_row)
    return subset_ds

def similarity(x1, x2, y1, y2):
    '''
    name: similarity
    parameters: two 2d points
    return type: int 
    '''
    dist = math.sqrt((x1 - y1)**2 + (x2 - y2)**2)
    return dist 

def find_closest(ab, ds):
    '''
    name: find closest
    parameters: data with one point, subset data 
    return type: string 
    '''
    #start with first row 
    closest = ds[0]
    ab = ab[0]
    best_dist = similarity(ab[1], ab[2], closest[1], closest[2])
    
    for row in ds:
        dist = similarity(ab[1], ab[2], row[1], row[2])
        if dist < best_dist:
            closest = row
            best_dist = dist 
    
    return closest[0]

def communicate_to_user(meas1, meas2, close):
    '''
    name: communicate_to_user
    parameters: strings of measures and closest
    return type: none 
    '''
    str = "The most similar to Ab's favorite in terms of " + meas1 + " and " + meas2 + " is " + close
    print(str)
    
def main():
    
    # read in data, pop headers 
    data = read_data(FILENAME)
    
    # declare ab's fave
    ab_fave = [["Cracklin' Oat Bran", "K", "C", 110, 3, 3, 140, 4, 10, 7, 160, 25, 3, 1, 0.5, 40.448772]]
    
    ab_sub = subset_data(ab_fave, NAME_IND, PROTEIN_IND, FAT_IND)
    subset = subset_data(data, NAME_IND, PROTEIN_IND, FAT_IND)
    ans = find_closest(ab_sub, subset)
    print("******", ans)
    
    # sodium and fiber
    ab_sub = subset_data(ab_fave, NAME_IND, SODIUM_IND, FIBER_IND)
    subset = subset_data(data, NAME_IND, SODIUM_IND, FIBER_IND)
    ans = find_closest(ab_sub, subset)
    communicate_to_user("sodium", "fiber", ans)
    
    # carbohydrates and rating
    ab_sub = subset_data(ab_fave, NAME_IND, CARBO_IND, RATING_IND)
    subset = subset_data(data, NAME_IND, CARBO_IND, RATING_IND)
    ans = find_closest(ab_sub, subset)
    communicate_to_user("carbohydrates", "rating", ans)
    
    # protein and vitamins
    ab_sub = subset_data(ab_fave, NAME_IND, PROTEIN_IND, VITAMINS_IND)
    subset = subset_data(data, NAME_IND, PROTEIN_IND, VITAMINS_IND)
    ans = find_closest(ab_sub, subset)
    communicate_to_user("protein", "vitamins", ans)
    
    # fiber and cups
    ab_sub = subset_data(ab_fave, NAME_IND, FIBER_IND, CUPS_IND)
    subset = subset_data(data, NAME_IND, FIBER_IND, CUPS_IND)
    ans = find_closest(ab_sub, subset)
    communicate_to_user("fiber", "cups", ans)

main()


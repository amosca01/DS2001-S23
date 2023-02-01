#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicum 3 sample solution

Ab Mosca

"""

import matplotlib.pyplot as plt

FILENAME = "bike_counts.txt"

def main():
    
    # empty lists 
    days = []
    dates = []
    times = []
    totals = []
    easts = []
    wests = []
    
    # read in data 
    with open(FILENAME, 'r') as infile:
        
        while True:
            day = infile.readline().strip()
            
            # check for end of file 
            if not day:
                break 
            # keep going if not at end 
            days.append(day)
            date = infile.readline().strip()
            dates.append(date)
            time = infile.readline().strip()
            times.append(time)
            total = int(infile.readline())
            totals.append(total)
            east = int(infile.readline())
            easts.append(east)
            west = int(infile.readline())
            wests.append(west)
            
    total_bikes = sum(totals)
    print("Total bikes:", total_bikes)
    
    total_east = sum(easts)
    total_west = sum(wests)
    if total_east >= total_west:
        print("More (or equal) bikes traveled east than west")
    else:
        print("More bikes traveled west than east")
        
    max_obs = max(totals)
    print("The max number of bikes observed was:", max_obs)
    
    min_obs = min(totals)
    print("The min number of bikes observed was:", min_obs)
    
    # calculate bikes per day of week 
    sun = 0
    mon = 0
    tue = 0
    wed = 0
    thu = 0
    fri = 0
    sat = 0
    
    loc_in_lst = 0
    
    for obs in days:
        if obs == "Sunday":
            sun += totals[loc_in_lst]
        elif obs == "Monday":
            mon += totals[loc_in_lst]
        elif obs == "Tuesday":
            tue += totals[loc_in_lst]
        elif obs == "Wednesday":
            wed += totals[loc_in_lst]
        elif obs == "Thursday":
            thu += totals[loc_in_lst]
        elif obs == "Friday":
            fri += totals[loc_in_lst]
        else:
            sat += totals[loc_in_lst]
        loc_in_lst += 1
        
    week_bikes = [sun, mon, tue, wed, thu, fri, sat]
    
    # bar chart 
    week_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    plt.bar(x = week_names, height = week_bikes)
    plt.xlabel("Day")
    plt.ylabel("Number of Bikes")
    
main() 

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicum 4 sample solution

Ab Mosca

"""

import matplotlib.pyplot as plt

#FILENAME = "bike_counts.txt"
FILENAME = "bike_counts_v2.txt"

def read_data(f_name):
    '''
    Parameters: filename
    Return Type: list of lists 
    Function: reads data from file   
    '''
    
    # empty lists 
    days = []
    dates = []
    times = []
    totals = []
    easts = []
    wests = []
    
    # read in data 
    with open(f_name, 'r') as infile:
        
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
            
    # set up list of lists to return 
    data = [days, dates, times, totals, easts, wests]
    return data

def total_bikes(counts):
    '''
    Parameters: list
    Return Type: string 
    Function: calculates total and returns in a string  
    '''
    
    total = sum(counts)
    return_str = "The total number of bikes was " + str(total)
    return return_str

def west_vs_east(west_counts, east_counts):
    '''
    Parameters: list, list
    Return Type: string 
    Function: calculates total or each list, compares, and returns result in a string  
    '''
    total_west = sum(west_counts)
    total_east = sum(east_counts)
    if total_east >= total_west:
        return "More bikes traveled eastbound"
    else:
        return "More bikes traveled westbound"
       
def max_15mins(counts):
    '''
    Parameters: list
    Return Type: string 
    Function: calculates max and returns in a string  
    ''' 
    max_obs = max(counts)
    return_str = "The max number of bikes in one 15 minute segment was " + str(max_obs)
    return return_str   

def daily_totals(day_names, counts): 
    '''
    Parameters: list, list
    Return Type: list 
    Function: calculates total per day of week and returns all totals in a list   
    '''
    sun = 0
    mon = 0
    tue = 0
    wed = 0
    thu = 0
    fri = 0
    sat = 0
    
    for i in range(len(day_names)):
        
        day = day_names[i]
        total = counts[i]
        
        if day == "Sunday":
            sun += total
        elif day == "Monday":
            mon += total
        elif day == "Tuesday":
            tue += total
        elif day == "Wednesday":
            wed += total
        elif day == "Thursday":
            thu += total
        elif day == "Friday":
            fri += total
        else:
            sat += total     
    week_bikes = [sun, mon, tue, wed, thu, fri, sat]
    return week_bikes

def daily_bar_plot(daily_counts):
    '''
    Parameters: list
    Return Type: nothing
    Function: plots bar chart of daily counts   
    '''
    week_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    plt.bar(x = week_names, height = daily_counts)
    plt.xlabel("Day")
    plt.ylabel("Number of Bikes")


def main():
    
    # read in data
    dataset = read_data(FILENAME)
    
    # pull out lists
    days_lst = dataset[0]
    dates_lst = dataset[1]
    times_lst = dataset[2]
    totals_lst = dataset[3]
    easts_lst = dataset[4]
    wests_lst = dataset[5]
    
    tot_bikes = total_bikes(totals_lst)
    print(tot_bikes)
    
    west_east = west_vs_east(wests_lst, easts_lst)
    print(west_east)
    
    max_obs = max_15mins(totals_lst)
    print(max_obs)
    
    week_totals = daily_totals(days_lst, totals_lst)
    daily_bar_plot(week_totals)
        
main() 

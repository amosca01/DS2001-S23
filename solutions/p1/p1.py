#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DS2001 S23
Ab Mosca 

p1 sample solution 
"""

FILENAME = "marathon.txt"
MILES_PER_MARATHON = 26.2
KM_PER_MILE = 1.61
MIN_PER_HOUR = 60 

def main():
    
    # input data 
    with open(FILENAME, 'r') as infile:
        name = infile.readline().strip()
        num_marathons = int(infile.readline())
        pr_total_mins = int(infile.readline())
        
    # computations
    pr_pace_mile = pr_total_mins / MILES_PER_MARATHON
    marathon_kms = MILES_PER_MARATHON * KM_PER_MILE
    pr_pace_km = pr_total_mins / marathon_kms
    pr_hours = pr_total_mins // MIN_PER_HOUR
    pr_mins = pr_total_mins % MIN_PER_HOUR 
    
    # communication 
    print(name, "has a marathon PR of", pr_total_mins, "minutes!")
    print("That's ", pr_hours, "hours and ", round(pr_mins), "mins of running")
    print("at a pace per mile of ", round(pr_pace_mile, 2), "minutes")
    print("or a pace per km of ", round(pr_pace_km, 2), "minutes!")
main()


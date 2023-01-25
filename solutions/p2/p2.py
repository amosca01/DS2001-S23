#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DS2001 S23 

Practicum 2 

Ab Mosca
"""

import matplotlib.pyplot as plt 

FILENAME = "punxsutawney.txt"
AVG_FEB = 52

def main():
    
    # read in data 
    with open(FILENAME, 'r') as infile:
        
        year1 = int(infile.readline())
        shadow1 = infile.readline().strip()
        temp1 = float(infile.readline())
        
        year2 = int(infile.readline())
        shadow2 = infile.readline().strip()
        temp2 = float(infile.readline())
        
        year3 = int(infile.readline())
        shadow3 = infile.readline().strip()
        temp3 = float(infile.readline())
        
        year4 = int(infile.readline())
        shadow4 = infile.readline().strip()
        temp4 = float(infile.readline())
        
        year5 = int(infile.readline())
        shadow5 = infile.readline().strip()
        temp5 = float(infile.readline())
        
    # computations 
    
    # spring temp?
    if (temp1 >= AVG_FEB):
        spring_temp1 = True
    else:
        spring_temp1 = False 
    
    if (temp2 >= AVG_FEB):
        spring_temp2 = True
    else:
        spring_temp2 = False 
        
    if (temp3 >= AVG_FEB):
        spring_temp3 = True
    else:
        spring_temp3 = False 
        
    if (temp4 >= AVG_FEB):
        spring_temp4 = True
    else:
        spring_temp4 = False 
        
    if (temp5 >= AVG_FEB):
        spring_temp5 = True
    else:
        spring_temp5 = False 
    
    
    # accurate?
    if shadow1 == "No Shadow":
        if spring_temp1:
            acc1 = True 
        else:
            acc1 = False
    elif shadow1 == "Full Shadow":
        if spring_temp1:
            acc1 = False
        else:
            acc1 = True 
            
    if shadow2 == "No Shadow":
        if spring_temp2:
            acc2 = True 
        else:
            acc2 = False
    elif shadow2 == "Full Shadow":
        if spring_temp2:
            acc2 = False
        else:
            acc2 = True 
            
    if shadow3 == "No Shadow":
        if spring_temp3:
            acc3 = True 
        else:
            acc3 = False
    elif shadow3 == "Full Shadow":
        if spring_temp3:
            acc3 = False
        else:
            acc3 = True 
            
    if shadow4 == "No Shadow":
        if spring_temp4:
            acc4 = True 
        else:
            acc4 = False
    elif shadow4 == "Full Shadow":
        if spring_temp4:
            acc4 = False
        else:
            acc4 = True 
            
    if shadow5 == "No Shadow":
        if spring_temp5:
            acc5 = True 
        else:
            acc5 = False
    elif shadow5 == "Full Shadow":
        if spring_temp5:
            acc5 = False
        else:
            acc5 = True 
    
    #communication 
    if acc1:
        plt.plot(year1, temp1, "o", color="green", label="correct")
    else:
        plt.plot(year1, temp1, "o", color="blue")
        
    if acc2:
        plt.plot(year2, temp2, "o", color="green")
    else:
        plt.plot(year2, temp2, "o", color="blue", label="incorrect")
        
    if acc3:
        plt.plot(year3, temp3, "o", color="green")
    else:
        plt.plot(year3, temp3, "o", color="blue")
        
    if acc4:
        plt.plot(year4, temp4, "o", color="green")
    else:
        plt.plot(year4, temp4, "o", color="blue")
        
    if acc5:
        plt.plot(year5, temp5, "o", color="green")
    else:
        plt.plot(year5, temp5, "o", color="blue")
        
    plt.title("Punxsutawney Phil's Predictions")
    plt.xlabel("Year")
    plt.ylabel("Average Temp (F)")
    plt.legend()
    #just tell students this, don't expect them to know it 
    plt.locator_params(axis="x", nbins=5)
    
main()
        

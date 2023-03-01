#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Practicum 6 Sample Solution

Ab Mosca
"""

BEYONCE = "beyonce.txt"
TAYLOR = "taylor.txt"

def read_data(filename):
    '''
    name: read_data
    parameter: filename, string 
    return: list of strings 
    does: reads in specifiect file, 
          returns list of strings in file
    '''
    
    with open(filename, 'r') as infile:
        words = []
        while True:
            line = infile.readline().strip().split(" ")
            
            if line == ['']:
                break
            
            # add each word in line to words
            for i in range(len(line)):
                words.append(line[i])
        return words
    
def wordcounts(word_lst):
    '''
    name: wordcounts
    parameter: list of words
    return: word count dictionary
    does: returns dictionart with key = word and value = frequency
    '''
    
    counts = dict()
    for word in word_lst:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts 
    
def predict(artist1, artist1_dict, artist2, artist2_dict, lyric):
    '''
    name: predict 
    parameters: artist 1's name, artist 1's word count dict,
                artist 2's name, artist 2's word count dict,
                lyric
    returns: string 
    does: returns which artist most likely wrote lyric
    '''
    
    # split lyric into words
    words = lyric.split(" ")
    
    # count
    artist1_count = 0
    artist2_count = 0
    
    for word in words:
        if word in artist1_dict:
            artist1_count += artist1_dict[word]
        if word in artist2_dict:
            artist2_count += artist2_dict[word]
            
    # compare 
    if artist1_count > artist2_count:
        return artist1
    elif artist1_count < artist2_count:
        return artist2
    else:
        return "Tie!"
            
def main():
    
    # read in data 
    bey_words = read_data(BEYONCE)
    tay_words = read_data(TAYLOR)
    
    # make word count dictionaries 
    bey_dict = wordcounts(bey_words)
    tay_dict = wordcounts(tay_words)
    
    # get input and communicate 
    lyr = input("Enter a lyric!\n")
    ans = predict("Beyonce", bey_dict, "Taylor", tay_dict, lyr)
    print("That lyric was probably written by:", ans)
    
main() 


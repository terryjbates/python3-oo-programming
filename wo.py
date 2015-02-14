#!/usr/bin/env python3

import os
import sys

def words_occur():
    # Prompt for file name.
    file_name = input("Enter name of file: ")
    # Open the file.
    f = open(file_name, 'r')
    # Use context manager to open file.
    with open(file_name,'r') as f:
        # Obtain list of words in one shot. 
        #Read the file then split on whitespace 
        word_list = f.read().split()
        
    # Create dict to store unique words
    occurs_dict = {}
    for word in word_list:
        # Add the word to our dictionary and increment the count. Use a 
        # default of 0 if this is first time words is encountered.
        occurs_dict[word] = occurs_dict.get(word, 0) + 1
    # Print out results.
    print("Files {0} has {1} unique words".format(file_name, len(occurs_dict)))
    print(occurs_dict)
    
def main():
    words_occur()
    
    
if __name__ == "__main__":
    main()

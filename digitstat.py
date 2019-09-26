#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, join

'''
I hope you don't program regularly, because this program is a mess. It is not optimized and was written during
a boring lecture. Thanks for reading anyways :) 
'''

data_sets = [f for f in listdir("Data Sets") if isfile(join("Data Sets", f))] #Get CSV files in subdirectory "data sets"

print("Analyzing %s data sets..." % len(data_sets))  #Write the amount of fetched data sets

data_entry_count = 0   #Value to store number of data entries


out = "" #The output to be written when all is analyzed
data_index = 0  #An index used when iterating though the files. Used to determine the progress

for csv in data_sets: #Iterate through all data set files
    file = open("Data Sets/" + csv, "r", encoding='mac_roman') #Open the current csv file
    data_entries = file.readlines() #Get an array with the lines (data_entries)
    data_entry_count += len(data_entries) #Add this to the data_entry_count to keep track of data_entries to be analyzed
    print("Data set %s/%s (%s)" % (data_index +1,len(data_sets), csv))  #Print which data set is curently being analyzed
    entry_index = 0 #Index when iterating through the data entries to keep track of the progress
    digit_count = 10 * [0] #Empty array, holding the statistics of the occurrence of each digit.

    for data_entry in data_entries: #Iterate through all data entries

        if round(entry_index/data_entry_count*100,3) % 10 == 0: #If the percentage of entries completed divided by 10 has 0 leftovers
            print("%s percent done" % str(round(entry_index/data_entry_count*100,0))) #Print progress
            print(digit_count)  #Print current statistics


        significant_digit = True #Set that the next digit is significant
        for char in data_entry: #Iterate through the data entries
            if significant_digit: #If the digit is significant
                #Following is a very stupid and slow way to determine if the digit is a number
                if char is "0":
                    digit_count[0] += 1
                elif char is "1":
                    digit_count[1] += 1
                elif char is "2":
                    digit_count[2] += 1
                elif char is "3":
                    digit_count[3] += 1
                elif char is "4":
                    digit_count[4] += 1
                elif char is "5":
                    digit_count[5] += 1
                elif char is "6":
                    digit_count[6] += 1
                elif char is "7":
                    digit_count[7] += 1
                elif char is "8":
                    digit_count[8] += 1
                elif char is "9":
                    digit_count[9] += 1

                significant_digit = False #Next is to set that the next digit isn't significant


            else: #Set that the next digit is significant if the current digit isn't a number
                try:
                    val = int(char)
                except ValueError:
                    if(char != "."):
                        significant_digit = True
        entry_index += 1
    data_index += 1
    significant_all = sum(digit_count) #Get amount of significant digits
    digit_percent = 10 * [0]
    for i in range(len(digit_count)): #Calculate the percentage (and remember to handle division by zero :p
        try:
            digit_percent[i] = round((digit_count[i]/significant_all)*100, 2)
        except:
            digit_percent[i] = 0

    out += "File: %s\n" % csv #Write data to output string
    out += "Digit counts: %s\n" % digit_count
    out += "Digit percent: %s \n" % digit_percent

#Print output :)
print("Analyzed %s data entries" % data_entry_count)
print(out)


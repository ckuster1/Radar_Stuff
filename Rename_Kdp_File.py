#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:07:35 2020

@author: charles.kuster
(c) University of Oklahoma
"""

#This script changes file names (appends _KDP) for KDP core study. **Really should only run this once. Could subset dates too as last resort

#Import needed libraries
import os

#Root path where all subdirectories and Kdp files are located
rootdir = "/localdata/ckuster/CIMMS_Research/Downburst_Precursors/Combined_Cases/20170721/Grab_Data"

#Loop through all of the subdirectories in root 
for subdirs, dirs, files in os.walk(rootdir):
    #print('dirs:', dirs)
    #print('subdirs:', subdirs)
    #Only look at the subdirectories that end with /KDP
    if subdirs.endswith("/KDP"):
        #Print out the directories and subdirectories for easy tracking as script is running.
        print('dirs:', dirs)
        print('subdirs:', subdirs)
        #Loop through all of the .csv files and rename them by adding _KDP after the elevation angle
        for file in files:
            print('old file name:', file)
            if file.endswith(".csv"):
                src = subdirs + "/" + file
                print('src:', src)
                #Remove .csv from end
                time_angle = file.strip('.csv')
                print('new filename:', time_angle)
                #Add _KDP and .csv to end of time angle (which is original file name without the .csv)
                dst = subdirs + "/" + time_angle + "_KDP" + ".csv"
                print('dst:', dst)
                #Rename the files from the old file name (src) to the new one (dst)
                os.rename(src, dst)



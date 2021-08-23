#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 13:07:35 2020

@author: charles.kuster
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
        print('dirs:', dirs)
        print('subdirs:', subdirs)
        #Loop through all of the .csv files and rename them by adding _KDP after the elevation angle
        for file in files:
            print('old file name:', file)
            if file.endswith(".csv"):
                src = subdirs + "/" + file
                print('src:', src)
                time_angle = file.strip('.csv')
                print('new filename:', time_angle)
                dst = subdirs + "/" + time_angle + "_KDP" + ".csv"
                print('dst:', dst)
                os.rename(src, dst)



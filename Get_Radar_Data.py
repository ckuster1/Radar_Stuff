# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:00:09 2020

@author: Charles
"""

import os
import matplotlib.pyplot as plt
import tempfile
import pytz
from datetime import datetime
#import pyart
import nexradaws

conn = nexradaws.NexradAwsInterface()

print('Current working directory is:' , os.getcwd(), '\n')

#download_location = os.chdir(r"C:\Users\User\Documents\CIMMS_Research\Radar_Data\20160727_OK_Downbursts")
download_location = (r"C:\Users\User\Documents\CIMMS_Research\Radar_Data\OK-First\20190704")
#print('Current working directory is:', os.getcwd(), '\n')
print(type(download_location))
#print('Download loation:', download_location)

#Set info for using UTC time
utc = pytz.utc
utc.zone

#Set radar id for data download (change as needed)
radar_id = 'KGJX'
#print('Radar is:', radar_id, '\n')

#Set start and end time for downloading data
start_time = datetime(2021,7,22,19,00, tzinfo=utc)
end_time = datetime(2021,7,22,20,30, tzinfo=utc)

#Check to see what scans are available for download
scans = conn.get_avail_scans_in_range(start_time, end_time, radar_id)
#Print the total number of available scans
print("There are {} scans available between {} and {}\n".format(len(scans), start_time, end_time))
#Print an example of the files available
print('Scans:', scans[0:4])

#Download all of the avialable data
file_download = conn.download(scans, download_location)
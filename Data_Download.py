# Tacoma Land Use Permits from CivicData (json)
# Data update process for Tacoma Public Notice Land Use Permits
# https://wspdsmap.cityoftacoma.org/website/PDS/LandUse/
# Download the file from `url` and save it locally under `file_name`
# Need to include 'limit' variable or else only get the first 100 records 
# CivicData table view of data: http://www.civicdata.com/dataset/landusenotices_v4_17660/resource/c05a77df-f2da-4cd4-9181-05eb13674782
# Updated: 2019-7-24
# Author: mmurnane

import urllib
import logging
import os

url = 'http://www.civicdata.com/api/3/action/datastore_search?resource_id=c05a77df-f2da-4cd4-9181-05eb13674782&limit=10000'
#file_name = "\\\\wsitd01dev\\c$\\GADS\\website\\PDS\\LandUse\\data\\LandUseNotices.json" #DEV 
file_name = "\\\\wsitd01\\c$\\GADS\\website\\PDS\\LandUse\\data\\LandUseNotices.json"  #PRODUCTION

try:
  # Download file 
  urllib.urlretrieve (url, file_name)
except:
  logging.exception('\n Unexpected error with website, could not download file successfully: \n')
else:
  if os.path.getsize(file_name)> 1000:
    print "File download successful!"
  else:
    print "CHECK JSON FILE FOR ERROR MESSAGE! File download successful, but file size appears too small!"

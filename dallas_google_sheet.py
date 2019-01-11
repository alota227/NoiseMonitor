import os
import sys
#print sys.path
import time
import datetime
#import datetime as dt
#from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
#import oauth2client
import json
json.JSONEncoder.default = lambda self,obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)

# use creds to create a client to interact with the Google Drive API
#scope = ['https://spreadsheets.google.com/feeds']
#scope = ['https://spreadsheets.google.com/feeds',
#         'https://www.googleapis.com/auth/drive']
scope = ['https://spreadsheets.google.com/feeds' + ' ' +'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

#json filename for credentials
#JSON_FILENAME = 'Tempo-84a920791d0a.json'
#JSON_FILENAME = 'client_secret.json'

# Google sheet to save to
GSHEET_NAME = 'temp_logging_demo'

#load credentials from json and open the spreadsheet for writing
#json_key = json.load(open(JSON_FILENAME))
#creds = oauth2client.client.SignedJwtAssertionCredentials(json_key['client_email'], 
#		json_key['private_key'],
#		['https://spreadsheets.google.com/feeds'])
client_inst = gspread.authorize(creds)
gsheet = client_inst.open(GSHEET_NAME).sheet1

while 1:
	tempfile = open("/sys/bus/w1/devices/28-5698031d64ff/w1_slave")
	thetext = tempfile.read()
	tempfile.close()
	tempdata = thetext.split("\n")[1].split(" ")[9]
	temperature = float(tempdata[2:])
	temperature = temperature / 1000

#curr_time = datetime.datetime.now()
	curr_time = json.dumps(datetime.datetime.now())
#curr_time = dt(int(year), int(month), 1)
#curr_time = datetime.datetime(2018, 12, 1)
	print ("Writing new row")

#write a new row to the spreadsheet with the current time and temperature
	gsheet.append_row((curr_time, temperature))
	time.sleep(5)

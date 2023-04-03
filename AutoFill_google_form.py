import requests
import datetime
import time
import random


#URL Of google form but replace viewform by formResponse

url = "https://docs.google.com/forms/d/e/ID/formResponse"

def get_gmt_time(delta = 1):
    ''' get local time Bruxelles (+1)
        help run correctly on any server'''
    date = datetime.datetime.now()
    tz = datetime.timezone(datetime.timedelta(hours = delta))
    return date.astimezone(tz)

start_day = datetime.datetime(2023, 4, 1,  tzinfo = datetime.timezone(datetime.timedelta(hours = 1)))
today = get_gmt_time()



def fill_form():

    date, hour = str(get_gmt_time()).split(' ')
    date = date.split('-')
    hour = hour.split(':')
    
    if (int(hour[0]) < 10):
        hour[0] = hour[0][1:]

    value = {
        # Consent
        "entry.Num" : "Yes, I Consent",
        "entry.Num": 'option1',
        "entry.Num": 'option2',
       
    }
    print(value, flush = True)
    return value


def submit(url, data):
    try:
        requests.post(url, data = data)
        print("Submitted successfully")
        return True
    except:
        print("Error!")
        return False

'''----------------------------------------------------------------------'''
print("Running script...", flush = True)

for i in range():
    submit(url, fill_form())
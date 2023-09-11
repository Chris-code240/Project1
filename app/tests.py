from django.test import TestCase
import pytz
import datetime

utc_timezone = pytz.timezone('UTC')
current_utc_time = datetime.datetime.now(utc_timezone)
current_utc_time = datetime.datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        

# current_utc_time = (datetime.datetime.strptime(current_utc_time, "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=1)).isoformat() + 'Z'

print(current_utc_time)


# Create your tests here.

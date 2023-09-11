from django.test import TestCase

import datetime

current_utc_time = datetime.datetime.utcnow().replace(
            second=0, microsecond=0).isoformat() + 'Z'

current_utc_time = (datetime.datetime.strptime(current_utc_time, "%Y-%m-%dT%H:%M:%SZ") + datetime.timedelta(hours=1)).isoformat() + 'Z'

print(current_utc_time)


# Create your tests here.

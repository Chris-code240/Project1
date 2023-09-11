from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
import datetime

@api_view(['GET'])
def home(request):
    
    current_datetime = datetime.datetime.now()
    day_of_week = current_datetime.strftime('%A')
    return HttpResponse(json.dumps({ "slack_name": request.GET.get('slack_name','None'),
            "current_day": day_of_week,
            "utc_time": str(datetime.datetime.utcnow()),
            "track": request.GET.get('track','None'),
            "github_file_url": "https://github.com/Chris-code240/Project1/blob/master/app/views.py",
            "github_repo_url": "https://github.com/Chris-code240/Project1",
            "status_code": 200
        }))

#http://example.com/api?slack_name=example_name&track=backend
# Create your views here.

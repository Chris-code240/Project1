from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pytz
from django.http import JsonResponse
import datetime

@api_view(['GET'])
def home(request):
        slack_name = request.GET.get('slack_name', 'example_name')
        track = request.GET.get('track', 'backend')

        current_day = datetime.datetime.now().strftime('%A')
        
        current_utc_time = datetime.datetime.now(pytz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

        github_repo_url = 'https://github.com/Chris-code240/Project1'
        github_file_url = f'https://github.com/Chris-code240/Project1/blob/dev/app/views.py'


        response_data = {
            'slack_name': slack_name,
            'current_day': current_day,
            'utc_time': current_utc_time,
            'track': track,
            'github_file_url': github_file_url,
            'github_repo_url': github_repo_url,
            'status_code': 200,
        }
        return JsonResponse(response_data)

#http://example.com/api?slack_name=example_name&track=backend
# Create your views here.

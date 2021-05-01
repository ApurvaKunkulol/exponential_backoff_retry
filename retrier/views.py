import time
from datetime import datetime
import requests
import json
from pprint import pprint

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .constants import (successful_poll_url,
                        unsuccessful_poll_url,
                        max_attempts,
                        random_const,
                        querystring,
                        )


@api_view(['GET'])
def send_request(request):
    try:
        response = poll_third_party(weather_url=successful_poll_url)
        print("Weather API response: {}\n\n".format(response.status_code))
        pprint(response.__dict__)
        if response.status_code == status.HTTP_200_OK:
            content = json.loads(response.content)
            return Response(content, status=status.HTTP_200_OK)
        else:
            weather_status, response = exp_retry()
            if weather_status == status.HTTP_200_OK:
                content = json.dumps(response)
                return Response(content, status=status.HTTP_200_OK)
            else:
                content = {"message": "Maximum attempts reached. Service unavailable."}
                return Response(content)
    except Exception as ex:
        raise ex


@api_view(['GET'])
def send_request_fail(request):
    try:
        response = poll_third_party(weather_url=unsuccessful_poll_url)
        print("Weather API response: {}\n\n".format(response.status_code))
        pprint(response.__dict__)
        if response.status_code == status.HTTP_200_OK:
            content = json.loads(response.content)
            return Response(content, status=status.HTTP_200_OK)
        else:
            weather_status, response = exp_retry(weather_url=unsuccessful_poll_url)
            if weather_status == status.HTTP_200_OK:
                content = json.dumps(response)
                return Response(content, status=status.HTTP_404_NOT_FOUND)
            else:
                content = {"message": "Maximum attempts reached. Service unavailable."}
                return Response(content, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        raise ex

def poll_third_party(weather_url=successful_poll_url):
    try:
        response = requests.get(url=weather_url,
                                params=querystring)
        return response
    except Exception as ex:
        raise ex


def exp_retry(weather_url=successful_poll_url):
    current_attempt = 1
    weather_status = False
    response = ''
    while current_attempt <= max_attempts:
        print("\n\nAttempt number {}\nTime: {}".format(current_attempt, datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        delay = current_attempt * random_const
        response = poll_third_party(weather_url=weather_url)
        print("Weather API response: {}".format(response.status_code))
        pprint(response)
        if response.status_code == status.HTTP_200_OK:
            weather_status = True
            break
        else:
            current_attempt += 1
            time.sleep(delay)
    return weather_status, response


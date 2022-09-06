#from http.client import HTTPResponse
from django.shortcuts import render

#from django.http import HTTPResponse
from django.shortcuts import HttpResponse


from rest_framework import status
from rest_framework.decorators import api_view
import json



# Create your views here.

@api_view(['GET', 'POST'])
def home(request):
    print("request came at home")
    if request.method == 'GET':
        return HttpResponse("Hello GET Arnab36!")
    elif request.method == 'POST':
        received_json_data=json.loads(request.body)
        print(received_json_data["name"])
        print(received_json_data["status"])
        return HttpResponse("Hello POST Arnab36!")
    

@api_view(['GET'])
def get_only(request):
    print("call came to get only")
    if request.method == 'GET':
        return HttpResponse("Hello GET only Arnab!")
    
@api_view(['POST'])
def post_only(request):
    print("request came at post only")
    if request.method == 'POST':
        received_json_data=json.loads(request.body)
        print(received_json_data["name"])
        print(received_json_data["status"])
        return HttpResponse("Hello POST Pk36!")


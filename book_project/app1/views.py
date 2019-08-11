from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view,renderer_classes
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from rest_framework.renderers import JSONRenderer
from datetime import datetime

def MainPage(request):
    return render(request,'app1/mainpage.html')


def BookLookUp(BookName):
#Function to lookup for the book in database
    pass

def APIBookLookup(BookName):
#Function to lookup for the book through API and populate the db
    pass



def ViewLookBook(request,BookName):
    pass
#Do a book look up
#Store the same in db
#Maintain a dictionary of stuff you want rendered
#return response
#return Response
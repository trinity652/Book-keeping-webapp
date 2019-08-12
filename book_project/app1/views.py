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
import requests
from .models import Book
from rest_framework.renderers import JSONRenderer
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

def MainPage(request):
    return render(request,'app1/mainpage.html')


def BookLookUp(BookId):
    try:
        BookObj=Book.objects.get(Id=BookId)
        x=BookObj.copies
        return x
    except:
        return 0

@api_view(['GET',])
@renderer_classes((JSONRenderer,))
def ViewLookBook(request,BookName):
    Items=[]
    BASE_URL="https://www.googleapis.com/books/v1/volumes?"
    api_key="AIzaSyB4d9wa95P9Di_-hEQ4kuuarpqy09NDC_8"
    r = requests.get(BASE_URL+"q="+str(BookName)+"&key =" +api_key)
    result = json.loads(r.content)
    for val in result["items"]:
        a={}
        if "id" in val:
            a["Id"]=val["id"]
        if "title" in val["volumeInfo"]:
            a["title"]=val["volumeInfo"]["title"]
        if "publisher" in val["volumeInfo"]:
            a["publisher"]=val["volumeInfo"]["publisher"]
        if "authors" in val["volumeInfo"]:
            a["author"]=val["volumeInfo"]["authors"][0]
        a["copies"]=BookLookUp(val["id"])
        Items.append(a)
    
    #newItems=map(dict, Items)
    print(Items)
    return JsonResponse(Items,safe=False)

    

    
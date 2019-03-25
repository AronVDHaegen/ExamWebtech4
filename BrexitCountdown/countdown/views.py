from django.shortcuts import render
from django.http import HttpResponse
import datetime
def hello(request):
  
   #brexit = datetime(2019, 3, 30, 00, 00, 00)
   #result = (brexit - datetime.datetime.now())
   text = """<h1>Time until Brexit: </h1>"""
   return HttpResponse(text)
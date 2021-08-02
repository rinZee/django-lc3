# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http.response import HttpResponse

from django.shortcuts import render

# Create your views here.
def index(request):
	return HttpResponse("Hello!")

def brian(request):
	return HttpResponse("Hello! Brian")

def david(request):
	return HttpResponse("Hello! David")
	
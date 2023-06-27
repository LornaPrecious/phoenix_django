from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse("homepage")

def aboutus(response):
    return HttpResponse("About us")

def contactus(response):
    return HttpResponse("Contact us")




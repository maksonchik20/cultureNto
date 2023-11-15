from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

def main(requests):
    return HttpResponse("I am ready")
#coding=utf-8


#from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    variables = RequestContext(request)
    return render_to_response("lzjindex.html", variables)

def aboutus(request):
    variables = RequestContext(request)
    return render_to_response("aboutus.html", variables)

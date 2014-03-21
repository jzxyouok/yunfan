# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

def navigation(request):
    variables = RequestContext(request)
    return render_to_response("ncepu_nav.html", variables)

def baoding(request):
    variables = RequestContext(request)
    return render_to_response("baoding.html", variables)
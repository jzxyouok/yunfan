#coding=utf-8

from django import forms  
from django.template import RequestContext  
from django.http import HttpResponse, HttpResponseRedirect  
from django.template.loader import get_template  
from django.core.paginator import Paginator  
from django.core.urlresolvers import reverse  
  
# app specific files  
  
from myapps.models import *  
from myapps.forms import *  
  
  
def create_answer(request):  
    #todo 重定向
    form = AnswerForm(request.POST or None)  
    if form.is_valid():  
        form.save()  
        return HttpResponseRedirect("answer/list/")
  
    t = get_template('create_answer.html')  
    c = RequestContext(request,locals())  
    return HttpResponse(t.render(c))  
    

  
  
  
def list_answer(request):  
    
    list_items = Answer.objects.all()  
    paginator = Paginator(list_items ,5)  
  
  
    try:  
        page = int(request.GET.get('page', '1'))  
    except ValueError:  
        page = 1  
  
    try:  
        list_items = paginator.page(page)  
    except :  
        list_items = paginator.page(paginator.num_pages)  
  
    t = get_template('list_answer.html')  
    c = RequestContext(request,locals())  
    return HttpResponse(t.render(c))  
  
  
  
def view_answer(request, id):  
    answer_instance = Answer.objects.get(id = id)  
  
    t=get_template('view_answer.html')  
    c=RequestContext(request,locals())  
    return HttpResponse(t.render(c))  
  
def edit_answer(request, id):  
  
    answer_instance = Answer.objects.get(id=id)  
  
    form = AnswerForm(request.POST or None, instance = answer_instance)  
  
    if form.is_valid():  
        form.save()  
  
    t=get_template('edit_answer.html')  
    c=RequestContext(request,locals())  
    return HttpResponse(t.render(c))  
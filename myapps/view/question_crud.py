#coding=utf-8

from django import forms  
from django.template import RequestContext  
from django.http import HttpResponse, HttpResponseRedirect  
from django.template.loader import get_template  
from django.core.paginator import Paginator  
from django.core.urlresolvers import reverse  
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required  

# app specific files  
  
from myapps.models import *  
from myapps.forms import *  
  
''' 
def create_question(request):  
    #todo 重定向
    form = QuestionForm(request.POST or None)  
    if form.is_valid():  
        form.save()  
        return HttpResponseRedirect("/question/")
  
    t = get_template('create_question.html')  
    c = RequestContext(request,locals())  
    return HttpResponse(t.render(c))  

    if form.is_valid():
            info = form.save(commit=False)
            info.owner = request.user
            info.save()        
            return HttpResponseRedirect("/info/")
'''
@login_required
def create_question(request):  
    #todo 重定向
    if request.method == 'POST':
        form = QuestionForm(request.POST or None)
        if form.is_valid():
            question = form.save(commit=False)
            question.owner = request.user
            question.save()        
            return HttpResponseRedirect("/question/")
    else:
        form =QuestionForm()
        
    return render_to_response("lzj-question-form.html",
            {'form': form,},
            context_instance=RequestContext(request)
            )         

  
  
  
def list_question(request):  
    
    list_items = question.objects.all()  
    paginator = Paginator(list_items ,10)  
  
  
    try:  
        page = int(request.GET.get('page', '1'))  
    except ValueError:  
        page = 1  
  
    try:  
        list_items = paginator.page(page)  
    except :  
        list_items = paginator.page(paginator.num_pages)  
  
    t = get_template('list_question.html')  
    c = RequestContext(request,locals())  
    return HttpResponse(t.render(c))  
  
  
  
def view_question(request, id):  
    question_instance = question.objects.get(id = id)  
  
    t=get_template('view_question.html')  
    c=RequestContext(request,locals())  
    return HttpResponse(t.render(c))  
  
def edit_question(request, id):  
  
    question_instance = question.objects.get(id=id)  
  
    form = QuestionForm(request.POST or None, instance = question_instance)  
  
    if form.is_valid():  
        form.save()  
  
    t=get_template('edit_question.html')  
    c=RequestContext(request,locals())  
    return HttpResponse(t.render(c))  

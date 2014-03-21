# -*- coding:utf-8 -*-  

from django.contrib import auth
from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template import RequestContext 
from forms import MyUserCreationForm,MyLoginForm

def index(request):
    #用户的个人页面
    return render(request,'index.html')  

def login_view(request):
    error = 0
    form = MyLoginForm()
    if request.method == 'POST':
        form = MyLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username=cd['username'], password=cd['password'])
            if user is not None and user.is_active:
                auth.login(request, user)
                from mygroups.myshortcuts import  redirect

                #return HttpResponseRedirect("/")
                return redirect(request)

            else :
                form = MyLoginForm(request.POST)
                error = 1

    return render_to_response("lzjlogin.html",
    {'form': form,'error':error,},
    context_instance=RequestContext(request)
    )

    '''
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/")
    else:
        # Show an error page
        return render_to_response("login.html",
            context_instance=RequestContext(request)
            )        
    '''

def logout_view(request):

    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/")

def register(request):
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = MyUserCreationForm()
    return render_to_response("lzjregister.html",
    {'form': form,},
    context_instance=RequestContext(request)
    )
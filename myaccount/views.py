# -*- coding:utf-8 -*-  
# Create your views here.  
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login as user_login, logout as user_logout  
from django.template import RequestContext


def index(request):
    #用户的个人页面
    return render(request,'index.html')  
 
  
def register(request):  
    #注册提交  
    if request.method == 'POST':  
        form = UserRegisterForm(data=request.POST)  
        if form.is_valid():  
            new_user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])  
            new_user.save()  
            return render(request,'index.html')  
        else:  
            return render(request,'register.html', {'form':form})  
    #超链接点击过来的注册  
    else:  
        return render(request,'register.html')  
#        return render_to_response('user/register.html', context_instance=RequestContext(request))  
      
def login(request):  
    #表单提交过来的数据  
    if request.user.is_authenticated():  
        return  HttpResponse('你已经登录')  
    if request.method == 'POST':  
        username = request.POST['username']  
        password = request.POST['password']  
        user = authenticate(username=username, password=password)  
        if user is not None:  
            if user.is_active:  
                        user_login(request, user)  
                        return HttpResponseRedirect('/%d' % user.id)  
            else:  
                    return HttpResponse('用户没有启用!')  
        else:  
                return HttpResponse('用户名或者密码错误！')  
    else:  
        return render_to_response('login-bootstrap.html')  
      
def logout(request):  
    user_logout(request)  
    return render_to_response('index.html')  
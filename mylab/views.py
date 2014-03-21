#coding=utf-8

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import send_mail

def ajax(request):
	myvar="hello"
	variables = RequestContext(request,{'myvar':myvar})

	#return render_to_response("q_all.html",variables)
	return render_to_response("ajax/1.html",variables)

def sendemail(request):
	myvar="hello"
	variables = RequestContext(request,{'myvar':myvar})
	send_mail(
                'goodjob',
                'hello',
                '2230360562@qq.com',
                ['1162025955@qq.com','710452093@qq.com'],
            )	
	return render_to_response("lzjindex.html",variables)


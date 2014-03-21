#coding=utf-8
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Question,Answer
from django.core.paginator import Paginator  

#todo:按照不同方式取得数据，热度，时间
def show_question_by_time(request, q_id):	
	question = '' 
	try:
        #只是取得数据时不同，其他地方都一样
		question = Question.objects.all().order_by('pub_date')
	except:
		pass
	variables = RequestContext(request,{'question':question})
	return render_to_response("question.html",variables)

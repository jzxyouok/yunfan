#coding=utf-8
#from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Question,Answer
#from datetime import datetime
from django.core.paginator import Paginator  

# Create your views here.


def show_all_questions(request):
	'''
	question_list = []
	try:
		question_list = Question.objects.all().order_by('-id')
		paginator = Paginator(question_list ,10)  
	except:
		pass
	try:  
		page = int(request.GET.get('page', '1'))  
	except ValueError:  
		page = 1  	
	try:  
	    list_items = paginator.page(page)  
	except :  
	    list_items = paginator.page(paginator.num_pages)	
	variables = RequestContext(request,{'list_items':list_items})
	#return render_to_response("q_all.html",variables)
	return render_to_response("lzjquestion.html",variables)
	'''
	list_items = Question.objects.all().order_by('-id')
	variables = RequestContext(request,{'list_items':list_items})
	return render_to_response("lzjquestion.html",variables)


def show_question_by_id(request, q_id):	
	question = '' 
	try:
		question = Question.objects.get(id=q_id)
	except:
		pass
	variables = RequestContext(request,{'question':question})
	return render_to_response("lzj_q_topic.html",variables)
'''
#本地登陆评论,需要pyjwt
from duoshuo.utils import set_duoshuo_token
    response = HttpResponse()
    return set_duoshuo_token(request, response)
'''



def show_all_answers(request):
	answer_list = []
	try:
		answer_list =Answer.objects.all().order_by('-id')
	except:
		pass
	variables = RequestContext(request,{'answer_list':answer_list})
	return render_to_response("a_all.html",variables)

def show_answer_by_question(request, q_id):	 
	answer_list  = '' 
	try:
		answer_list = Answer.objects.filter(question=q_id)  #等效于where
	except:
		pass
	variables = RequestContext(request,{'answer_list':answer_list})
	return render_to_response("answer.html",variables)


#coding=utf-8
from views import show_question_by_id, show_all_questions,show_all_answers,show_answer_by_question
from django.conf.urls.defaults import patterns, url
from view.answer_crud import list_answer,create_answer
from view.question_crud import create_question
urlpatterns = patterns('',
   
    url(r'^$',show_all_questions),
	url(r'^q/(?P<q_id>\d+)/$',show_question_by_id),
	url(r'^qall/$',show_all_questions),
    
    url(r'^aall/$',show_all_answers),
    url(r'^a/(?P<q_id>\d+)/$',show_answer_by_question),
    
	
)


urlpatterns += patterns('',  
    (r'answer/list/$', list_answer ),
    (r'answer/create/$', create_answer ),  
    url(r'question/create/$', create_question,name="create_question" ),  
    
) 

'''
我推荐的方法是使用url name，即把url pattern定义如下：
(r'^accounts/login/$', login_view, name = 'login_view'),
(r'^accounts/logout/$', logout_view, name = 'logout_view'),
{% url login_view %}
{% url logout_view %}
这样的方式不依赖项目结构
'''
urlpatterns += patterns('',  
    (r'^answer/list/$', list_answer ),

)
'''
urlpatterns += patterns('',    
    (r'question/create/$', create_question),  
    (r'question/list/$', list_question ),  
    (r'question/edit/(?P<id>[^/]+)/$', edit_question),  
    (r'question/view/(?P<id>[^/]+)/$', view_question),  
) 
'''


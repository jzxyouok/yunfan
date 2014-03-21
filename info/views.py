#coding=utf-8
from django.shortcuts import render_to_response
from models import Information,InfoCategories
from django.template import RequestContext
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from django.shortcuts import render_to_response, get_object_or_404
from django.utils import simplejson as json



def show_all_information(request): #包含分页功能
	categories=InfoCategories.objects.order_by('order')
	list_items = Information.objects.all()
	variables = RequestContext(request,{'list_items':list_items,'categories':categories})
	return render_to_response("lzj_info.html",variables)
    

def show_information_by_id(request, info_id):	
	information = '' 
	try:
		information = Information.objects.get(id=info_id)
	except:
		pass

	categories=InfoCategories.objects.order_by('order')
	variables = RequestContext(request,{'information':information,'categories':categories})
	return render_to_response("wwj_detail.html",variables)

def search_by_title(request):
	query=request.GET.get("title",'')
	list_items = Information.objects.filter( Q(title__icontains=query)|Q(content__icontains=query) )#content__icontains=search_word
	categories=InfoCategories.objects.order_by('order')


	variables = RequestContext(request,{'list_items':list_items,'categories':categories})
	return render_to_response("lzj_info.html",variables)


def show_by_categories(request,categories):
	list_items = Information.objects.filter(categories=categories)#content__icontains=search_word
	categories=InfoCategories.objects.order_by('order')


	variables = RequestContext(request,{'list_items':list_items,'categories':categories})
	return render_to_response("lzj_info.html",variables)

def show_by_tag(request,tag):
	list_items = Information.objects.filter(tags__name__in=[tag])#content__icontains=search_word
	categories=InfoCategories.objects.order_by('order')


	variables = RequestContext(request,{'list_items':list_items,'categories':categories})
	return render_to_response("lzj_info.html",variables)
#联合查询
#https://docs.djangoproject.com/en/dev/topics/db/queries/#query-expressions
#from django.db.models import Q
#Q(question__startswith='What')
#Q(question__startswith='Who') | Q(question__startswith='What')
#用正则表达式可以为匹配的文字着色，首先选定范围在title 和 content里

#关注
# 以接口来编程   userid(request),infoid
@login_required
def view(request,info_id,template_name='wwj_detail.html'):
	from_user = request.user
	info = get_object_or_404(Information, id=int(info_id))


	if request.method == 'POST':
		info.viewers.add(from_user)
		info.save()
		#next = request.GET.get('next', None)
		return HttpResponseRedirect('')
		if next:
		 	return HttpResponseRedirect(next)

		# if request.is_ajax():
		# 	response = {
  #               'success': 'Success',
  #           }
		# 	return HttpResponse(json.dumps(response), mimetype="application/json")
		# # if next:
		# # 	return HttpResponseRedirect(next)


	categories=InfoCategories.objects.order_by('order')
	context = {
        'Success': 'Success',
        'information':info,
        'categories':categories,
        #'next': next
    }
	return render_to_response(template_name, context, context_instance=RequestContext(request))




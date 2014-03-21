#coding=utf-8

from django.template import RequestContext  
from django.http import HttpResponse, HttpResponseRedirect  
from django.template.loader import get_template  
from info.forms import InformationForm
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required


@login_required
def create_info(request):  
    #todo 重定向
    if request.method == 'POST':
        '''
        owner = request.user.id
        if not owner:
            owner = 0
        owner = int(request.user.id)
        
        getdata = { "owner":1,
                    "website":request.POST.get('website', ''),
                    "topic":request.POST.get('topic', ''),
                    "title":request.POST.get('title', ''),
                    "description":request.POST.get('description', ''),
                    "end_date":request.POST.get('end_date', ''),
                        
                  }
        form = InformationForm(getdata or None)  
        if form.is_valid():  
                   form.save()  
                   return HttpResponseRedirect("/info/")        
        '''
        form = InformationForm(request.POST or None)
        if form.is_valid():
            info = form.save(commit=False)
            info.owner = request.user
            info.save()        
            return HttpResponseRedirect("/info/")
    else:
        form =InformationForm()
        
    return render_to_response("create_info.html",
            {'form': form,},
            context_instance=RequestContext(request)
            )        

#test user for use it 
def show_user(request):
    theuser = request.user.id
    t = get_template('show_user.html')  
    c = RequestContext(request,locals())  
    return HttpResponse(t.render(c))     
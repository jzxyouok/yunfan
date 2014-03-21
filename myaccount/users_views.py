# -*- coding:utf-8 -*-  
# Create your views here.  
from django.shortcuts import render_to_response,render,get_object_or_404  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login as user_login, logout as user_logout  
from django.template import RequestContext
from django.contrib.auth.models import User 

#关注资讯
from info.models import Information

from myrelationships.models import Relationship


from mygroups.models import  GroupMember


def user(request,username):
    #用户的个人页面
    #反向查询
    template_name='lzj-user.html'
    # if username=='wwj':
    #     template_name='wwjhome.html'

    #获取当前主页君的关系
    theuser = get_object_or_404(User, username=username)#当前主页君
    theuser_following_ids = Relationship.objects.get_friends_for_user(theuser ,flat=True)
    theuser_followers_ids = Relationship.objects.get_followers_for_user(theuser,flat=True)
    theuser_following = User.objects.filter(pk__in=theuser_following_ids)
    theuser_followers = User.objects.filter(pk__in=theuser_followers_ids)



    #关注
    from_user = request.user
    to_user = get_object_or_404(User, username=username)
    next = request.GET.get('next', None)
    following_ids = Relationship.objects.get_friends_for_user(from_user)
    followers_ids = Relationship.objects.get_followers_for_user(to_user,flat=True)
    following = User.objects.filter(pk__in=following_ids)
    followers = User.objects.filter(pk__in=followers_ids)

    #关注资讯

    viewed_Information = from_user.viewers.all()
    Information.objects.filter()

    user_groupmember=GroupMember.objects.filter(user=1)[0:9]

    return render_to_response(template_name, {
        'user_groupmember': user_groupmember,
        'username':username,
        
#当前主页君的关系数据：
        'theuser':theuser,
        'theuser_following':theuser_following,
        'theuser_followers':theuser_followers,

        #服务于用户关注按钮
        'to_user':to_user,
        'from_user':from_user,
        'following':following,
        'followers':followers,

        #资讯关注
        'viewed_Information':viewed_Information,


    },context_instance=RequestContext(request))


def userself(request):
    #用户的个人页面
    #反向查询
    user_groupmember=GroupMember.objects.filter(user=request.user)[0:9]

    return render(request, 'lzj-user.html', {
        'user_groupmember': user_groupmember,

    })

#myself
def wwj(request,username):
    #用户的个人页面
    #反向查询
    theuser = User.objects.filter(username=username)
    user_groupmember=GroupMember.objects.filter(user=1)[0:9]

    return render(request, 'wwjhome.html', {
        'user_groupmember': user_groupmember,
        'username':username,
        'theuser':theuser,

    })

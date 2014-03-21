#coding=utf-8

from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from mygroups.decorators import *
from mygroups.models import *
from mygroups.forms import *
from mygroups.myshortcuts import render, redirect

from django.core.paginator import Paginator  



#小组广场
def group_list(request, username=None,
        template_name='groups/lzj-group-square.html'):
    """
    Returns a group list page.

    Templates: ``groups/group_list.html``
    Context:
        group_list
            Group object list
    """
    group_list = Group.objects.filter(is_active=True) #pass
    nav_group_list = Group.objects.filter(is_active=True).order_by("-created")[0:9]#pass

    if request.user.is_authenticated():
        #用户属于的组
        membership_list = group_list.filter(members__user=request.user)
    else:
        membership_list = []
    return render(request, template_name, {
        'group_list': group_list,
        'nav_group_list': nav_group_list,
        'membership_list': membership_list
    })


@login_required #需要登陆,合理
def group_create(request, template_name='groups/lzj-create-group.html'):
    """
    Returns a group form page.

    Templates: ``groups/group_form.html``
    Context:
        form
            GroupForm object
    """

    '''
    # 限制图片大小
    image=request.FILES['cion']
    if image.size > 500000:
        return HttpResponse(‘上传的图片大小不能超过500K’)
    '''
    if request.method == 'POST':

        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            #验证图片大小
            image=request.FILES['icon']
            if image.size > 500000:
                form = GroupForm()
                size_error='上传的图片大小不能超过500K'
                return render(request, template_name, {'form': form,'size_error':size_error})
            
            group = form.save(commit=False)
            group.creator = request.user
            group.save()
            creator = GroupMember.objects.create(user=request.user, group=group, status=0)
            return redirect(request, group)
    else:
        form = GroupForm()
    return render(request, template_name, {'form': form})


def group_detail(request, pk, template_name='groups/lzj-group.html'):
    """
    Returns a group detail page.

    Templates: ``groups/group_detail.html``
    Context:
        group
            Group object
    """
    #分页
    group = get_object_or_404(Group, pk=pk, is_active=True)
    member_list = group.members.all()
    if group.invite_only and not GroupMember.objects.is_member(group, request.user):
        return redirect(request, reverse('groups:join', kwargs={'pk': group.pk})) 
    topic_list = group.topics.all()
    return render(request, template_name, {
        'group': group,
        'topic_list': topic_list,
        'member_list':member_list,
    })

    '''    
    group = get_object_or_404(Group, pk=pk, is_active=True)
    if group.invite_only and not GroupMember.objects.is_member(group, request.user):
        return redirect(request, reverse('groups:join', kwargs={'pk': group.pk}))
    return render(request, template_name, {
        'group': group,
        'topic_list': group.topics.all(),
    })
    '''

@ownership_required
def group_edit(request, pk, template_name='groups/wwj-groupchange-form.html'):
    """
    Returns a group form page.

    Templates: ``groups/group_form.html``
    Context:
        form
            GroupForm object
        group
            Group object
    """
    group = get_object_or_404(Group, pk=pk, creator=request.user)
    form = GroupForm(instance=group)

    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES, instance=group)
        if form.is_valid():
            form.save()
            return redirect(request, group)
    return render(request, template_name, {
        'form': form,
        'group': group
    })


@ownership_required
def group_remove(request, pk, template_name='groups/group_remove_confirm.html'):
    """
    Returns a group delete confirmation page.

    Templates: ``groups/group_remove_confirm.html``
    Context:
        group
            Group object
    """
    group = get_object_or_404(Group, pk=pk, creator=request.user)
    if request.method == 'POST':
        group.is_active = False
        group.save()
        return redirect(request, reverse('groups:groups'))
    return render(request, template_name, {'group': group})


def group_members(request, pk, template_name='groups/group_members.html'):
    """
    Returns members of a group.

    Templates: ``groups/group_members.html``
    Context:
        group
            Group object
        member_list
            User objects
    """
    group = get_object_or_404(Group, pk=pk, is_active=True)
    member_list = group.members.all()
    return render(request, template_name, {
        'group': group,
        'member_list': member_list
    })


@login_required
def group_join(request, pk, template_name='groups/group_join_confirm.html'):
    """
    Returns a group join confirmation page.

    Templates: ``groups/group_join_confirm.html``
    Context:
        group
            Group object
    """
    group = get_object_or_404(Group, pk=pk, is_active=True)
    if request.method == 'POST':
        membership = GroupMember(group=group, user=request.user)
        membership.save()
        return redirect(request, group)
    return render(request, template_name, {'group': group})


@membership_required
def group_invite(request, pk, template_name='groups/group_invite.html'):
    """
    Returns an invite form.
    
    Templates: ``groups/group_invite.html``
    Context:
        form
            GroupInviteForm object
    """
    group = get_object_or_404(Group, pk=pk, is_active=True)
    form = GroupInviteForm(initial={'group': group.pk, 'user': request.user.pk})
    return render(request, template_name, {
        'group': group,
        'form': form
    })

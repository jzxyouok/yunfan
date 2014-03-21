from django.shortcuts import get_object_or_404

from mygroups.decorators import *
from mygroups.models import *
from mygroups.forms import *
from mygroups.myshortcuts import render, redirect
from django.contrib.auth.decorators import login_required



def topic_list(request, pk, template_name='groups/topics/topic_list.html'):
    """
    Returns a group topic list page.

    Templates: ``groups/topics/topic_list.html``
    Context:
        group
            Group object
        topic_list
            GroupTopic object list
    """
    group = get_object_or_404(Group, pk=pk, is_active=True)
    topic_list = GroupTopic.objects.filter(group=group, is_active=True)
    return render(request, template_name, {
        'group': group,
        'topic_list': topic_list
    })

@login_required
@membership_required
def topic_create(request, pk, template_name='groups/topics/lzj-create-topic.html'):
    """
    Returns a group topic form page.

    Templates: ``groups/topics/topic_form.html``
    Context:
        form
            GroupTopicForm object
    """
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        form = GroupTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.user = request.user
            topic.group = group
            topic.save()
            return redirect(request, topic)
    else:
        form = GroupTopicForm()
    return render(request, template_name, {
        'form': form,
        'group': group
    })


def topic_detail(request, pk, topic_id,
        template_name='groups/topics/lzj_g_topic.html'):
    """
    Returns a group topic detail page.

    Templates: ``groups/topics/topic_detail.html``
    Context:
        topic
            GroupTopic object
        group
            Group object
    """
    group = get_object_or_404(Group, pk=pk, is_active=True)
    topic = get_object_or_404(GroupTopic, pk=topic_id, is_active=True)
    messages = topic.messages.all
    message_form = GroupMessageForm()
    return render(request, template_name, {
        'group': group,
        'topic': topic,
        'messages':messages,
        'message_form': message_form,
    })


@membership_required
def topic_edit(request, pk, topic_id,
        template_name='groups/topics/topic_form.html'):
    """
    Returns a group topic form page.

    Templates: ``groups/topics/topic_form.html``
    Context:
        form
            GroupTopicForm object
        topic
            GroupTopic object
    """
    group = get_object_or_404(Group, pk=pk)
    topic = get_object_or_404(GroupTopic, pk=topic_id, group=group, user=request.user)
    if request.method == 'POST':
        form = GroupTopicForm(request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect(request, topic)
    else:
        form = GroupTopicForm(instance=topic)
    return render(request, template_name, {
        'form': form,
        'group': group,
        'topic': topic
    })


@membership_required
def topic_remove(request, pk, topic_id,
        template_name='groups/topics/topic_remove_confirm.html'):
    """
    Returns a group topic delete confirmation page.

    Templates: ``groups/topics/topic_remove_confirm.html``
    Context:
        topic
            GroupTopic object
    """
    group = get_object_or_404(Group, pk=pk)
    topic = get_object_or_404(GroupTopic, pk=topic_id, group=group, user=request.user)
    if request.method == 'POST':
        topic.is_active = False
        topic.save()
        return redirect(request, group)
    return render(request, template_name, {'topic': topic})

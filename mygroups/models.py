#coding=utf-8
from django.db import models
from django.db.models import permalink

#以user为中心
from django.contrib.auth.models import User
from django.conf import settings

from mygroups.myshortcuts import build_filename


GROUP_OWNER = 0
GROUP_MODERATOR = 1
GROUP_MEMBER = 2
GROUP_MEMBER_CHOICES = (
    (GROUP_OWNER, 'Owner'),
    (GROUP_MODERATOR, 'Moderator'),
    (GROUP_MEMBER, 'Member')
)


def get_icon_path(instance, filename):
    if instance.pk:
        group = Group.objects.get(pk=instance.pk)
        if group.icon:
            return group.icon.path.replace(settings.MEDIA_ROOT, '')
    return build_filename(instance, filename)


class Group(models.Model):
    """ Group model """
    #唯一？
    title = models.CharField(blank=False, max_length=255,unique=True)
    #小组名称,用于url,作用类似id
    #slug = models.SlugField(unique=True, help_text="小组名称")
    #描述组是什么
    tease = models.TextField(blank=True, help_text="小组描述")

    use_markdown =  models.BooleanField(default=False,blank=True)

    creator = models.ForeignKey(User, related_name='created_groups', help_text="Serves as a record as who the original creator was in case ownership is transfered.")
    #路径正常可用
    icon = models.FileField(upload_to=get_icon_path, blank=True, help_text="必须大于 120x120 像素")
    #邀请
    invite_only = models.BooleanField(default=False,help_text="需要邀请")
    #审核？
    is_active = models.BooleanField(default=False)
    #创建时间
    created = models.DateTimeField(auto_now_add=True)
    #修改时间
    modified = models.DateTimeField(auto_now=True)

#SlugField:嵌条 就是一段内容的简短标签，这段内容只能包含字母、数字、下划线或连字符。通常用于URL中



    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('group', None, {'pk': self.pk})
    

    
    def owners(self):
        return self.members.filter(status=0)

    def moderators(self):
        return self.members.filter(status=1)

    def is_member(self, user):
        try:
            member = self.members.get(user=user)
            return member
        except:
            return None

#在Templates里 使用{%blog. get_absolute_url%} 解析出来的地址就是我们想要的了地址字符串：


class GroupPage(models.Model):
    """ GroupPage model """
    group = models.ForeignKey(Group, related_name='pages')
    title = models.CharField(blank=True, max_length=100)
    slug = models.SlugField(help_text='Used for the page URL.')
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = (('slug', 'group'),)

    @permalink
    def get_absolute_url(self):
        return ('page', None, {
            'pk': self.group.pk,
            'page_slug': self.slug
        })


class GroupTopic(models.Model):
    """ GroupTopic model """
    group = models.ForeignKey(Group, related_name='topics')
    user = models.ForeignKey(User, related_name='group_topics')
    title = models.CharField(blank=False, max_length=100)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-id',)

    def __unicode__(self):
        return self.title
    '''
    @permalink
    def get_absolute_url(self):
        return ('groups:topic', [self.group.slug, self.pk])
    '''
    
    @permalink
    def get_absolute_url(self):
        return ("topic", None,{ "pk":self.group.pk,
                                "topic_id":self.pk,})
    
    @permalink
    def get_edit_url(self):
        return ("topic_edit", None,{ "pk":self.group.pk,
                                    "topic_id":self.pk,})    
    '''
    def get_edit_url(self):
        return ('groups:topic_edit', [self.group.slug, self.pk])
    '''
#'groups:topic_edit',use for input /topic_edit/
    @permalink
    def get_edit_url(self):
        return ("topic_remove", None,{ "pk":self.group.pk,
                                        "topic_id":self.pk,})        
    '''
    def get_remove_url(self):
        return ('groups:topic_remove', [self.group.slug, self.pk])
    '''

class GroupMessageManager(models.Manager):
    """Returns messages that are flagged as active."""

    def get_query_set(self):
        return super(GroupMessageManager, self).get_query_set().filter(is_active=True)


class GroupMessage(models.Model):
    """ GroupMessage model """
    topic = models.ForeignKey(GroupTopic, related_name="messages")
    user = models.ForeignKey(User)
    message = models.TextField(blank=False)
    is_active = models.BooleanField(default=True)
    objects = GroupMessageManager()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.message

    class Meta:
            ordering = ('-id',)
    @permalink
    def get_absolute_url(self):
        return ("message", None,{           "pk":self.topic.group.pk,
                                            "topic_id":self.topic.pk,
                                            "message_id":self.pk,})         
        '''
        return ('groups:message',
            [self.topic.group.slug, self.topic.pk, self.pk])
        '''
    @permalink
    def get_edit_url(self):
        return ("message_edit", None,{"pk":self.topic.group.pk,
                                 "topic_id":self.topic.pk,
                                 "message_id":self.pk,})          
    '''
    def get_edit_url(self):
        return ('groups:message_edit',
        [self.topic.group.slug, self.topic.pk, self.pk])
    '''
    
    
    @permalink
    def get_remove_url(self):
        return ("message_remove", None,{"pk":self.topic.group.pk,
                                         "topic_id":self.topic.pk,
                                         "message_id":self.pk,})         
        '''
        return ('groups:message_remove',
            [self.topic.group.slug, self.topic.pk, self.pk])
        '''

class GroupMemberManager(models.Manager):
    """Returns memebers that belong to a group"""
    def is_member(self, group, user):
        if user.is_anonymous():
            return False
        if self.filter(group=group, user=user).count() > 0:
            return True
        return False

    def is_owner(self, group, user):
        if user.is_anonymous():
            return False
        if self.filter(group=group, user=user, status=GROUP_OWNER).count() > 0:
            return True
        return False

    def is_moderator(self, group, user):
        if user.is_anonymous():
            return False
        if self.filter(group=group, user=user, status__in=(GROUP_MODERATOR, GROUP_OWNER)).count() > 0:
            return True
        return False


class GroupMember(models.Model):
    """ GroupMember model """
    user = models.ForeignKey(User, related_name='group_memberships')
    group = models.ForeignKey(Group, related_name='members')
    status = models.PositiveSmallIntegerField(choices=GROUP_MEMBER_CHOICES, default=GROUP_MEMBER)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = GroupMemberManager()

    class Meta:
        unique_together = (('user', 'group'),)

    def __unicode__(self):
        return self.user.username

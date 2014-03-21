#coding=utf-8
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User


class InfoCategories(models.Model):
    name = models.CharField(max_length=50,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField() #用来后台控制排序
    class Meta:
        verbose_name = '分类'
        ordering = ['order']
    def __unicode__(self):
        return self.name


class Information(models.Model):
    owner = models.ForeignKey(User,related_name='owner')  #get from request.user
    #contect = models.CharField(max_length=100,blank=True)    #联系方式
    #website = models.URLField(max_length=200,blank=False)   
    #主题
    #topic = models.CharField(max_length=100) 
    #creator = models.ForeignKey(User, related_name='created_info')
    #关注者
    viewers = models.ManyToManyField(User,related_name='viewers',blank=True)
    title = models.CharField(max_length=100)
    categories = models.ForeignKey(InfoCategories)   #外键,建立数据联系
    tags = TaggableManager() #第三方标签

    content = models.TextField()
    #use_marndown =  models.BooleanField(default=False,blank=True)

    pub_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=False,null=True)    
    #todo:热度

    #willhost = models.BigIntegerField(default=0) # 

    ishosting = models.BigIntegerField(default=0,help_text='资金托管金额') #资金托管数额


    heat =  models.BigIntegerField(default=0, help_text='热度')
    #审核
    ischeck = models.BooleanField(default=False, help_text ='是否审核')
    #过期
    istimeout = models.BooleanField(default=False,help_text='是否过期')

    def __unicode__(self):
    		return " %s " % self.title

    class Meta:
        ordering = ['-id']

#coding=utf-8
from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Question(models.Model):
    #CLASS_TYPE_CHOICES = (
    #		(u'e',u'生活'),
    #		(u'm',u'学习'),
    #		(u'h',u'社团'),    
    owner = models.ForeignKey(User)
    title = models.CharField(max_length=100)
    description = models.TextField()    
    #class_type = models.CharField(max_length=1,choices= CLASS_TYPE_CHOICES) # easy ; difficult ; hard
    #todo:热度
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
    		return " %s " % self.title
    '''    
    class Meta:
            verbose_name = '文章类名' #作用？
            verbose_name_plural = '文章类型列表' #作用？
            #按标签名排序
            ordering = ['id']    
     '''   
class Answer(models.Model):
    owner = models.ForeignKey(User)
    question = models.ForeignKey(Question)
    description = models.TextField()
#	title = models.CharField(max_length=100)
#	isRight = models.BooleanField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
		return "%s" % self.owner

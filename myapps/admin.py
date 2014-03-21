#coding=utf-8

from django.contrib import admin
from myapps.models import Question,Answer

admin.site.register(Question)
admin.site.register(Answer)


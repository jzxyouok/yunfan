from django.core.urlresolvers import reverse
from rest_framework.views import View
from rest_framework.resources import ModelResource
from models import *

class QuestionResource(ModelResource):
    model = Question
    fields = ('title ', 'description', 'pub_date')
    

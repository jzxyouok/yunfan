#coding=utf-8
#todo 从前台表单传来问题id数据
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput
from django import forms  
from models import Information


'''
class InformationForm(forms.ModelForm):  #ModelForm  使form能save数据到数据库
      
    class Meta:   #关联起来
        model = Information 
        fields = ("contect","website","topic","title","description","end_date","owner",)     
    
    end_date=forms.DateField(widget=BootstrapDateInput())
    
    def __init__(self, *args, **kwargs):  
        super(InformationForm, self).__init__(*args, **kwargs)  
  
    def clean_description(self):  
        description = self.cleaned_data['description']  
        if len(description) <=8:  
            raise forms.ValidationError("拜托，多些几个字会死啊")  
        return description  
    def clean_owner(self):  
        owner = self.cleaned_data['owner'] 
        if owner == 'lzj' :
            raise forms.ValidationError('这个问题让wwj来回答')  
        return owner 
'''

class InformationForm(forms.ModelForm): 
    class Meta:
        model = Information
        exclude = ('owner', 'heat', 'ischeck','istimeout')
    end_date=forms.DateField(widget=BootstrapDateInput())
    def clean_description(self):  
            description = self.cleaned_data['description']  
            if len(description) <=8:  
                raise forms.ValidationError("字数不够")  
            return description      
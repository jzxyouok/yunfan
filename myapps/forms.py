#coding=utf-8
#todo 从前台表单传来问题id数据

from django import forms  
from models import Answer,Question
  
class AnswerForm(forms.ModelForm):  #ModelForm  使form能save数据到数据库
      
    class Meta:  
        model = Answer#关联起来    
  
    description = forms.CharField(label=("问题描述"),
                max_length=200,
                widget=forms.Textarea(),
                
                error_messages={'invalid': ("")}
                )   


    def __init__(self, *args, **kwargs):  
        super(AnswerForm, self).__init__(*args, **kwargs)  
  
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
      
   
class QuestionForm(forms.ModelForm):  #ModelForm  使form能save数据到数据库
      
    class Meta:  
        model = Question#关联起来 
        exclude = ('owner')

    title = forms.CharField(label=(""),
                    max_length=30,
                    widget=forms.TextInput(attrs={'placeholder': '问题名称', }),

                    
                    error_messages={'invalid': ("")}
                    )  
    description = forms.CharField(label=(""),
                max_length=200,
                widget=forms.Textarea(attrs={'placeholder': '问题描述', }),
                
                error_messages={'invalid': ("字数不够")}
                )   

  
    def __init__(self, *args, **kwargs):  
        super(QuestionForm, self).__init__(*args, **kwargs)  
  
    def clean_description(self):  
        description = self.cleaned_data['description']  
        if len(description) <=8:  
            raise forms.ValidationError("字数不够")  
        return description  
    def clean_owner(self):  
        owner = self.cleaned_data['owner'] 
        if owner == 'lzj' :
            raise forms.ValidationError('这个问题让wwj来回答')  
        return owner
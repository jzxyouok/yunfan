#coding=utf-8

from django import forms
from django.contrib.auth.models import User

from mygroups.models import *


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = ('creator', 'is_active','invite_only')
#得使用英文,用id吧
    title = forms.CharField(label=("小组名称"),
                max_length=15,
                widget=forms.TextInput(attrs={'placeholder': '15个字之内', }),

                #error_messages={'invalid': ("只能用字母、数字和字符")}
                ) 
    # slug = forms.CharField(label=("小组标识"),
    #             max_length=30,
    #             widget=forms.TextInput(attrs={'placeholder': '小组标识,用于url,只能用英文', }),
    #             error_messages={'invalid': ("只能用字母、数字和字符")}
    #             ) 

    tease = forms.CharField(label=("小组描述"),
                #max_length=140,
                widget=forms.Textarea(attrs={'placeholder': '小组描述', }),
                
                error_messages={'invalid': ("")}
                )
    icon = forms.FileField(label=("小组图片"),                
                help_text='图片尺寸最好为140X140',
                error_messages={'invalid': ("")},
                ) 

    def clean_tease(self):  
        tease = self.cleaned_data['tease']  
        if len(tease) <=8:  
            raise forms.ValidationError("字数不够")  
        return tease  



class GroupTopicForm(forms.ModelForm):
    class Meta:
        model = GroupTopic
        exclude = ('group', 'user', 'is_active')


class GroupMessageForm(forms.ModelForm):
    class Meta:
        model = GroupMessage
        exclude = ('topic', 'user', 'is_active')


class GroupInviteForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.HiddenInput)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), widget=forms.HiddenInput)
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class GroupPageForm(forms.ModelForm):
    class Meta:
        model = GroupPage
        exclude = ('group',)
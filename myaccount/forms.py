#coding=utf-8
from django import forms  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import auth
#验证码
from captcha.fields import CaptchaField


class MyUserCreationForm(UserCreationForm): 
    username = forms.RegexField(label=("用户名"), max_length=30,
                regex=r'^[\w.@+-]+$',
                widget=forms.TextInput(attrs={'placeholder': '只能用字母、数字和字符', }),

                #help_text=("只能用字母、数字和字符."), #use placeholder to replace it
                error_messages={
                    'invalid': ("只能用字母、数字和字符")})     
    email = forms.EmailField(label=("Email"),
                 #   help_text=("请输入您的邮箱"),
                    widget=forms.TextInput(attrs={'placeholder': '邮件', }),
                    error_messages={'invalid': ("请输入正确的邮箱")},
    #验证码
    

                    ),  

    first_name = forms.CharField(label=("昵称"),
                 #   help_text=("请输入您的邮箱"),
                    widget=forms.TextInput(attrs={'placeholder': '昵称(可选)', }),    
                    )

    captcha = CaptchaField(label=("验证码"),
                           error_messages={'invalid': ("验证码有误")},
        )

    class Meta:
             model = User
             fields = ("username","email","first_name")     
    
    def clean_email(self):
            # Since email is unique, this check is redundant,
            email = self.cleaned_data["email"]
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError('邮箱已被注册')    

    def clean_first_name(self):
            # Since email is unique, this check is redundant,
            first_name = self.cleaned_data["first_name"]
            try:
                User.objects.get(first_name=first_name)
            except User.DoesNotExist:
                return first_name
            raise forms.ValidationError('昵称已被使用') 

class MyLoginForm(forms.Form): 
    username = forms.CharField(required=True,
                                label='用户名',
                                widget=forms.TextInput(attrs={'placeholder': '用户名', })
                                )
    password = forms.CharField(required=True,label='密码',widget=forms.PasswordInput(
                                                    attrs={'placeholder': '密码', }))
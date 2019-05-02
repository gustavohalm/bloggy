from django import forms
from blog import  models
from django.contrib.auth.models import User

class Post(forms.Form):
    title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class':'inputs', 'placeholder':'Titulo do Post'}))
    content = forms.CharField( widget=forms.TextInput( attrs={'class':'text', 'placeholder':'Digite aqui se texto... '}))

class Comment(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['author', 'content']

class Login(forms.Form):
    username = forms.CharField(max_length=128, label=False, widget=forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Username'}))
    password = forms.CharField(max_length=20, label=False, widget=forms.PasswordInput(attrs={'class': 'inputs', 'placeholder': '******'}))

class Cadastro(forms.Form):
    username = forms.CharField(max_length=128, label=False, widget=forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Username'}))
    first_name = forms.CharField(max_length=128, label=False,
                               widget=forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Primeiro nome'}))
    last_name = forms.CharField(max_length=128, label=False,
                               widget=forms.TextInput(attrs={'class': 'inputs', 'placeholder': 'Sobrenome'}))

    email    =  forms.CharField(max_length=228, label=False, widget=forms.EmailInput(attrs={'class': 'inputs', 'placeholder': 'Email'}))
    password = forms.CharField(max_length=20, label=False, widget=forms.PasswordInput(attrs={'class': 'inputs', 'placeholder': '******'}))


class Profile(forms.ModelForm):
    class Meta:
        model = models.Profile
        exclude = ['user']
        labels= {
            'gender' : '',
            'age':''
        }
from blog  import forms, models
from django import forms as fo
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect,get_object_or_404
from django.views.generic import ( TemplateView, ListView, DetailView,CreateView)
from django.views.generic.edit import FormView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

class AboutView(TemplateView):
    template_name = 'index.html'

class Home(ListView):
    template_name = 'index.html'
    model = models.Post
    def get_query(self):
        return Post.objects.filter(published_data__lte = timezone.now().order_by('published_data'))

class Post(DetailView):
    model = models.Post
    template_name = 'post_detail.html'

def Comment(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    if request.method == "POST":
        form = forms.Comment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
    url =  '/post/' + str(pk)

    return redirect(url)
class CreatePost(CreateView):
    login_url = '/login'
    template_name =  'post_create.html'
    model = models.Post
    fields = ['author', 'title', 'content']
    success_url = '/home'

#Criar pagina de perfil do usuário
class ProfileView(DetailView):
    model = models.Profile





#login, cadastro and logout
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/home/")
        else:
            error = 'Usuário/Senha inválida'
    else:
        form  = forms.Login
        return render(request, 'login.html', {'form' : form})

def cadastro(request):
    if request.method == 'POST':
        form = forms.Cadastro(request.POST)
        form2 = forms.Profile(request.POST)
        if form.is_valid() and form2.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            sex = form2.cleaned_data['gender']
            age = form2.cleaned_data['age']
            #photo = form2.cleaned_data['photo']
            #create the auth.User
            new_user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
            new_user.save()
            # create the blog.Profile
            new_profile = models.Profile(age=age, gender=sex)
            new_profile.user = new_user
            new_profile.save()
            return redirect('/login/')
    else:
        form = forms.Cadastro
        form2 = forms.Profile
    return render(request, 'cadastro.html', {'form': form, 'form2': form2})

def logout_view(request):
    logout(request)
    return redirect('/home/')
from blog.models import BlogModel
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import BlogModel

class BlogTop(TemplateView):
    template_name = 'blog/top.html'

def signupview(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        errors = []

        if username == '':
            errors.append('ユーザー名が空です')
        
        if email == '':
            errors.append('メールアドレスが空です')
        
        if password == '':
            errors.append('パスワードが空です')
        
        if len(errors) > 0:
            return render(request, 'blog/signup.html', { 'errors' : errors })
        
        else:
            try:
                user = User.objects.create_user(username, email, password)
                login(request, user)
                return redirect('blog:list')
            
            except IntegrityError:
                errors.append('ユーザー登録に失敗しました')
                return render(request, 'blog/signup.html', {'errors' : errors })
    
    else:
        return render(request, 'blog/signup.html', {})
    
    return render(request, 'blog/signup.html', {})

def loginview(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('blog:list')
        else:
            return redirect('blog:login')
    
    return render(request,'blog/login.html')

def logoutview(request):
    logout(request)
    return redirect('blog:login')

class BlogList(ListView):
    template_name = 'blog/list.html'
    model = BlogModel

class BlogArticle(DetailView):
    template_name = 'blog/article.html'
    model = BlogModel
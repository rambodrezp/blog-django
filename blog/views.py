from django.shortcuts import render
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # این خط باعث ورود خودکار می‌شه
            return redirect('post_list')  # یا هر صفحه‌ای که می‌خوای بری
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
from django.contrib import admin
from django.urls import path , include
from django.contrib.auth import views as auth_views
from blog import views as blog_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('register/', blog_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/profile/', auth_views.LoginView.as_view(), name='profile'),
]

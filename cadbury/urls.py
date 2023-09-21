"""cadbury URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import home,register_user,frame1,otp,frame2,frame3,frame4,frame5,frame6
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('homee', frame1, name='frame1'),
    path('frame3', frame2, name='frame3'),
    path('frame4', frame3, name='frame4'),
    path('frame5', frame4, name='frame5'),
    path('frame6', frame5, name='frame6'),
    path('frame7', frame6, name='frame7'),




    path('register', register_user, name='register_user'),
    path('otp', otp, name='otps'),


]

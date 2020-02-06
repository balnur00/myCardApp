"""cardApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from main.views import views
from main.views import auth


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('main/', include('main.urls')),
    path('employeeList/', views.EmployeeList.as_view()),
    path('bossCreate/', views.BossCreate.as_view()),
    path('empCreate/', views.EmployeeCreate.as_view()),
    path('softSkillCreateList/', views.SoftSkillCreateList.as_view()),
    path('hardSkillCreateList/', views.HardSkillCreateList.as_view()),
    path('employee/<int:pk>/', views.EmployeeDetail.as_view()),
    path('roles/', views.RoleList.as_view()),
    path('signup/', auth.signup),
    path('login/', auth.login),
    path('logout/', auth.logout),
]

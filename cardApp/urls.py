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
from main.views import auth, userViews, employeeViews, roleViews, skillViews, typeViews
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
#boss
    path('userCreate/', userViews.UserCreate.as_view()),
#employee
    path('employeeList/', employeeViews.EmployeeList.as_view()),
    path('empCreate/', employeeViews.EmployeeCreate.as_view()),
    path('employee/<int:pk>/', employeeViews.EmployeeDetail.as_view()),
    path('employee/<int:pk>/delete', employeeViews.EmployeeDetail.as_view()),
    path('employee/<int:pk>/update', employeeViews.EmployeeDetail.as_view()),
#skill
    path('skillUpdateLevelUp/<int:pk>/', skillViews.SkillUpdateLevelUp.as_view()),
    path('skillUpdateLevelDown/<int:pk>/', skillViews.SkillUpdateLevelDown.as_view()),
    path('skillCreate/', skillViews.SkillCreate.as_view()), #remove later
    path('skillList/', skillViews.SkillList.as_view()),
    path('level/<int:pk>/<int:pk2>/', skillViews.increase_level),
#roles
    path('roles/', roleViews.RoleList.as_view()),
#types
    path('typeListCreate/', typeViews.TypeListCreate.as_view()),
#auth
    path('refresh/', refresh_jwt_token),
    path('login/', obtain_jwt_token),
    # path('logout/', )
]

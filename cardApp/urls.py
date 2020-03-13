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
from django.conf.urls import include, url
from main.views import auth, userViews, employeeViews, roleViews, skillViews, typeViews
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from main.views.imageUpload import ImageUploadView, ImageView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
#boss
    path('userCreate/', userViews.UserCreate.as_view()),
#employee
    path('employeeList/', employeeViews.EmployeeList.as_view()),
    path('empCreate/', employeeViews.EmployeeCreate.as_view()),
    path('employee/<int:pk>/', employeeViews.EmployeeDetail.as_view()),
    path('employee/skill/<int:pk>/', employeeViews.retrieve_employee),
    path('employee/<int:pk>/delete', employeeViews.EmployeeDetail.as_view()),
    path('employee/<int:pk>/update', employeeViews.EmployeeDetail.as_view()),
    path('employee/levelUp/<int:pk>/<int:pk2>/', skillViews.increase_level),
    path('employee/levelDown/<int:pk>/<int:pk2>/', skillViews.dec_level),
#skill
    path('skillCreate/', skillViews.SkillCreate.as_view()), #remove later
    path('skillList/', skillViews.SkillList.as_view()),
#roles
    path('roles/', roleViews.RoleList.as_view()),
#types
    path('typeListCreate/', typeViews.TypeListCreate.as_view()),
#auth
    path('refresh/', refresh_jwt_token),
    path('login/', obtain_jwt_token),
    # path('logout/', )
#autodocx
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#image
    path('employee/<int:pk>/image/', ImageUploadView.as_view()),
#images
    path('image/', ImageView.as_view()),
]

# if settings.DEBUG:
#     urlpatterns += [
#         re_path(r'^media/(?P<path>.*)$', serve, {
#             'document_root': settings.MEDIA_ROOT,
#         }),
#     ]

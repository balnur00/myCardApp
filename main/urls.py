from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employeeList/', views.EmployeeList.as_view()),
]

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
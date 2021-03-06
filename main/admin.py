from django.contrib import admin
from main.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Skill)
admin.site.register(Type)
admin.site.register(Role)
admin.site.register(Image)

# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# from django.utils.translation import ugettext_lazy as _
#
# from .models import User
#
#
# @admin.register(User)
# class UserAdmin(DjangoUserAdmin):
#     """Define admin model for custom User model with no email field."""
#
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ('email', 'first_name', 'last_name', 'is_staff')
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email',)
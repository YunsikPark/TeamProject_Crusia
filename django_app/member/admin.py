from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import MyUser


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields':
                                  ('user_type',
                                   'first_name', 'last_name',
                                   'email', 'img_profile',
                                   'gender', 'birthday',
                                   'phone_num', 'preference_language',
                                   'preference_currency', 'living_site',
                                   'introduce',)}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


# admin.site.register(MyUser)
# admin.site.register(MyUser, UserAdmin)
admin.site.register(MyUser, MyUserAdmin)

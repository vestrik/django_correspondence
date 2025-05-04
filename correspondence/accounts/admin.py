from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import Department, UserDepartment


class UserDepartmentInline(admin.StackedInline):
    model = UserDepartment
    can_delete = False
    verbose_name_plural = 'UserDepartment'


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserDepartmentInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserDepartment)
admin.site.register(Department)
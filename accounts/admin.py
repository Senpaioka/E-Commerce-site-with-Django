from django.contrib import admin
from accounts.models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class AccountAdmin(UserAdmin):

    list_display = ['email', 'username', 'last_login', 'is_active']
    filter_horizontal = []
    list_filter = []
    ordering = ["-date_joined"]
    fieldsets = [
        (None, {"fields": ["username" ,"email", "password"]}),
        ("Personal info", {"fields": ["first_name", "last_name", "phone_number"]}),
        ("User activity", {"fields": ["last_login", "date_joined"]}),
        ("Status", {"fields": ["is_active" ,"is_admin", "is_staff", "is_superuser"]}),
    ]
    readonly_fields = ['date_joined', 'last_login']
    list_display_links = ["email" ,"username"]

admin.site.register(Account, AccountAdmin)
from django.contrib import admin

# Register your models here.
# from .models import UserInfo

admin.site.site_header = '个人博客管理平台'
admin.site.site_title = '博客平台'
admin.site.index_title = '欢迎使用'


class UserInfoAdmin(admin.ModelAdmin):

    list_per_page = 5


# admin.site.register(UserInfo,UserInfoAdmin)
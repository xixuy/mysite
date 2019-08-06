from django.contrib import admin
from .models import Artical
# Register your models here.


#列表页选项
class ArticalAdmin(admin.ModelAdmin):
    list_display = ['id','title','datetime']
    list_per_page = 5  #默认每页显示5条


# 在管理页面中注册模型类
admin.site.register(Artical,ArticalAdmin)
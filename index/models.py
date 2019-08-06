from django.db import models

# Create your models here.


class Artical(models.Model):
    title=models.CharField(max_length=50,verbose_name='标题')
    A_content=models.CharField(max_length=1000,verbose_name='文章内容')
    datetime=models.DateField(verbose_name='日期')
    sign=models.CharField(max_length=10,verbose_name='标签')
    #返回中文值
    # def __init__(self):
    #     return self.title

    class Meta:
        db_table = 'tb_artical'
        verbose_name='文章表'
        verbose_name_plural=verbose_name

from django.db import models

# Create your models here.

class Whisper(models.Model):
    user=models.CharField(max_length=30)
    W_content=models.CharField(max_length=1000)
    datetime=models.DateTimeField()

    class Meta:
        db_table = 'tb_whisper'
        verbose_name='微语'
        verbose_name_plural=verbose_name

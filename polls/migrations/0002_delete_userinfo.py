# Generated by Django 2.1.2 on 2018-12-04 02:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='userinfo',
        ),
    ]
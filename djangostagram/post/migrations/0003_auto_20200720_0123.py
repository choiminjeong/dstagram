# Generated by Django 3.0.8 on 2020-07-19 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20200719_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imgurl',
            field=models.CharField(max_length=128, verbose_name='이미지 주소'),
        ),
    ]

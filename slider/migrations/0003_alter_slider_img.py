# Generated by Django 3.2.5 on 2021-09-11 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_alter_slider_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(default='slider/static/slider/default.jpg', upload_to='slider/static/slider/images'),
        ),
    ]

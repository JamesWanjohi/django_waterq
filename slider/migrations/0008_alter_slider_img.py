# Generated by Django 3.2.5 on 2022-04-18 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0007_alter_slider_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(default='static/slider/imgs/default.jpg', upload_to='static/slider/imgs'),
        ),
    ]

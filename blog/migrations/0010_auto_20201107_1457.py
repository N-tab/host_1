# Generated by Django 3.1.3 on 2020-11-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201107_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
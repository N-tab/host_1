# Generated by Django 3.1.3 on 2020-11-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20201107_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
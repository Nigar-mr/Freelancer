# Generated by Django 2.2.3 on 2019-07-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0026_auto_20190706_0750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniqemodel',
            name='header_subtitle',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='uniqemodel',
            name='header_title',
            field=models.CharField(max_length=200),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-04 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0014_auto_20190704_1029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmodel',
            name='button_link',
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0008_auto_20190704_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutmodel',
            name='button_link',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='aboutmodel',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
# Generated by Django 2.2.3 on 2019-07-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0029_auto_20190706_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutmodel',
            name='text',
        ),
        migrations.AddField(
            model_name='aboutmodel',
            name='left_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

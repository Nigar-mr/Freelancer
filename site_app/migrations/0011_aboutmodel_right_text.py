# Generated by Django 2.2.3 on 2019-07-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0010_auto_20190704_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='right_text',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

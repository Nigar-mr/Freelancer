# Generated by Django 2.2.3 on 2019-07-04 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0011_aboutmodel_right_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutmodel',
            name='background_color',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
